import src.preprocessing.string_literals as str_lit
import src.preprocessing.comments as com
import src.preprocessing.escaping as esc
from src.swift_tokens import *
import src.preprocessing.numeric_constant as number_literal
import argparse


def format_file(src_fname):
    """
    Method processes file with lexical analyzer
    :param src_fname: name of file
    :return: list of tokens
    """
    with open(src_fname) as f:
        content = f.read()
        return process(content)


def process(content: str) -> list:
    """
    Method processes source code with lexical analyzer
    :param content: source code
    :return: list of tokens
    """
    comments_filtered = com.preprocess_comments(content)  # Get rid of comments
    formatted_strings = str_lit.format_strings(comments_filtered)  # Convert string literals
    delimiters_escaped = esc.delimiter_spacing(formatted_strings)  # Escape & transform delimiters
    operators_escaped = esc.operator_spacing(delimiters_escaped)  # Escape & transform operators
    tokens_list = keywords_replacement(operators_escaped)  # Reverse string literals, handle numbers & identifiers
    return tokens_list


def handle_literal(literal: str):
    """
    Method handles last part of lex analysis:
        1) Reverses string literals
        2) Handles numbers
        3) Handles identifiers
    :param literal: word
    :return: new token
    """
    # On `repl.it` swift doesn't recognize multi-line strings
    if number_literal.is_number(literal):
        return number_literal.handle_number(literal)
    elif 'TEMP' in literal:  # Literals are substituted by TEMP#, where # is index of the literal (read string_literals)
        return str_lit.retrieve(literal)
    else:
        return {'identifier': literal}


def process_token(word: str) -> str:
    """
    Method transforms word into keyword/delimiter or operator
    It is checked that the word is one of them for sure
    :param word:
    :return: new token
    """
    keyword = keywords.get(word, None)
    delimiter = delimiters.get(word, None)
    operator = operators.get(word, None)
    # Can be optimized

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
    """
    Method checks is the word a keyword/delimiter or operator
    :param word:
    :return: true or false
    """
    is_keyword = keywords.get(word, None)
    is_delimiter = delimiters.get(word, None)
    is_operator = operators.get(word, None)
    return is_operator is not None or is_keyword is not None or is_delimiter is not None


def is_processed(word: str) -> bool:
    """
    Method checks has the word already been processed or not
    During `escaping` phase it can happen with delimietrs & operators
    :param word: to check
    :return: true or false
    """
    is_keyword = word in keywords.values()
    is_delimiter = word in delimiters.values()
    is_operator = word in operators.values()
    return is_operator or is_keyword or is_delimiter


def keywords_replacement(content: str) -> list:
    """
    Method splits whole code by space and transforms into tokens
    :param content:
    :return:
    """
    words = content.split(' ')
    for i in range(len(words)):
        words[i] = words[i].strip()  # Get rid of \n, \r, spaces, etc.

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
    parser = argparse.ArgumentParser(description='Lexical analyzer')
    parser.add_argument('input', metavar='in', type=str,
                        help='Full path to file to process by Swift Lexical analyzer')
    parser.add_argument('output', metavar='out', type=str,
                        help='Path to store tokens')

    args = parser.parse_args()
    input_file = args.input
    out_file = args.output

    with open(input_file) as f:
        content = f.read()
    tokens = process(content)
    with open(out_file, 'w') as f:
        for token in tokens:
            f.write("{}\n".format(token))