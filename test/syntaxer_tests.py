import unittest

from src.syntaxer.function_grammar import *

sys.path.insert(0, sys.path[0]+'/Swift-lexical-analyzer')
sys.path.append('../src/')


class FunctionDeclarationTest(unittest.TestCase):
    def test_simple_function_declaration(self):
        expected_foo = FunctionDefinition(name='greet', params=[('person', 'String')], rparams=['String'], fbody=None)

        with open('swift_examples/syntaxer_function_simple.txt') as f:
            content = f.read()
        tokens = lexer(content)
        pointer = 1  # because assume  we found `func` and now know that we have to parse other stuff
        fgrammar = FunctionDeclarationGrammar(tokens, pointer)
        foo, pointer = fgrammar.process_func()
        print(foo)

        self.assertListEqual(expected_foo.params, foo.params)
        self.assertListEqual(expected_foo.return_params, foo.return_params)
        self.assertEqual(expected_foo.fbody, foo.fbody)
        self.assertEqual(expected_foo.name, foo.name)


class FunctionCallTest(unittest.TestCase):
    def test_simple_fcall(self):
        with open('swift_examples/syntaxer_fcall_simple.txt') as f:
            content = f.read()
        tokens = lexer(content)
        pointer = 0
        f_call, pointer = parse_function_call(tokens, pointer)
        self.assertEqual(f_call.name, 'print')
        self.assertEqual(len(f_call.args), 1)
        self.assertListEqual(f_call.args, ['"str"'])