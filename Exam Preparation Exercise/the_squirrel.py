rows = int(input())
commands = input().split(", ")
matrix = []
squirrel_row = 0
squirrel_col = 0
hazelnuts = 0
is_game_over = False

for row in range(rows):
    matrix.append(list(input()))
    for column in range(rows):
        if matrix[row][column] == "s":
            squirrel_row = row
            squirrel_col = column

for command in commands:
    matrix[squirrel_row][squirrel_col] = "*"

    if command == "up":
        squirrel_row -= 1
    elif command == "down":
        squirrel_row += 1
    elif command == "left":
        squirrel_col -= 1
    elif command == "right":
        squirrel_col += 1

    if not (0 <= squirrel_row < rows and 0 <= squirrel_col < rows):
        print("The squirrel is out of the field.")
        is_game_over = True
        break

    if matrix[squirrel_row][squirrel_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        is_game_over = True
        break

    if matrix[squirrel_row][squirrel_col] == "h":
        hazelnuts += 1
        if hazelnuts == 3:
            is_game_over = True
            print("Good job! You have collected all hazelnuts!")
            break

if hazelnuts < 3 and not is_game_over:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")