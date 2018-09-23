import string

# `decimal` is the list of decimal digits.
# The same for `binary`, `octal`, `hexadecimal` with respective digits
# There is parser and checker methods for natural, integer, float, double,
# binary, octal and hexadecimal numbers
# Every method takes as input a string and returns the substring that follows the rules
# (e.g. '0b0101001', rule is that every binary number starts with '0b'
# and contains after only 0's and 1's).

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
    natural = parse_natural(input_string)
    return len(natural) == len(input_string) and input_string != '' and input_string is not None


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
    if input_string[0] == '+':
        input_string = input_string[1:]
    integer = parse_integer(input_string)
    return len(integer) == len(input_string) and input_string != '' and input_string is not None


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
    s = parse_float(input_string)
    return len(s) == len(input_string) and input_string != '' and input_string is not None


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
    double_ = parse_double(input_string)
    return len(double_) == len(input_string) and input_string != '' and input_string is not None


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
                break
    if result == '0b' or result == '':
        return ''
    return result


def is_binary(input_string: str):
    binary = parse_binary(input_string)
    return len(binary) == len(input_string) and input_string != '' and input_string is not None


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
                break
    if result == '0o' or result == '':
        return ''
    return result


def is_octal(input_string: str):
    octal = parse_octal(input_string)
    return len(octal) == len(input_string) and input_string != '' and input_string is not None


hexadecimal = [i for i in string.hexdigits]


def parse_hexadecimal(input_string: str):
    if input_string == '' or input_string is None:
        return ''
    result = ''
    if len(input_string) > 1 and input_string[0] == '0' and input_string[1] == 'x':
        result = '0x'
        for c in input_string[2:]:
            if c in hexadecimal:
                result += c
            else:
                break
    if result == '0x' or result == '':
        return ''
    return result


def is_hexadecimal(input_string: str):
    hexadecimal_ = parse_hexadecimal(input_string)
    return len(hexadecimal_) == len(input_string) and input_string != '' and input_string is not None


def is_number(input_string: str):
    double_ = is_double(input_string)
    binary_ = is_binary(input_string)
    octal_ = is_octal(input_string)
    hexadecimal_ = is_hexadecimal(input_string)
    return double_ or binary_ or octal_ or hexadecimal_
