import unittest

from src.syntaxer.grammars import *
from src.syntaxer.syntaxer import transform_funcs, transform_main

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

    def test_complex_subcalls(self):
        with open('swift_examples/f_cal.txt') as f:
            content = f.read()
        tokens = lexer(content)
        f_call, pointer = parse_function_call(tokens=tokens, pointer=0)
        print(f_call.dict_representation())

        self.assertEqual(f_call.name, 'print')
        self.assertEqual(type(f_call), type(f_call.args[0]))
        self.assertEqual(len(f_call.args), 3)
        f2 = f_call.args[0]
        self.assertEqual(f2.name, 'call')
        self.assertListEqual(f2.args, ['"cat"'])


class SyntaxerTests(unittest.TestCase):
    def test_fdefs(self):
        with open('swift_examples/test_funcs.txt') as f:
            content = f.read()
        tokens = lexer(content)
        results = transform_funcs(tokens)
        print(results)

        self.assertEquals(type(results[0]), FunctionDefinition)
        self.assertEquals(type(results[1]), FunctionDefinition)
        self.assertEquals(type(results[2]), FunctionDefinition)

    def test_funcs_calls_vars(self):
        with open('swift_examples/test_funcs2.txt') as f:
            content = f.read()
        tokens = lexer(content)
        results = transform_main(tokens)
        print(results)

        self.assertEquals(type(results[0]), FunctionDefinition)
        self.assertEquals(type(results[1]), FunctionDefinition)
        self.assertEquals(type(results[2]), FunctionDefinition)
        self.assertEquals(type(results[3]), VariableDefinition)
        self.assertEquals(type(results[4]), VariableDefinition)
        self.assertEquals(type(results[5]), FunctionCall)
        self.assertEquals(type(results[5].args[1]), FunctionCall)
        self.assertEquals(type(results[0].fbody[0]), FunctionCall)
        self.assertEquals(type(results[0].fbody[1]), VariableDefinition)

