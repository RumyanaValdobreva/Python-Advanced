rows, columns = list(map(int, input().split()))
matrix = [[int(x) for x in input().split()] for row in range(rows)]

max_sum = float('-inf')
matrix_to_print = []

for row in range(rows - 2):
    for column in range(columns - 2):
        char_1 = matrix[row][column]
        char_2 = matrix[row][column + 1]
        char_3 = matrix[row][column + 2]
        char_4 = matrix[row + 1][column]
        char_5 = matrix[row + 1][column + 1]
        char_6 = matrix[row + 1][column + 2]
        char_7 = matrix[row + 2][column]
        char_8 = matrix[row + 2][column + 1]
        char_9 = matrix[row + 2][column + 2]
        sum_of_chars = char_9 + char_8 + char_7 + char_6 + char_5 + char_4 + char_3 + char_2 + char_1
        if sum_of_chars > max_sum:
            max_sum = sum_of_chars
            matrix_to_print = [[char_1, char_2, char_3], [char_4, char_5, char_6], [char_7, char_8, char_9]]

print(f"Sum = {max_sum}")

for i in range(len(matrix_to_print)):
    print(*matrix_to_print[i], sep=" ")