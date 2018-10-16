def parse_term(tokens: list, i: int) -> (dict, int):
    result = {}
    result = {"term": result}
    return result, i


def parse_simple_expression(tokens: list, i: int) -> (dict, int):
    term, i = parse_term(tokens, i)

    return None, i
