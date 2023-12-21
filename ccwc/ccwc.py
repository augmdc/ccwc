#!/usr/bin/env python3
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    description="Counts the number of bytes, characters, lines or words in a file.",
    prog="ccwc"
)

parser.add_argument("-c", "--byte", action="store_true")
parser.add_argument("-l", "--line", action="store_true")
parser.add_argument("-w", "--word", action="store_true")
parser.add_argument("-m", "--character", action="store_true")
parser.add_argument("path", help='The path of the file to process')

args = parser.parse_args()
file_path = Path(args.path)

if not file_path.exists():
    parser.exit(1, message="The target directory does not exist")

if sum([args.byte, args.line, args.word, args.character]) >= 2:
    parser.exit(1, message="Combinations of flags is not allowed")

if not any([args.byte, args.line, args.word, args.character]):
        args.byte = args.line = args.word = args.character = True

def build_output(namespace):
    output = []

    if namespace.byte:
        with open(file_path, 'rb') as file:
            output.append(len(file.read()))

    if namespace.line:
        with open(file_path, 'r') as file:
            output.append(sum(1 for line in file))

    if namespace.word:
        with open(file_path, 'r') as file:
            output.append(sum(len(line.split()) for line in file))

    # Exclude this one if default
    if namespace.character and not sum([args.byte, args.line, args.word]) == 3:
        with open(file_path, 'r') as file:
            output.append(sum(len(line) for line in file))

    return output

final_output = build_output(args)
str_output = " ".join(map(str, final_output))

print(f"{str_output} {file_path.name}")