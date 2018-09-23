from src.swift_tokens import *

temp_id = 0  # Stores current index of last item in a storage
storage = {}  # Storage for literals

# Sometimes we can meet print("val a = \(a)")
# This way we hide literals from post-processing by delimiters/operators/keywords, etc.

def store(structure):
    """
    Method stores literal in local storage
    Not-thread safe!
    :param structure: object to store
    :return: temp name for this literal
    """
    global temp_id
    name = "TEMP{}".format(temp_id)
    storage[name] = structure
    temp_id += 1
    return name

def retrieve(name):
    """
    Method returns literal object by name
    :param name: temp name
    :return: object or None
    """
    return storage.get(name, None)


def format_strings(content):
    """
    Method combines transformation of inline and multiline strings
    Converts them to temp names (TEMP0, TEMP1, etc.)
    :param content: source code
    :return: code with TEMP# names instead of string literals
    """
    multiline = format_multiline_strings(content)
    inline = format_inline_strings(multiline)
    return inline

def format_inline_strings(content):
    """
    Method converts inline string literals into TEMP#
    :param content: source code
    :return: code without inline literals and with TEMP# instead
    """
    start = content.find('"')
    shift = len('"')
    while start != -1:
        end = start + shift + content[start + len('"'):].find('"') + shift  # Takes care of correct substring size
        string_literal = content[start:end]

        global temp_id
        literal_index = store({string_literals['inline']: string_literal})
        content = content.replace(string_literal, literal_index)
        start = content.find('"')
    return content

def format_multiline_strings(content):
    """
    Method converts multiline string literals into TEMP#
    :param content: source code
    :return: code without multiline literals and with TEMP# instead
    """
    start = content.find('"""')
    shift = len('"""')
    while start != -1:
        end = start + shift + content[start + shift:].find('"""') + shift  # Takes care of correct substring size
        string_literal = content[start:end]

        global temp_id
        literal_index = store({string_literals['multiline']: string_literal})
        content = content.replace(string_literal, literal_index)
        start = content.find('"""')
    return content