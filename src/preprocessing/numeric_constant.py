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

def parse_natural(input_string: str):
    result = ''
    for c in input_string:
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


def is_integer(s: str):
    integer = parse_integer(s)
    if integer is None:
        return False
    return len(integer) == len(s)

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


def is_float(s):
    float_n = parse_float(s)
    if float_n is None:
        return False
    return len(float_n) == len(s)

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


def is_double(s: str):
    double = parse_double(s)
    if double is None:
        return False
    return len(double) == len(s)

binary = ['0', '1']


def parse_binary(input_string: str):
    if input_string == '' or input_string is None:
        return ''
    result = ''
    if len(input_string) > 1 and input_string[0] == '0' and input_string[1] == 'b':
        result = '0b'
        for c in input_string[2:]:
            if c in binary:
                result += c
            else:
                return result
    return None


def is_binary(s: str):
    binary = parse_binary(s)
    if binary is None:
        return False
    return len(binary) == len(s)


octal = [i for i in string.octdigits]


def parse_octal(input_string: str):
    if input_string == '' or input_string is None:
        return ''
    result = ''

    if len(input_string) > 1 and input_string[0] == '0' and input_string[1] == 'o':
        result = '0o'
        for c in input_string[2:]:
            if c in octal:
                result += c
            else:
                return result
    return None


def is_octal(s: str):
    octal = parse_octal(s)
    if octal is None:
        return False
    return len(octal) == len(s)

hexadecimal = [i for i in string.hexdigits]


def parse_hexadecimal(input_string: str):
    if input_string == '' or input_string is None:
        return ''
    if len(input_string) > 1 and input_string[0] == '0' and input_string[1] == 'x':
        result = '0x'
        for c in input_string[2:]:
            if c in hexadecimal:
                result += c
            else:
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
