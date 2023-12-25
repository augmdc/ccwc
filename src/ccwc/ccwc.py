import sys
import locale

def ccwc(namespace, file_path):
    output = []

    # Function to open the file only if it's not stdin
    def open_file(file_path, mode):
        if file_path is sys.stdin:
            return sys.stdin
        else:
            return open(file_path, mode)

    if namespace.byte:
        with open_file(file_path, 'rb') as file:
            output.append(len(file.read()))

    if namespace.line:
        with open_file(file_path, 'r') as file:
            output.append(sum(1 for line in file))

    if namespace.word:
        with open_file(file_path, 'r') as file:
            output.append(sum(len(line.split()) for line in file))

    # Exclude this one if default
    if namespace.character and not sum([namespace.byte, namespace.line, namespace.word]) == 3:
    # Check if input is sys.stdin
        if file_path is sys.stdin:
            # Count characters directly from sys.stdin
            output.append(len(sys.stdin.read()))
        else:
            # Handle as a regular file
            file_encoding = locale.getpreferredencoding()
            with open_file(file_path, 'rb') as file:
                output.append(len(file.read().decode(file_encoding)))

    return output

