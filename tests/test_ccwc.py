import pytest
import tempfile
from argparse import Namespace
import os
from io import StringIO
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(project_root, 'src')
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
from ccwc import ccwc

@pytest.mark.parametrize("namespace, content, expected_result", [
    (Namespace(byte=True, line=False, word=False, character=False, path=None), b"Test content", [12]),
    (Namespace(byte=False, line=True, word=False, character=False), "Line 1\nLine 2\nLine 3", [3]),
    (Namespace(byte=False, line=False, word=True, character=False), "One two three\nFour five\nSix", [6]),
    (Namespace(byte=False, line=False, word=False, character=True), "12345\n67890", [11]),
    (Namespace(byte=True, line=True, word=True, character=False), "12345\n67890", [11, 2, 2])
])

def test_ccwc_file_input(namespace, content, expected_result):
    # Correctly handle writing bytes or strings
    mode = 'w+b' if isinstance(content, bytes) else 'w+'
    with tempfile.NamedTemporaryFile(mode=mode, delete=False) as temp_file:
        temp_file.write(content)
        temp_file.flush()  # Ensure all data is written to the file
        temp_file.seek(0)  # Reset file pointer to the beginning

    # Pass the file path to ccwc function
    result = ccwc(namespace, temp_file.name)
    
    # Cleanup: remove the temporary file
    os.remove(temp_file.name)
    
    # Assertion
    assert result == expected_result

def test_ccwc_stdin_input():
    namespace = Namespace(byte=False, line=False, word=False, character=True, path=None)
    original_stdin = sys.stdin

    # Simulate stdin using StringIO
    simulated_stdin = StringIO("This is piped data\nWith two lines")
    sys.stdin = simulated_stdin

    # Call ccwc with simulated stdin
    result = ccwc(namespace, sys.stdin)

    # Restore original stdin and close the simulated one
    sys.stdin = original_stdin
    simulated_stdin.close()

    # Assertion
    assert result == [33]
