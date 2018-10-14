from src.lexer.swift_tokens import keywords
from src.syntaxer.code_block import CodeBlock
from src.syntaxer.condition_list import ConditionList


class WhileLoop:
    trigger_token = keywords['while']

    def __init__(self, condition_list: ConditionList, code_block: CodeBlock):
        self.condition_list = condition_list
        self.code_block = code_block

    def dict(self):
        return '"while-loop":{' + self.condition_list.dict() + ',' + self.code_block.dict() + '}'
