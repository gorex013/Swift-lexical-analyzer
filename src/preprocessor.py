from src.swift_tokens import *

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
