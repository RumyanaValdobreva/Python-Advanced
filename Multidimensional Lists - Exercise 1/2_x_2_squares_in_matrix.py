identical_chars = 0
rows, columns = list(map(int, input().split()))

matrix = [[x for x in input().split()] for row in range(rows)]

for row in range(rows - 1):
    for column in range(columns - 1):
        first_char = matrix[row][column]
        second_char = matrix[row][column + 1]
        third_char = matrix[row + 1][column]
        fourth_char = matrix[row + 1][column + 1]
        if fourth_char == third_char == second_char == first_char:
            identical_chars += 1

print(identical_chars)