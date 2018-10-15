from src.lexer.swift_tokens import keywords, delimiters


def parse_try_operator(tokens: list, i: int) -> (str, int):
    result = '"try-operator":'
    if tokens[i] is keywords['try']:
        result += '"try'
        i += 1
        if tokens[i] == delimiters['?']:
            result += '?'
        elif tokens[i] == delimiters['!']:
            result += '!'
        return result + '"', i
    else:
        return '', i


def parse_prefix_operator(tokens: list, i: int) -> (dict, int):
    result = {}
    if tokens[i][:2] == 'O_':
        result["prefix-operator"] = tokens[i]
        i += 1
        return result, i
    else:
        return None, i


def parse_primary_expression(tokens, i) -> (str, int):
    result = {"primary-expression": {}}
    return result, i


def parse_postfix_expression(tokens: list, i: int) -> (dict, int):
    result = {}
    result["postfix-expression"], i = parse_primary_expression(tokens, i)
    if result is not None:
        return result, i
    return None, i


def parse_prefix_expression(tokens: list, i: int) -> (dict, int):
    result = {}
    if tokens[i] is delimiters['&']:
        i += 1
        if tokens[i][0] == '{' and tokens[i].index('\'identifier\'') == 2:
            result["prefix-expression"] = {
                "symbol": '"' + delimiters['&'] + '"',
                "identifier": tokens[i]
            }
            return result, i
        else:
            return None, i - 1

    part, i = parse_prefix_operator(tokens, i)
    if part != '':
        if result != '':
            result += ','
        result += part
    part, i = parse_postfix_expression(tokens, i)
    if part != '':
        if result != '':
            result += ','
        result += part + '}'
        return result, i
    else:
        return '', i


def parse_binary_expression(tokens: list, i: int) -> (dict, int):
    head = '"binary-expression":{'
    result = ''
    return result, i


def parse_expression(tokens: list, i: int) -> (dict, int):
    result = {}
    if tokens[i] == keywords['try']:
        part, i = parse_try_operator(tokens, i)
        result += part
    part, i = parse_prefix_expression(tokens, i)
    result += part
    part, i = parse_binary_expression(tokens, i)
    result += part
    if result is None:
        return result, i
    else:
        result["expression"] = result
    return result, i
