import string

A = [string.digits]


def parse_natural(s=''):
    result = ''
    for c in s:
        if c in A:
            result += c
        else:
            return result
    return result


def parse_integer(s=''):
    if s == '':
        return ''
    if s[0] == '-':
        result = '-' + parse_natural(s[1:])
    elif s[0] == '+':
        result = parse_natural(s[1:])
    else:
        result = parse_natural(s)
    if result == '-' or result == '+':
        return ''
    else:
        return result


def parse_float(s=''):
    if s == '':
        return ''
    left = parse_integer(s)
    right = ''
    i = len(left)
    if i == len(s):
        return left
    if s[i] == '.':
        i += 1
        right = '.' + parse_natural(s[i:])
    if right == '.':
        return left
    else:
        return left + right


def parse_double(s=''):
    if s == '':
        return ''
    left = parse_float(s)
    right = ''
    i = len(left)
    if i == len(s):
        return left
    if s[i] == 'e' or s[i] == 'E':
        i += 1
        right = 'e' + parse_integer(s[i:])
    if right == 'e':
        return ''
    else:
        return left + right
