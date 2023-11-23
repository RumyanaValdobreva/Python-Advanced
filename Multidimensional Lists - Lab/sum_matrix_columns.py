rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for row in range(rows):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

for column in range(columns):
    sum_column = 0
    for row in range(rows):
        sum_column += matrix[row][column]
    print(sum_column)

# rows_columns = [int(x) for x in input().split(', ')]
# rows = rows_columns[0]
# columns = rows_columns[1]
# matrix = []
#
# for row in range(rows):
#     elements = [int(x) for x in input().split()]
#     matrix.append(elements)
#
# for column in range(columns):
#     sum_column = 0
#     for row in range(rows):
#         sum_column += matrix[row][column]
#     print(sum_column)
