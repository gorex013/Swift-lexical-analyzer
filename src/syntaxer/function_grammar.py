import re
import sys

# sys.path.insert(0, sys.path[0]+'/Swift-lexical-analyzer/syntaxer')

from src.lexer.LexicalAnalyzer import lexer
from src.syntaxer.function_parser import *


class FunctionDeclarationGrammar:
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
        return FunctionDefinition(self.fname, params, self.rtypes, None), self.pointer


class FunctionCallGrammar:
    def __init__(self, tokens: list, pointer: int, initial_state=1, fname=''):
        self.tokens = tokens
        self.pointer = pointer
        self.callee_name = ''
        self.args = []
        self.initial_state = initial_state

    class State:
        def __init__(self, name, final=False, action=None):
            self.transitions = {}
            self.final = final
            self.name = name
            self.action = action
            self.states = {}
            self.opt_name = None

        def make_transition(self, token, stack: list):
            # if self.transitions.get(token, None) is None:
            #     raise FunctionParseException("Incorrect order of tokens {}".format(token))
            if self.action is not None:
                result = self.action(token, self)  # Действие должно быть завязано на объект Функция
                if result is not None:
                    token = result
            if type(token) is dict and token.get('identifier', None) is not None:
                token = 'ID'  # Обработка случая, когда у меня {'identifier': 'sdfs'} приходит, а хотелос бы 'ID'
            if type(token) is dict and (FunctionCallGrammar.is_string(token) or FunctionCallGrammar.is_number(token)):
                token = 'CONST'

            if (self.name == 3 or self.name == 6 or self.name == 8) and token in 'DEL_RP':
                popped = stack.pop() + stack.pop()
            else:
                popped = stack.pop()

            # popped = popped[::-1]

            index, push = self.transitions[(token, popped)]
            stack += list(push)
            return self.states[index]

    def save_arg(self, token, state_obj):
        if type(token) is dict and (FunctionCallGrammar.is_string(token) or FunctionCallGrammar.is_number(token)):
            token = self.preprocess_literal(token)
        self.args.append(token)

    def is_string(token):
        is_inline = token.get('INLINE_STRING_LITERAL', None) is not None
        is_multiline = token.get('MULTILINE_STRING_LITERAL', None) is not None
        return is_inline or is_multiline

    def is_number(token):
        integer = token.get('decimal_integer', None) is not None
        binary = token.get('binary_integer', None) is not None
        floatt = token.get('decimal_double', None) is not None
        double = token.get('decimal_double', None) is not None
        hexad = token.get('octal_integer', None) is not None
        return integer or binary or floatt or double or hexad

    def preprocess_literal(self, token, state_obj):
        is_str = FunctionCallGrammar.is_string(token)
        is_num = FunctionCallGrammar.is_number(token)
        if is_str:
            inline = token.get('INLINE_STRING_LITERAL', None)
            multiline = token.get('MULTILINE_STRING_LITERAL', None)
            return inline or multiline
        if is_num:
            integer = token.get('decimal_integer', None)
            binary = token.get('binary_integer', None)
            floatt = token.get('decimal_double', None)
            double = token.get('decimal_double', None)
            hexad = token.get('octal_integer', None)
            return integer or binary or floatt or double or hexad

            return value
        raise Exception("How did you come here?")

    def complex_action(self, token, state_obj):
        if token is dict:  # to 9
            return self.save_complex_arg(token)
        if 'DEL_LP' in token:  # to 10
            fcall, pointer = parse_function_call(self.tokens, self.pointer - 1, state_obj.opt_name)
            self.pointer = pointer
            self.args.append(fcall)
            return tokens[self.pointer]

    def save_complex_arg(self, token, state_obj):
        pass #TODO me, store somehow name and value

    def save_name(self, name, state_obj):
        state_obj.opt_name = name['identifier']
        self.callee_name = name['identifier']


def parse_function_call(tokens, pointer, initial=1, fname=None):
    stack = ['Z']
    fcall_grammar = FunctionCallGrammar(tokens, pointer)
    fcall_grammar.states = {}
    for i in range(11):
        fcall_grammar.states[i] = fcall_grammar.State(name=i)
    fcall_grammar.states[3].action = fcall_grammar.save_arg
    fcall_grammar.states[8].action = fcall_grammar.complex_action
    fcall_grammar.states[7].action = fcall_grammar.save_arg
    fcall_grammar.states[1].action = fcall_grammar.save_name

    s = fcall_grammar.states
    s[4].final = True
    s[1].transitions = {('ID', 'Z'): (2, 'Z')}
    s[2].transitions = {('DEL_LP', 'Z'): (3, 'ZA')}
    s[3].transitions = {('DEL_RP', 'AZ'): (4, 'Z'), ('CONST', 'A'): (6, 'A'), ('ID', 'A'): (8, 'A')}
    s[6].transitions = {('DEL_COMMA', 'A'): (7, 'A'), ('DEL_RP', 'AZ'): (4, 'Z')}
    s[7].transitions = {('CONST', 'A'): (6, 'A'), ('ID', 'A'): (8, 'A')}
    s[8].transitions = {('DEL_COMMA', 'A'): (7, 'A'), ('DEL_COLON', 'A'): (9, 'A'), ('LP', 'A'): (10, 'A'), ('DEL_RP', 'AZ'): (4, 'Z')}
    s[9].transitions = {('ID', 'A'): (8, 'A'), ('CONST', 'A'): (6, 'A')}
    s[10].transitions = {('DEL_RP', 'A'): (8, 'A')}

    for item in s.values():
        item.states = s

    state = fcall_grammar.states[fcall_grammar.initial_state]
    while state.final is not True:
        state = state.make_transition(tokens[fcall_grammar.pointer], stack)
        fcall_grammar.pointer += 1

    if fname is not None:
        name = fname
    else:
        name = fcall_grammar.callee_name

    f_call = FunctionCall(name, fcall_grammar.args)
    return f_call, fcall_grammar.pointer


if __name__ == "__main__":
    with open('f_cal.txt') as f:
        content = f.read()
    tokens = lexer(content)
    f_call, pointer = parse_function_call(tokens=tokens, pointer=0)
    print(f_call.dict_representation())