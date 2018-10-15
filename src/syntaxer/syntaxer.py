from src.lexer.lexical_analyzer import lexer
from src.lexer.swift_tokens import *
from src.syntaxer.grammars import *


def transform_funcs(tokens):
    tok_copy = list(tokens)
    func_def = keywords['func']

    while True:
        if func_def in tok_copy:
            func_index = tok_copy.index(func_def)
            foo, p = FunctionDeclarationGrammar(tok_copy, func_index).process_func()
            end_code_block = wrap_code_block(tok_copy, p)
            foo.fbody = tok_copy[p + 1:end_code_block - 1]
            l1 = tok_copy[0:func_index]
            l2 = tok_copy[end_code_block + 1:]
            tok_copy = l1 + [foo] + l2
        else:
            break

    return tok_copy


def transform_ifs(tokens):
    pass


def transform_cycles(tokens):
    pass

def wrap_code_block(tokens, pointer):
    stack = ['{']
    index = pointer + 1  # Should be guaranteed that next token is {
    # try:
    while len(stack) > 0:
        if tokens[index] == 'DEL_RCP':
            stack.pop()
        if tokens[index] == 'DEL_LCP':
            stack.append('{')
        index += 1
    # except Exception:
    #     print("Impossibru exception :: stack={} index={}".format(stack, index))
    #     return None

    return index - 1






if __name__ == '__main__':
    with open('test_funcs.txt') as f:
        content = f.read()
    tokens = lexer(content)
    results = transform_funcs(tokens)
    print(results)
