def ccwc(namespace, file_path):
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
    if namespace.character and not sum([namespace.byte, namespace.line, namespace.word]) == 3:
        with open(file_path, 'r') as file:
            output.append(sum(len(line) for line in file))

    return output