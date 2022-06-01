import unittest
from anagrams.anagrams import my_function

cases = [("abcd efgh", "dcba hgfe"),
         ("a1bcd efg!h", "d1cba hgf!e"),
         ("", ""),
         ]


class TestSentence(unittest.TestCase):

    def test_reversed(self):
        for text, reversed_text in cases:
            self.assertEqual(my_function(text), reversed_text)

    def test_type(self):
        self.assertTrue(type(text) == int or float for text in cases)


if __name__ == '__main__':
    unittest.main()
