import src.Numbers.parse_natural as natural


def parse_integer(s=''):
    i = 0
    result = ''
    if s[i] == '-' and i == 0:
        result = '-' + natural.parse_natural(s[1:])
    else:
        result = natural.parse_natural(s)
    if result == '-':
        return ''
    else:
        return result
