#!/usr/bin/env python3
import argparse
from pathlib import Path
import sys

parser = argparse.ArgumentParser(
    description="Counts the number of bytes, characters or words"
)

parser.add_argument("-b", "--byte", action="store_true")
parser.add_argument("path", help='The path of the file to process, either absolute or relative')

args = parser.parse_args()

print(args)
#sys.exit(0)

file_path = Path(args.path)

if not file_path.exists():
    print("Error: The target directory doesn't exist")
    raise SystemExit(1)

#Step 1: Output the number of bytes
with open(file_path, 'rb') as file:
    content = file.read()

# Count the number of bytes
byte_count = len(content)

print(byte_count)
