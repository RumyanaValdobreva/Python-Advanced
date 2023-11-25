with open("text.txt") as file:
    for row, line in enumerate(file.readlines()):
        if row % 2 == 0:
            for element in ["-", ",", ".", "!", "?"]:
                line = line.replace(element, "@")
            print(' '.join(reversed(line.split())))