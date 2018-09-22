import string

printable_chars = [i for i in string.printable]


def get_string_literal(s):
    start = s.find('"')
    temp = start + s[start:].find('"')
    while s[temp - 1] == "\\" and s[temp - 2] != "\\":
        temp = s[temp:].find('"')
    return s[start: temp + 1]


def is_string(s):
    result = ''
    for c in s[1:len(s) - 1]:
        if c in printable_chars:
            result += c
        else:
            return result
    return s[0] == "\"" and s[len(s) - 1] == "\"" and len(result) == len(s)
