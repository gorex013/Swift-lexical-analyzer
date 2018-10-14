from src.syntaxer.code_block import CodeBlock
from src.syntaxer.condition_list import ConditionList


class RepeatWhile:
    def __init__(self, code_block: CodeBlock, condition_list: ConditionList):
        self.code_block = code_block
        self.condition_list = condition_list

    def dict(self):
        return '"repeat-while":{' + self.code_block.dict() + ',' \
               + self.condition_list.dict() + '}'
