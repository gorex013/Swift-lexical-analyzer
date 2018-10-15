from src.lexer.swift_tokens import keywords
from src.govno_cod.code_block import *
from src.govno_cod.condition_list import ConditionList, Condition


class Statement:
    def __init__(self, value):
        self.value = value

    def dict(self):
        return '"statement":{' + self.value + '}'

    @staticmethod
    def parse_statement(tokens: list, i: int):
        while i < len(tokens):
            if tokens[i] is keywords['if'] or tokens[i] is keywords['while']:
                condition_strings = ''
                while tokens[i] is not delimiters['{']:
                    condition_strings += str(tokens[i]) + ' '
                    i += 1
                condition_strings = condition_strings.split(delimiters[','])
                condition_list = ConditionList()
                for e in condition_strings:
                    condition_list.add_condition(Condition(e))
                code_block = CodeBlock()
                if tokens[i] is delimiters['{']:
                    i += 1
                    statement = Statement.parse_statement(tokens, i)
                    code_block.add_statement(statement)
                if tokens[i] is delimiters['}']:
                    pass