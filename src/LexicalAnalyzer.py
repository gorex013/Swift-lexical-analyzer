import src.preprocessing.string_literals as str_lit
import src.preprocessing.comments as com
import src.preprocessing.escaping as esc
from src.swift_tokens import *
import src.preprocessing.numeric_constant as number_literal

def format_file(src_fname):
    with open(src_fname) as f:
        content = f.read()
        return format(content)


def format(content: str) -> list:
    comments_filtered = com.preprocess_comments(content)
    formatted_strings = str_lit.format_strings(comments_filtered)
    delimiters_escaped = esc.delimiter_spacing(formatted_strings)
    operators_escaped = esc.operator_spacing(delimiters_escaped)
    tokens_list = keywords_replacement(operators_escaped)
    return tokens_list

def handle_literal(literal: str):
    # On `repl.it` swift doesn't recognize multi-line strings
    if number_literal.is_number(literal):
        return number_literal.handle_number(literal)
    elif 'TEMP' in literal: #TODO: more explanation
        return str_lit.retrieve(literal)
    else:
        return {'identifier': literal}



def process_token(word: str) -> str:
    keyword = keywords.get(word, None)
    delimiter = delimiters.get(word, None)
    operator = operators.get(word, None)

    truth = (keyword is not None) + (delimiter is not None) + (operator is not None)
    if truth > 1 or truth == 0:
        raise Exception("Tokens meaning exception: IS IT EVEN POSSIBLE?")

    if keyword is not None:
        return keyword
    elif delimiter is not None:
        return delimiter
    elif operator is not None:
        return operator


def is_special(word: str) -> bool:
    is_keyword = keywords.get(word, None)
    is_delimiter = delimiters.get(word, None)
    is_operator = operators.get(word, None)
    return is_operator is not None or is_keyword is not None or is_delimiter is not None


def is_processed(word: str) -> bool:
    is_keyword = word in keywords.values()
    is_delimiter = word in delimiters.values()
    is_operator = word in operators.values()
    return is_operator or is_keyword or is_delimiter


def keywords_replacement(content: str) -> list:
    words = content.split(' ')
    for i in range(len(words)):
        words[i] = words[i].strip()

    words = [w for w in words if w is not '']

    for i in range(len(words)):
        if is_processed(words[i]):
            continue
        elif is_special(words[i]):
            words[i] = process_token(words[i])
        else:
            words[i] = handle_literal(words[i]) # TODO: Maybe there's another way to fix it
    return words

if __name__ == '__main__':
    with open('swift_examples/BTree.swift') as f:
        content = f.read()
    tokens = format(content)
    with open('swift_examples/out.txt', 'w') as f:
        for token in tokens:
            f.write("{}\n".format(token))