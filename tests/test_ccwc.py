import unittest
import tempfile
from argparse import Namespace
import sys
import os
ccwc_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ccwc")
sys.path.append(ccwc_path)
from ccwc import ccwc

class TestCCWC(unittest.TestCase):
    def test_byte_count(self):
        namespace = Namespace(byte=True, line=False, word=False, character=False, path=None)

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b"Test content")

        file_path = temp_file.name
        result = ccwc(namespace, file_path)
        os.remove(file_path)
        self.assertEqual(result, [12])

    def test_line_count(self):
        namespace = Namespace(byte=False, line=True, word=False, character=False)
        file_path = "test_file.txt"

    def test_word_count(self):
        namespace = Namespace(byte=False, line=False, word=True, character=False)
        file_path = "test_file.txt"

    def test_character_count(self):
        namespace = Namespace(byte=False, line=False, word=False, character=True)
        file_path = "test_file.txt"

if __name__ == '__main__':
    unittest.main()
