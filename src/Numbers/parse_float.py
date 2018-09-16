import src.Numbers.parse_integer as integer
import src.Numbers.parse_natural as natural


def parse_float(s=''):
    left = integer.parse_integer(s)
    right = ''
    i = len(left)
    if s[i] == '.':
        i += 1
        right = '.' + natural.parse_natural(s[i:])
    if right == '.':
        return left
    else:
        return left + right
