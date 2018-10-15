import json

from src.lexer.lexical_analyzer import lexer
from src.lexer.swift_tokens import keywords
from src.syntaxer.if_statement import parse_condition_list, parse_code_block


def parse_while_loop(tokens: list, i: int) -> (dict, int):
    result = {}
    if tokens[i] == keywords['while']:
        i += 1
    result["condition-list"], i = parse_condition_list(tokens, i)
    result["code-block"], i = parse_code_block(tokens, i)
    if result is None:
        return None, i
    result = {"while-loop": result}
    return result, i


code = """
while(x<10){
    x+=1
    print(x)
}
"""
# tokens = lexer(code)
# x, y = parse_while_loop(tokens, 0)
# print(json.dumps(x, sort_keys=True, indent=4, default=str))
