import unittest
from reverse_string import execute


class TestReverseString(unittest.TestCase):
    def test_handles_empty_string(self):
        self.assertEqual(execute(''), '')

    def test_reverses_single_word(self):
        self.assertEqual(execute('robot'), 'tobor')

    def test_reverses_capitalized_word(self):
        self.assertEqual(execute('Ramen'), 'nemaR')

    def test_reverses_sentence_with_punctuation(self):
        self.assertEqual(execute('I am hungry!'), '!yrgnuh ma I')

    def test_reverses_palindrome(self):
        self.assertEqual(execute('racecar'), 'racecar')

    def test_reverses_even_sized_word(self):
        self.assertEqual(execute('drawer'), 'reward')


if __name__ == '__main__':
    unittest.main()
