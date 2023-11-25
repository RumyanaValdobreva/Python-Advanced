def is_outside(row, column, rows, matrix):
    return 0 > row or row >= rows or column < 0 or column >= len(matrix[row])


rows = int(input())
matrix = [[int(x) for x in input().split()] for row in range(rows)]

while True:
    command = input()
    if command == "END":
        break

    command = command.split()
    row, column, number = [int(x) for x in command[1:]]

    if is_outside(row, column, rows, matrix):
        print("Invalid coordinates")
        continue
    if "Add" in command:
        matrix[row][column] += number
    elif "Subtract" in command:
        matrix[row][column] -= number

for row in matrix:
    print(*row, sep=" ")