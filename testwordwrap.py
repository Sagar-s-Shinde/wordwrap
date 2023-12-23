import unittest
import wordwrap


class MyTestCase(unittest.TestCase):
    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            wordwrap.word_wrap(12, 20)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            wordwrap.word_wrap("Sample text", 0)


if __name__ == '__main__':
    unittest.main()
