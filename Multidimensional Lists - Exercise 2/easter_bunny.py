size_of_matrix = int(input())
matrix = []

bunny_row = 0
bunny_column = 0
best_sum = float('-inf')
best_direction = ""
best_path = []


for row in range(size_of_matrix):
    row_elements = input().split()
    for column in range(size_of_matrix):
        if row_elements[column] == "B":
            bunny_row = row
            bunny_column = column
    matrix.append(row_elements)

directions = {"right": lambda r, c: (r, c + 1),
              "left": lambda r, c: (r, c - 1),
              "up": lambda r, c: (r - 1, c),
              "down": lambda r, c: (r + 1, c)}

for direction in directions:
    current_sum = 0
    row, column = directions[direction](bunny_row, bunny_column)
    current_path = []
    while 0 <= row < size_of_matrix and 0 <= column < size_of_matrix and matrix[row][column] != "X":
        current_sum += int(matrix[row][column])
        current_path.append([row, column])
        row, column = directions[direction](row, column)
    if current_sum > best_sum and current_path:
        best_sum = current_sum
        best_direction = direction
        best_path = current_path

print(best_direction)
print(*best_path, sep="\n")
print(best_sum)