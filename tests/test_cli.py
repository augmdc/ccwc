import unittest
from unittest.mock import patch, mock_open
import sys
from io import StringIO
import os

# Require the following in order to import package properly and avoid circular imports
ccwc_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ccwc")
sys.path.append(ccwc_path)

from src.ccwc.cli import main

class TestCCWCCli(unittest.TestCase):
    
    @patch('sys.argv', ['ccwc', '-c', 'testfile.txt'])
    @patch('builtins.open', new_callable=mock_open, read_data='test data')
    def test_byte_count(self, mock_file):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            self.assertIn('9', fake_output.getvalue())

    @patch('sys.argv', ['ccwc', '-l', 'testfile.txt'])
    @patch('builtins.open', new_callable=mock_open, read_data='line 1\nline 2\n')
    def test_line_count(self, mock_file):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            self.assertIn('2', fake_output.getvalue())

    # Additional tests for word count, character count, combinations of flags, no flags, non-existent file, etc.

if __name__ == '__main__':
    unittest.main()