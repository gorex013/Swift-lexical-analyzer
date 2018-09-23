import sys
sys.path.insert(0, sys.path[0]+'/Swift-lexical-analyzer')
sys.path.append('../src/')

import unittest
from LexicalAnalyzer import *
import preprocessing.string_literals as str_lit
import preprocessing.comments as com

from src.LexicalAnalyzer import *
from src.swift_tokens import *


class IdentifyComments(unittest.TestCase):
    def test_single_comment(self):
        initial = 'var a = 15 //igor nigor'
        expected = 'var a = 15'

        processed = com.format_inline_comment(initial)
        processed = processed.strip()

        self.assertEqual(expected, processed)

    def test_multi_comment(self):
        initial = '''Kevin likes bicycle /*\nBut his daughter likes dogs val p = 16\n*/var x = 20'''
        expected = '''Kevin likes bicycle var x = 20'''

        processed = com.format_multiline_comment(initial)
        processed = processed.strip()

        self.assertEqual(expected, processed)

    def test_complex_comments(self):
        initial = '''var bruce = "John Doe" // Lil Wayne is not satisfied\nval chuck = 'Norris' /* And there is some magic -> content\n*/ print('doc')\n//test'''

        expected = '''var bruce = "John Doe" val chuck = 'Norris'  print('doc')'''

        processed = com.format_inline_comment(initial)
        processed = com.format_multiline_comment(processed)
        processed = processed.strip()

        self.assertEqual(expected, processed)


def reinitialize_storage():
    str_lit.storage = {}  # Reinitialize storage
    str_lit.temp_id = 0


class StringLiterals(unittest.TestCase):
    def test_inline(self):
        reinitialize_storage()

        initial = 'print("Doctor \(dc_name), I don`t feel legs!")'
        expected = 'print(TEMP0)'
        expected_literal = {string_literals['inline']: '"Doctor \(dc_name), I don`t feel legs!"'}
        formatted = str_lit.format_inline_strings(initial)

        self.assertEqual(expected, formatted)
        self.assertEqual(str_lit.retrieve('TEMP0'), expected_literal)

    def test_multiline(self):
        reinitialize_storage()

        initial = 'initial dog is """KKK clan"""'
        expected = 'initial dog is TEMP0'
        expected_literal = {string_literals['multiline']: '"""KKK clan"""'}
        formatted = str_lit.format_multiline_strings(initial)

        self.assertEqual(expected, formatted)
        self.assertEqual(str_lit.retrieve('TEMP0'), expected_literal)

    def test_complex(self):
        reinitialize_storage()

        with open('swift_examples/complex_string_literals.swift') as f:
            content = f.read()
        expected = 'var a = TEMP0\nlet b = TEMP1'
        expected_literals = [{string_literals['multiline']: '"""KKK clan"""'},
                             {string_literals['inline']: '"Doctor who?"'}]

        formatted = str_lit.format_strings(content)
        actual_literals = [str_lit.retrieve('TEMP0'), str_lit.retrieve('TEMP1')]

        self.assertEqual(expected, formatted)
        self.assertEqual(expected_literals, actual_literals)



class FormatTest(unittest.TestCase):

    def test_simple(self):
        initial = 'var a = 15->Int'
        tokens = process(initial)
        expected = ['D_VAR', {'identifier': 'a'}, 'DEL_EQUAL', {'decimal_integer': '15'}, 'DEL_ARROW', 'class_INT']
        self.assertEqual(expected, tokens)

    def test_is_special(self):
        words = ['val', 'var', '->', 'Int', 'integer', '"let"', '//', '<=']
        expected = [False, True, True, True, False, False, False, True]
        answers = [is_special(w) for w in words]

        self.assertEqual(expected, answers)

    def test_is_processed(self):
        words = ['DEL_EQUAL', 'a', '_', 'DEL_ARROW', 'class_INT', 'operator',
                 'mutating']  # TODO: CAN ALTER IF NAMINGS CHANGE
        expected = [True, False, False, True, True, False, False]
        answers = [is_processed(w) for w in words]

        self.assertEqual(expected, answers)


if __name__ == '__main__':
    unittest.main()
