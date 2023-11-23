rows_columns = input().split(', ')
rows = int(rows_columns[0])
columns = int(rows_columns[1])
matrix = []
matrix_sum = 0

for _ in range(rows):
    elements = [int(x) for x in input().split(', ')]
    matrix_sum += sum(elements)
    matrix.append(elements)

# matrix_sum = 0
#
# # for row_index in range(rows):
# #     for column_index in range(columns):
# #         matrix_sum += matrix[row_index][column_index]
# #
print(matrix_sum)
print(matrix)