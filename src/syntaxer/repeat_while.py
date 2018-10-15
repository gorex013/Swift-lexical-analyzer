import json

from src.lexer.lexical_analyzer import lexer
from src.syntaxer.if_statement import parse_code_block, parse_condition_list


def parse_repeat_while(tokens: list, i: int) -> (dict, int):
    result = {}
    result["code-block"], i = parse_code_block(tokens, i)
    result["condition-list"], i = parse_condition_list(tokens, i)
    if result is not None:
        result["repeat-while-loop"] = result
    return result, i


code = """
repeat{
    if x>2 {
        x+=1
    } else {
        x+=2
    }
}while(x<10)
    """
tokens = lexer(code)
x, y = parse_repeat_while(tokens, 0)
print(json.dumps(x, sort_keys=True, indent=4, default=str))
