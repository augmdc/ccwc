import unittest
import tempfile
from argparse import Namespace
import sys
import os
from io import StringIO

# Add the src directory to sys.path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(project_dir, 'src')
sys.path.insert(0, src_dir)

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
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
            temp_file.write("Line 1\nLine 2\nLine 3")

        file_path = temp_file.name
        result = ccwc(namespace, file_path)
        os.remove(file_path)
        self.assertEqual(result, [3])

    def test_word_count(self):
        namespace = Namespace(byte=False, line=False, word=True, character=False)
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
            temp_file.write("One two three\nFour five\nSix")

        file_path = temp_file.name
        result = ccwc(namespace, file_path)
        os.remove(file_path)
        self.assertEqual(result, [6])
    
    def test_character_count(self):
        namespace = Namespace(byte=False, line=False, word=False, character=True)
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
            temp_file.write("12345\n67890")

        file_path = temp_file.name
        result = ccwc(namespace, file_path)
        os.remove(file_path)
        self.assertEqual(result, [11])

    def test_default_count(self):
        namespace = Namespace(byte=True, line=True, word=True, character=False)
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
            temp_file.write("12345\n67890")

        file_path = temp_file.name
        result = ccwc(namespace, file_path)
        os.remove(file_path)
        self.assertEqual(result, [11, 2, 2])

    def test_piped_data_character_option(self):
        namespace = Namespace(byte=False, line=False, word=False, character=True)
        original_stdin = sys.stdin

        # Use StringIO to simulate stdin
        simulated_stdin = StringIO("This is piped data\nWith two lines")
        sys.stdin = simulated_stdin

        result = ccwc(namespace, sys.stdin)

        # Restore the original stdin
        sys.stdin = original_stdin
        simulated_stdin.close()

        self.assertEqual(result, [33])

if __name__ == '__main__':
    unittest.main()
