from string import punctuation

with open("text.txt") as file, open("output.txt", "w") as output:
    lines = file.readlines()
    result = []
    for row, line in enumerate(lines):
        line = line.strip()
        length_of_line = len(line.replace(" ", ""))
        counter_of_punct = 0
        for element in line:
            if element in punctuation:
                counter_of_punct += 1
        result.append(f"Line {row +1}: {line} ({length_of_line - counter_of_punct})({counter_of_punct})")
    output.write('\n'.join(result))
