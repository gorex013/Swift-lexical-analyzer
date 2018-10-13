import sys
# sys.path.append('..')

from src.lexer.swift_tokens import *


def delimiter_spacing(content):
    """
    Method provides spaces between delimiters and converts them into end representation
    :param content: source code
    :return: source code with transformed delimiters shifted by spaces
    """
    for key in delimiters.keys():
        content = content.replace(key, ' ' + delimiters[key] + ' ')
    return content


def operator_spacing(content):
    """
    Method provides spaces between operators and converts them into end representation
    Method also takes care of operators' priority, `<=` will be processed before `<` or `=`
    :param content: source code
    :return: source code with transformed delimiters shifted by spaces
    """
    for key in operators_priority:
        content = content.replace(key, ' ' + operators[key] + ' ')
    return content
