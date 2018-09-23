import unittest
from src.LexicalAnalyzer import *

class IdentifyComments(unittest.TestCase):
	def test_single_comment(self):
		initial = 'var a = 15 //igor nigor'
		expected = 'var a = 15'

		processed = ps.format_inline_comment(initial)
		processed = processed.strip()

		self.assertEqual(expected, processed)

	def test_multi_comment(self):
		initial = '''Kevin likes bicycle /*\nBut his daughter likes dogs val p = 16\n*/var x = 20'''
		expected = '''Kevin likes bicycle var x = 20'''

		processed = ps.format_multiline_comment(initial)
		processed = processed.strip()

		self.assertEqual(expected, processed)

	def test_complex_comments(self):
		initial = '''var bruce = "John Doe" // Lil Wayne is not satisfied\nval chuck = 'Norris' /* And there is some magic -> content\n*/ print('doc')\n//test'''

		expected = '''var bruce = "John Doe" val chuck = 'Norris'  print('doc')'''

		processed = ps.format_inline_comment(initial)
		processed = ps.format_multiline_comment(processed)
		processed = processed.strip()

		self.assertEqual(expected, processed)

	def test_complex_comments2(self):
		initial = """  /**
   *  Moves the key at the specified `index` from `node` to
   *  the `targetNode` at `position`
   *
   *  - Parameters:
   *    - index: the index of the key to be moved in `node`
   *    - targetNode: the node to move the key into
   *    - node: the node to move the key from
   *    - position: the position of the from node relative to the targetNode
   */
  private func move(keyAtIndex index: Int, to targetNode: BTreeNode,
                                  from node: BTreeNode, at position: BTreeNodePosition) {
    switch position {"""
		processed = format(initial)
		print(processed)

class StringLiterals(unittest.TestCase):
	def test_inline(self):
		initial = 'print("Doctor \(dc_name), I don`t feel legs!")'
		expected =

class FormatTest(unittest.TestCase):
	def test_simple(self):
		initial = 'var a = 15->Int'
		tokens = format(initial)
		expected = ['D_VAR', {'identifier': 'a'}, 'DEL_EQUAL', 'NUMERICAL', 'DEL_ARROW', 'class_INT']
		self.assertEqual(expected, tokens)

	def test_is_special(self):
		words = ['val', 'var', '->', 'Int', 'integer', '"let"', '//', '<=']
		expected = [False, True, True, True, False, False, False, True]
		answers = [is_special(w) for w in words]

		self.assertEqual(expected, answers)

	def test_is_processed(self):
		words = ['DEL_EQUAL', 'a', '_', 'DEL_ARROW', 'class_INT', 'operator', 'mutating'] # TODO: CAN ALTER IF A CHANGE NAMINGS
		expected = [True, False, False, True, True, False, False]
		answers = [is_processed(w) for w in words]

		self.assertEqual(expected, answers)

	def test_swift_file(self):
		content = ''
		with open('BTree.swift') as f:
			content = f.read()
		tokens = format(content)
		with open('out.txt', 'w') as f:
			for token in tokens:
				f.write("{}\n".format(token))


if __name__ == '__main__':
	unittest.main()