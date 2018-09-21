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






if __name__ == '__main__':
	unittest.main()