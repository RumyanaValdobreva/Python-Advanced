def is_inside(row, column, size):
    return 0 <= row < size and 0 <= column < size


presents = int(input())
size = int(input())

current_row = 0
current_column = 0
initial_nice_kids = 0
neighborhood = []
directions = {"left": lambda r, c: (r, c - 1),
              "right": lambda r, c: (r, c + 1),
              "up": lambda r, c: (r - 1, c),
              "down": lambda r, c: (r + 1, c)}

for row in range(size):
    line = input().split()
    for column in range(size):
        if line[column] == "S":
            current_row = row
            current_column = column
        elif line[column] == "V":
            initial_nice_kids += 1
    neighborhood.append(line)

nice_kids = initial_nice_kids
neighborhood[current_row][current_column] = "-"

while presents:
    command = input()
    if command == "Christmas morning":
        break

    next_row, next_column = directions[command](current_row, current_column)

    if not is_inside(next_row, next_column, size):
        continue
    current_row, current_column = next_row, next_column

    if neighborhood[next_row][next_column] == "V":
        presents -= 1
        nice_kids -= 1
    elif neighborhood[next_row][next_column] == "C":
        for direction in directions:
            row_, column_ = directions[direction](next_row, next_column)
            if neighborhood[row_][column_] == "X":
                presents -= 1
                neighborhood[row_][column_] = "-"
            if neighborhood[row_][column_] == "V":
                nice_kids -= 1
                presents -= 1
                neighborhood[row_][column_] = "-"
            if not presents:
                break
    neighborhood[next_row][next_column] = "-"

neighborhood[current_row][current_column] = "S"

if not presents and nice_kids:
    print("Santa ran out of presents!")

for line in neighborhood:
    print(*line, sep=" ")

if not nice_kids:
    print(f"Good job, Santa! {initial_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")