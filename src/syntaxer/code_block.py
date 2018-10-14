from src.lexer.swift_tokens import delimiters
from src.syntaxer.statement import Statement


class CodeBlock:
    trigger_token = delimiters['{']

    def __init__(self):
        self.statements = []

    def add_statement(self, statement: Statement = None):
        self.statements.append(statement)

    def add_statement_list(self, statement_list: list):
        for e in statement_list:
            self.add_statement(e)

    def dict(self):
        result = '"code-block":{'
        for e in self.statements:
            result += e.dict + ','
        result += '}'
