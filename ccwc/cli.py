"""
The command-line interface for the ccwc
"""
import argparse
from pathlib import Path
from .ccwc import ccwc

def main():
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

    final_output = ccwc(args, file_path)
    str_output = " ".join(map(str, final_output))

    print(f"{str_output} {file_path.name}")

if __name__ == "__main__":
    main()