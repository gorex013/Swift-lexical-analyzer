import re
import sys

# sys.path.insert(0, sys.path[0]+'/Swift-lexical-analyzer/syntaxer')

from src.lexer.LexicalAnalyzer import lexer
from src.syntaxer.function_parser import *


class FunctionGrammar:
    def __init__(self, tokens: list, pointer: int):
        self.tokens = tokens
        self.pointer = pointer
        self.fname = ''
        self.pnames = []
        self.ptypes = []
        self.rtypes = []
        self.states = {}

    class State:
        def __init__(self, name, final=False, action=None):
            self.transitions = {}
            self.final = final
            self.name = name
            self.action = action
            self.states = {}

        def make_transition(self, token):
            # if self.transitions.get(token, None) is None:
            #     raise FunctionParseException("Incorrect order of tokens {}".format(token))
            if self.action is not None:
                self.action(token)  # Действие должно быть завязано на объект Функция
            if type(token) is dict and token['identifier'] is not None:
                token = 'ID'  # Обработка случая, когда у меня {'identifier': 'sdfs'} приходит, а хотелос бы 'ID'
            if token.startswith("class_"):
                token = 'CLASS'

            index = self.transitions[token]
            return self.states[index]

    def save_name(self, identifier):
        name = identifier['identifier']
        self.fname = name

    def save_pname(self, pname):
        if type(pname) is dict:
            self.pnames.append(pname['identifier'])

    def save_ptype(self, ptype: str):
        class_len = len('class_')
        ptype = ptype[class_len:]
        self.ptypes.append(ptype)  # Work with types

    def save_rtype(self, rtype):
        if 'ARROW' not in rtype:
            class_len = len('class_')
            rtype = rtype[class_len:]
            self.rtypes.append(rtype)  # Work with types

    def process_func(self):
        self.states = {
            2: self.State(name='2', action=self.save_name),
            3: self.State(name='3'),
            4: self.State(name='4', action=self.save_pname),
            5: self.State(name='5'),
            6: self.State(name='6', action=self.save_rtype),
            7: self.State(name='7'),
            8: self.State(name='8'),
            9: self.State(name='9'),
            10: self.State(name='10', final=True),
            11: self.State(name='11'),
            12: self.State(name='12',  action=self.save_ptype),
            13: self.State(name='13'),
            14: self.State(name='14'),
            15: self.State(name='15'),
            16: self.State(name='16'),
            17: self.State(name='17', action=self.save_rtype),
            18: self.State(name='18'),
        }

        s = self.states
        s[2].transitions = {'ID': 3}
        s[3].transitions = {'DEL_LP': 4}
        s[4].transitions = {'ID': 11, 'DEL_RP': 5}
        s[5].transitions = {'DEL_ARROW': 6}
        s[6].transitions = {'CLASS': 7, 'DEL_LP': 15}
        s[7].transitions = {'DEL_LCP': 8}
        s[8].transitions = {'S_RETURN': 9}  # TODO: THERE SHOULD BE PARSED EXPRESSION
        s[9].transitions = {'DEL_RCP': 10}
        s[11].transitions = {'DEL_COLON': 12}
        s[12].transitions = {'CLASS': 13}
        s[13].transitions = {'DEL_COMMA': 14, 'DEL_RP': 5}
        s[14].transitions = {'ID': 11}
        s[15].transitions = {'CLASS': 16}
        s[16].transitions = {'DEL_COMMA': 17}
        s[17].transitions = {'CLASS': 18}
        s[18].transitions = {'DEL_RP': 7, 'DEL_COMMA': 17}
        for item in self.states.values():
            item.states = s

        state = self.states[2]  # Initial
        final = self.states[10]
        while state != final:
            state = state.make_transition(self.tokens[self.pointer])
            self.pointer += 1

        params = [(self.pnames[i], self.ptypes[i]) for i in range(len(self.pnames))]
        return Function(self.fname, params, self.rtypes, None), self.pointer


if __name__ == "__main__":
    pass
