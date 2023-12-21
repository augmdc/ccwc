"""
The command-line interface for the ccwc
"""

import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    description="Counts the number of bytes, characters, lines or words in a file.",
    prog="ccwc"
)