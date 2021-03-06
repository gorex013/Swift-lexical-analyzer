import json
from src.lexer.lexical_analyzer import lexer
from src.lexer.swift_tokens import delimiters, keywords
from src.syntaxer.ObjectTrees import Expression


def parse_condition_list(tokens: list, i: int) -> (dict, int):
    result = {}
    j = tokens[i:].index(delimiters['{'])
    result["condition"], i = tokens[i:i + j], i + j
    return result, i


def parse_else_clause(tokens: list, i: int) -> (dict, int):
    result = {}
    print(i)
    if tokens[i] != keywords['else']:
        return None, i
    i += 1
    if tokens[i] == keywords['if']:
        result["if-statement"], i = parse_if_statement(tokens, i + 1)
    elif tokens[i] == delimiters['{']:
        result["code-block"], i = parse_code_block(tokens, i)
    return result, i


def parse_if_statement(tokens: list, i: int) -> (dict, int):
    result = {}
    if tokens[i] == keywords['if']:
        i += 1
    result["condition-list"], i = parse_condition_list(tokens, i)
    result["code-block"], i = parse_code_block(tokens, i)

    # if tokens[i] == keywords['else']:
    #     result["else-clause"], i = parse_else_clause(tokens, i + 1)
    result = {"if-statement": result}
    return MyIf(result), i

class MyIf(Expression):
    def __init__(self, obj):
        self.cond_list = obj['if-statement']['condition-list']
        self.code = obj['if-statement']['code-block']['statements']['statement']
        self.elseclause = None
        if obj['if-statement'].get('else-clause', None) is not None:
            self.elseclause = obj['if-statement']['else-clause']


    def dict_representation(self):
        return {
            'condition-list': self.cond_list,
            'code-block': self.code,
            'code-block': self.elseclause,
        }


def parse_code_block(tokens: list, i: int) -> (dict, int):
    result = {
        "statements": {}
    }
    k = 1
    j = i
    while k > 0 and j < len(tokens):
        if tokens[j] == delimiters['{']:
            k += 1
        elif tokens[j] == delimiters['}']:
            k -= 1
        j += 1
    result["statements"]["statement"] = tokens[i + 1:j - 1]
    return result, j
