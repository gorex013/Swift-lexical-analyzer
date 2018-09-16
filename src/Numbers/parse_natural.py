Q = [0]
A = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def parse_natural(s=''):
    result = ''
    for c in s:
        if c in A:
            result += c
        else:
            return result
    return result
