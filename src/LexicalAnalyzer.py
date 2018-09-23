import src.preprocessor as ps
from src.swift_tokens import *
import src.constant_literal.numeric_constant as number_literal
import src.constant_literal.string_constant as string_literal

def format_file(src_fname):
    with open(src_fname) as f:
        content = f.read()
        return format(content)


def format(content: str) -> list:
    comments_filtered = ps.preprocess_comments(content)
    formatted_strings = ps.format_strings(comments_filtered)
    delimiters_escaped = ps.delimiter_spacing(formatted_strings)
    operators_escaped = ps.operator_spacing(delimiters_escaped)
    tokens_list = keywords_replacement(operators_escaped)
    return tokens_list

def handle_literal(literal):  # TODO: Not sure about multi-line string in swift.
    # On `repl.it` swift doesn't recognize multi-line strings
    if number_literal.is_number(literal):
        return number_literal.handle_number(literal)
    elif string_literal.is_string(literal):
        return {'inline_string': literal}
    else:
        return {'unknown_literal': literal}



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
        if words[i] in 'return':
            print('?')

        if is_processed(words[i]):
            continue
        elif is_special(words[i]):
            words[i] = process_token(words[i])
        else:
            words[i] = handle_literal(words[i]) # TODO: Maybe there's another way to fix it
    return words


if __name__ == '__main__':
    tokens = format("""struct Stack<Element> {
    var items = [Element]()
    mutating func push(_ item: Element) {
        items.append(item)
    }
    mutating func pop() -> Element {
        return items.removeLast()
    }
}""")
    for _ in tokens:
        print(_)
