import src.Numbers.parse_natural as natural


def parse_integer(s=''):
    i = 0
    if s == '':
        return ''
    if s[i] == '-':
        result = '-' + natural.parse_natural(s[1:])
    elif s[i] == '+':
        result = natural.parse_natural(s[1:])
    else:
        result = natural.parse_natural(s)
    if result == '-' or result == '+':
        return ''
    else:
        return result
