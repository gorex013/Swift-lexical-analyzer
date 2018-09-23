from src.swift_tokens import *

temp_id = 0
storage = {}

'''
'''
def store(structure):
    global temp_id
    name = "TEMP{}".format(temp_id)
    storage[name] = structure
    temp_id += 1
    return name
'''
'''
def retrieve(name):
    return storage.get(name, None)


def format_strings(content):
    multiline = format_multiline_strings(content)
    inline = format_inline_strings(multiline)
    return inline

def format_inline_strings(content):
    start = content.find('"')
    shift = len('"')
    while start != -1:
        end = start + shift + content[start + len('"'):].find('"') + shift
        string_literal = content[start:end]

        global temp_id
        literal_index = store('inline_literal.({})'.format(string_literal))
        content = content.replace(string_literal, literal_index)
        start = content.find('"')
    return content

def format_multiline_strings(content):
    start = content.find('"""')
    shift = len('"""')
    while start != -1:
        end = start + shift + content[start + shift:].find('"""') + shift
        string_literal = content[start:end]

        global temp_id
        literal_index = store('multiline_literal.({})'.format(string_literal))
        content = content.replace(string_literal, literal_index)
        start = content.find('"""')
    return content