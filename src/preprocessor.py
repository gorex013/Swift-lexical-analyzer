from src.swift_tokens import *

temp_id = 0
storage = {}
def store(structure):
    global temp_id
    name = "TEMP{}".format(temp_id)
    storage[name] = structure
    temp_id += 1
    return name

def retrieve(name):
    return storage.get(name, None)

'''

'''


def preprocess_comments(content):
    multiline_cleaned = format_multiline_comment(content)
    inline_cleaned = format_inline_comment(multiline_cleaned)
    return inline_cleaned


'''

'''

def format_multiline_comment(content):
    start = content.find('/*')
    while start != -1:
        end = content.find('*/') + len('*/')
        comment = content[start:end]
        content = content.replace(comment, '')
        start = content.find('/*')
    return content


'''

'''


def format_inline_comment(content):
    start = content.find('//')
    while start != -1:
        end = content[start:].find('\n')  # End in a substring from start index
        if end == -1:
            end = len(content)
        end = start + end + 1

        comment = content[start:end]
        content = content.replace(comment, '')  # TODO Does it do for all cases
        start = content.find('//')
    return content


'''

'''


def delimiter_spacing(content):
    for key in delimiters.keys():
        content = content.replace(key, ' ' + delimiters[key] + ' ')
    return content


'''

'''


def operator_spacing(content):  # TODO: ADD PRIORITY <= first and < next
    for key in operators_priority:
        content = content.replace(key, ' ' + operators[key] + ' ')
    return content

def format_strings(content):
    inline = format_inline_strings(content)
    multiline = format_multiline_strings(inline)
    return multiline

def format_inline_strings(content):
    start = content.find('"')
    while start != -1:
        end = content.find('"') + len('"')
        string_literal = content[start:end]
        global temp_id
        new_word = store({string_literals['inline']: string_literal})
        content = content.replace(string_literal, new_word)
        start = content.find('"')
    return content

def format_multiline_strings(content):
    start = content.find('"""')
    while start != -1:
        end = content.find('"""') + len('"""')
        string_literal = content[start:end]
        global temp_id
        new_word = store({string_literals['multiline']: string_literal})
        content = content.replace(string_literal, new_word)
        start = content.find('"""')
    return content