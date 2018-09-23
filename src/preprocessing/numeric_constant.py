import string

decimal = [i for i in string.digits]


def handle_number(literal):
    if is_binary(literal):
        return {'binary_integer': literal}
    elif is_octal(literal):
        return {'octal_integer': literal}
    elif is_hexadecimal(literal):
        return {'hexadecimal_integer': literal}
    elif is_double(literal):
        if is_integer(literal):
            return {'decimal_integer': literal}
        elif is_float(literal):
            return {'decimal_float': literal}
        else:
            return {'decimal_double': literal}
    raise Exception("How did you come here?")

def parse_natural(s: str):
    if s == '' or s is None:
        return ''
    result = ''
    for c in s:
        if c in decimal:
            result += c
        else:
            return result
    return result


def is_natural(s: str):
    natural = parse_natural(s)
    if natural is None:
        return False
    return len(natural) == len(s)


def parse_integer(s: str):
    if s == '' or s is None:
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


def is_integer(s: str):
    integer = parse_integer(s)
    if integer is None:
        return False
    return len(integer) == len(s)


def parse_float(s: str):
    if s == '' or s is None:
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
    float_n = parse_float(s)
    if float_n is None:
        return False
    return len(float_n) == len(s)


def parse_double(s: str):
    if s == '' or s is None:
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


def is_double(s: str):
    double = parse_double(s)
    if double is None:
        return False
    return len(double) == len(s)


binary = ['0', '1']


def parse_binary(s: str):
    result = ''
    if len(s) > 1 and s[0] == '0' and s[1] == 'b':
        for c in s[2:]:
            if c in binary:
                result += c
            else:
                return result
        return result
    return None


def is_binary(s: str):
    binary = parse_binary(s)
    if binary is None:
        return False
    return len(binary) == len(s)


octal = [i for i in string.octdigits]


def parse_octal(s: str):
    result = ''
    if len(s) > 1 and s[0] == '0' and s[1] == 'o':
        for c in s[2:]:
            if c in octal:
                result += c
            else:
                return result
        return result
    return None


def is_octal(s: str):
    octal = parse_octal(s)
    if octal is None:
        return False
    return len(octal) == len(s)


hexadecimal = [i for i in string.hexdigits]


def parse_hexadecimal(s: str):
    result = ''
    if len(s) > 1 and s[0] == '0' and s[1] == 'x':
        for c in s[2:]:
            if c in hexadecimal:
                result += c
            else:
                return result
        return result
    return None


def is_hexadecimal(s: str):
    hexadecimal = parse_hexadecimal(s)
    if hexadecimal is None:
        return False
    return len(hexadecimal) == len(s)


def is_number(s: str):
    double = is_double(s)
    binary = is_binary(s)
    hexad = is_hexadecimal(s)
    return double or binary or hexad
