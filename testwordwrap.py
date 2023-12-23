import unittest
import wordwrap


class TestWordWrap(unittest.TestCase):
    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            wordwrap.word_wrap(12, 20)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            wordwrap.word_wrap("Sample text", 0)

    def test_valid_input(self):
        para = "This is a sample paragraph for testing word_wrap function."
        width = 20
        result = wordwrap.word_wrap(para, width)

        expected_output = [
            'This   is  a  sample',
            'paragraph        for',
            'testing    word_wrap',
            'function.           '
        ]

        self.assertEqual(result, expected_output, "Output does not match expected result")

    def test_long_word_than_width(self):
        para = "Thisisasampleparagraph"
        width = 5
        result = wordwrap.word_wrap(para, width)

        self.assertEqual(result, None, "Expecting None for a word length longer than the specified width")


if __name__ == '__main__':
    unittest.main()
