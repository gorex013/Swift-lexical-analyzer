import string

A = [i for i in string.ascii_letters] + ['_']

digits = [i for i in string.digits]
B = A + digits


def parse_identifier(s=''):
    result = ''
    if s == '':
        return ''
    elif s[0] == '$':
        result += s[0]
        for c in s[1:]:
            if c in digits:
                result += c
            else:
                return result
        return result
    elif s[0] in A:
        result += s[0]
        for c in s[1:]:
            if c in B:
                result += c
            else:
                return result
        return result
    else:
        return ''
