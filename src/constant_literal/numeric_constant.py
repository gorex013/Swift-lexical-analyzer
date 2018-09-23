import string

decimal = [i for i in string.digits]


def parse_natural(input_string: str):
    if input_string == '' or input_string is None:
        return ''
    result = ''
    for c in input_string:
        if c in decimal:
            result += c
        else:
            return result
    return result


def is_natural(input_string: str):
    return len(parse_natural(input_string)) == len(input_string) and input_string != '' and input_string is not None


def parse_integer(input_string: str):
    if input_string == '' or input_string is None:
        return ''
    if input_string[0] == '-':
        result = '-' + parse_natural(input_string[1:])
    elif input_string[0] == '+':
        result = parse_natural(input_string[1:])
    else:
        result = parse_natural(input_string)
    if result == '-' or result == '+':
        return ''
    else:
        return result


def is_integer(input_string: str):
    return len(parse_integer(input_string)) == len(input_string) and input_string != '' and input_string is not None


def parse_float(input_string: str):
    if input_string == '' or input_string is None:
        return ''
    left = parse_integer(input_string)
    right = ''
    i = len(left)
    if i == len(input_string):
        return left
    if input_string[i] == '.':
        i += 1
        right = '.' + parse_natural(input_string[i:])
    if right == '.':
        return left
    else:
        return left + right


def is_float(input_string):
    return len(parse_float(input_string)) == len(input_string) and input_string != '' and input_string is not None


def parse_double(input_string: str):
    if input_string == '' or input_string is None:
        return ''
    left = parse_float(input_string)
    right = ''
    i = len(left)
    if i == len(input_string):
        return left
    if input_string[i] == 'e' or input_string[i] == 'E':
        i += 1
        right = 'e' + parse_integer(input_string[i:])
    if right == 'e':
        return left
    else:
        return left + right


def is_double(input_string: str):
    return len(parse_double(input_string)) == len(input_string) and input_string != '' and input_string is not None


binary = ['0', '1']


def parse_binary(input_string: str):
    if input_string == '' or input_string is None:
        return ''
    result = ''
    if input_string[0] == '0' and input_string[1] == 'b':
        result = '0b'
        for c in input_string[2:]:
            if c in binary:
                result += c
            else:
                return result
    if result == '0b' or result == '':
        return ''
    return result


def is_binary(input_string: str):
    return len(parse_binary(input_string)) == len(input_string) and input_string != '' and input_string is not None


octal = [i for i in string.octdigits]


def parse_octal(input_string: str):
    if input_string == '' or input_string is None:
        return ''
    result = ''
    if input_string[0] == '0' and input_string[1] == 'o':
        result = '0o'
        for c in input_string[2:]:
            if c in octal:
                result += c
            else:
                return result
    if result == '0o' or result == '':
        return ''
    return result


def is_octal(input_string: str):
    return len(parse_octal(input_string)) == len(input_string) and input_string != '' and input_string is not None


hexadecimal = [i for i in string.hexdigits]


def parse_hexadecimal(input_string: str):
    if input_string == '' or input_string is None:
        return ''
    result = ''
    if input_string[0] == '0' and input_string[1] == 'x':
        result = '0x'
        for c in input_string[2:]:
            if c in hexadecimal:
                result += c
            else:
                return result
    if result == '0x' or result == '':
        return ''
    return result


def is_hexadecimal(s: str):
    return len(parse_hexadecimal(s)) == len(s) and s != '' and s is not None


def is_number(s: str):
    return is_double(s) or is_binary(s) or is_octal(s) or is_hexadecimal(s)
