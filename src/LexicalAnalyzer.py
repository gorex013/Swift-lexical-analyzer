import src.preprocessor as ps
from src.swift_tokens import *


def format_file(src_fname):
    with open(src_fname) as f:
        content = f.read()
        return format(content)


def format(content: str) -> list:
    comments_filtered = ps.preprocess_comments(content)
    delimiters_escaped = ps.delimiter_spacing(comments_filtered)
    operators_escaped = ps.operator_spacing(delimiters_escaped)
    tokens_list = keywords_replacement(operators_escaped)
    return tokens_list

    # return is_delimiter or is_keyword or is_operator
    # TODO: Something wrong here, I don't know what is it doing? What to change?


import src.constant_literal.numeric_constant as number_literal
import src.constant_literal.string_constant as string_literal


def handle_literal(literal):  # TODO: Not sure about multi-line string in swift.
    # On `repl.it` swift doesn't recognize multi-line strings
    if number_literal.is_number(literal):
        if number_literal.is_binary(literal):
            return {'binary_integer': literal}
        elif number_literal.is_octal(literal):
            return {'octal_integer': literal}
        elif number_literal.is_hexadecimal(literal):
            return {'hexadecimal_integer': literal}
        elif number_literal.is_double(literal):
            if number_literal.is_integer(literal):
                return {'decimal_integer': literal}
            elif number_literal.is_float(literal):
                return {'decimal_float': literal}
            else:
                return {'decimal_double': literal}
    elif string_literal.is_string(literal):
        return {'inline_string': literal}


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
            words[i] = handle_literal(words[i])

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
