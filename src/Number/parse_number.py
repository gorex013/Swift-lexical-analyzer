import string

decimal = [i for i in string.digits]


def parse_natural(s=''):
    result = ''
    for c in s:
        if c in decimal:
            result += c
        else:
            return result
    return result


def is_natural(s):
    return len(parse_natural(s) == len(s))


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


def is_integer(s):
    return len(parse_integer(s)) == len(s)


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


def is_float(s):
    return len(parse_float(s)) == len(s)


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
        return left
    else:
        return left + right


def is_double(s):
    return len(parse_double(s)) == len(s)


binary = ['0', '1']


def parse_binary(s):
    result = ''
    if s[0] == '0' and s[1] == 'b':
        for c in s[2:]:
            if c in binary:
                result += c
            else:
                return result
        return result


def is_binary(s):
    return len(parse_binary(s)) == len(s)


octal = [i for i in string.octdigits]


def parse_octal(s):
    result = ''
    if s[0] == '0' and s[1] == 'o':
        for c in s[2:]:
            if c in octal:
                result += c
            else:
                return result
        return result


def is_octal(s):
    return len(parse_octal(s)) == len(s)


hexadecimal = [i for i in string.hexdigits]


def parse_hexadecimal(s):
    result = ''
    if s[0] == '0' and s[1] == 'x':
        for c in s[2:]:
            if c in hexadecimal:
                result += c
            else:
                return result
        return result


def is_hexadecimal(s):
    return len(parse_hexadecimal(s)) == len(s)


def is_number(s):
    return is_double(s) or is_binary(s) or is_octal(s) or is_hexadecimal(s)
