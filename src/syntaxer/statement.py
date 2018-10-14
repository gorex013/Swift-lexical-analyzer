from src.lexer.swift_tokens import keywords, delimiters
from src.syntaxer.condition_list import ConditionList, Condition
from src.syntaxer.if_statement import IfStatement


class Statement:
    def __init__(self, value):
        self.value = value

    def dict(self):
        return '"statement":{' + self.value.dict() + '}'

    @staticmethod
    def parse_statement(tokens: list):
        for i in range(len(tokens)):
            if tokens[i] is keywords['if'] or tokens[i] is keywords['while']:
                condition_strings = ''
                while tokens[i] is not delimiters['{']:
                    condition_strings += str(tokens[i]) + ' '
                    i += 1
                condition_strings = condition_strings.split(delimiters[','])
                condition_list = ConditionList()
                for e in condition_strings:
                    condition_list.add_condition(Condition(e))


if __name__ == '__main__':
    Statement.parse_statement([keywords['if'], ])