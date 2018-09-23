from src.swift_tokens import *

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
