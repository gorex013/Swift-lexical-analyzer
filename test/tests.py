import unittest
from .Identifier.parser import parse

class identifyComments(unittest.TestCase):

	def test_single_comment(self):
		initial = 'var a = 15 //igor nigor'
		expected = 'var a = 15'

		processed = get_rid_of_single(initial)
		processed = processed.trim()

		self.assertEqual(initial, expected)

	def test_multi_comment(self):
		initial = '''Kevin likes bicycle /*
		But his daughter likes dogs val p = 16
		*/var x = 20
		'''
		expected = '''Kevin likes bicycle var x = 20'''

		processed = get_rid_of_multi(initial)
		processed = processed.trim()

		self.assertEqual(expected, processed)

	def test_complex_comments(self):
		initial = '''
			var bruce = "John Doe" // Lil Wayne is not satisfied
			val chuck = 'Norris' /* And there is some magic -> content
			*/ print('doc')
			//test
		'''

		expected = '''
		var bruce = "John Doe" val chuck = 'Norris' print('doc')'''

		processed = get_rid_of_single(initial)
		processed = get_rid_of_multi(processed)
		processed = processed.trim()

		self.assertEqual(expected, processed)






if __name__ == '__main__':
	unittest.main()