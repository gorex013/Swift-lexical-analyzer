from src.lexer.swift_tokens import keywords
from src.syntaxer.code_block import CodeBlock
from src.syntaxer.condition_list import ConditionList


class IfStatement:
    trigger_token = keywords['if']
    pass


class ElseClause:
    trigger_token = keywords['else']

    pass


def if_init(self, condition_list: ConditionList, code_block: CodeBlock, else_clause: ElseClause = None):
    if condition_list is None or len(condition_list.condition_list) == 0:
        raise Exception("If statement without condition is not valid!!!")
    self.condition_list = condition_list
    self.code_block = code_block
    self.else_clause = else_clause


def else_init(self, code_block: CodeBlock = None, if_statement: IfStatement = None):
    if code_block is None and if_statement is None:
        raise Exception("After else should be a code block or an if statement!!!")
    self.code_block = code_block
    self.if_statement = if_statement


IfStatement.__init__ = if_init
ElseClause.__init__ = else_init


def if_dict(self):
    result = '"if-statement":{' + self.code_block.dict()
    if self.else_clause is not None:
        result += ',' + self.else_clause.dict()
    result += '}'
    return result


def else_dict(self):
    result = '"else-clause":{'
    if self.code_block is None:
        result += self.if_statement.dict()
    else:
        result += self.code_block.dict()
    result += '}'
    return result


IfStatement.dict = if_dict
ElseClause.dict = else_dict
