import json
from pprint import pprint

from src.govno_cod.expression import parse_expression
from src.lexer.lexical_analyzer import lexer


def parse_declaration(tokens: list, i: int) -> (str, int):
    head = '"declaration":{'
    result = ''
    return result, i


def parse_loop(tokens: list, i: int) -> (str, int):
    head = '"loop-statement":{'
    result = ''

    return result, i


def parse_branch(tokens: list, i: int) -> (str, int):
    head = '"branch-statement":{'
    result = ''
    return result, i


def parse_labeled(tokens: list, i: int) -> (str, int):
    head = '"labeled-statement":{'
    result = ''
    return result, i


def parse_control_transfer_statement(tokens: list, i: int) -> (str, int):
    head = '"control-transfer-statement":{'
    result = ''
    return result, i


def parse_defer_statement(tokens: list, i: int) -> (str, int):
    head = '"defer-statement":{'
    result = ''
    return result, i


def parse_do_statement(tokens: list, i: int) -> (str, int):
    head = '"do-statement":{'
    result = ''
    return result, i


def parse_compiler_control_statement(tokens: list, i: int) -> (str, int):
    head = '"compiler-control-statement":{'
    result = ''
    return result, i


def parse_statement(tokens: list, i: int) -> (str, int):
    head = '"statement":{'
    result = ''
    part, i = parse_expression(tokens, i)
    if part != '':
        result += part
    part, i = parse_declaration(tokens, i)
    if part != '':
        if result != '':
            result += ','
        result += part
    part, i = parse_loop(tokens, i)
    if part != '':
        if result != '':
            result += ','
        result += part
    part, i = parse_branch(tokens, i)
    if part != '':
        if result != '':
            result += ','
        result += part
    part, i = parse_labeled(tokens, i)
    if part != '':
        if result != '':
            result += ','
        result += part
    # part, i = parse_control_transfer_statement(tokens, i)
    # if part != '':
    #     if result != '':
    #         result += ','
    #     result += part
    # part, i = parse_defer_statement(tokens, i)
    # if part != '':
    #     if result != '':
    #         result += ','
    #     result += part
    # part, i = parse_do_statement(tokens, i)
    # if part != '':
    #     if result != '':
    #         result += ','
    #     result += part
    # part, i = parse_compiler_control_statement(tokens, i)
    # if part != '':
    #     if result != '':
    #         result += ','
    #     result += part
    if result == '':
        return '', i
    return head + result + '}', i


code = """
var x = 1
var y = 2
var z = x+y
if(x==y/2){
    x*2
} else {
    y = z*2 - y
    z = x+y
}
    """
code0 = 'try?'
tokens = lexer(code0)
x, y = parse_statement(tokens, 0)
pprint(x)
