from src.lexer.lexical_analyzer import lexer
from src.lexer.swift_tokens import *
from src.syntaxer.grammars import *

def transform_main(tokens):
    copied = list(tokens)
    copied = transform_funcs(copied)
    copied = parse_expression(copied)
    return copied


def transform_funcs(tokens):
    tok_copy = list(tokens)
    func_def = keywords['func']

    while True:
        if func_def in tok_copy:
            func_index = tok_copy.index(func_def)
            foo, p = FunctionDeclarationGrammar(tok_copy, func_index).process_func()
            end_code_block = wrap_code_block(tok_copy, p)
            code_block_parsed = parse_expression(tok_copy[p + 1:end_code_block])
            foo.fbody = code_block_parsed
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


def parse_expression(tokens):
    copied = list(tokens)
    # copied = transform_ifs(copied)
    # copied = transform_cycles(copied)
    for i in range(len(copied)):
        is_dict = type(copied[i]) is dict

        if copied[i] == keywords['var'] or copied[i] == keywords['let']:
            vgrammar = VariableCreationGrammar(copied, i)
            vars, pointer = vgrammar.process_var_definition()
            l1 = copied[0: i]
            l2 = copied[pointer:]
            copied = l1 + vars + l2
            return parse_expression(copied)

        size_fits = i + 1 < len(copied)
        is_fcall = is_dict and copied[i].get('identifier', None) is not None and copied[i + 1] == 'DEL_LP'
        if size_fits and is_fcall:
            foo, pointer = parse_function_call(copied, i)
            l1 = copied[0: i]
            l2 = copied[pointer:]
            copied = l1 + [foo] + l2
            return parse_expression(copied)

    return copied

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
    results = transform_main(tokens)
    print(results)

