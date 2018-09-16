import src.Numbers.parse_float as float
import src.Numbers.parse_integer as integer


def parse_double(s=''):
    left = float.parse_float(s)
    right = ''
    i = len(left)
    if s[i] == 'e' or s[i] == 'E':
        i += 1
        right = 'e' + integer.parse_integer(s[i:])
    if right == 'e':
        return ''
    else:
        return left + right
