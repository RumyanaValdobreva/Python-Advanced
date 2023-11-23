rows = int(input())
matrix = []

for row_index in range(rows):
    element = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    matrix.append(element)

print(matrix)

# even_matrix = []
#
# for row_index in range(rows):
#     even_matrix.append([])
#     for column_index in range(len(matrix[row_index])):
#         current_element = matrix[row_index][column_index]
#         if current_element % 2 == 0:
#             even_matrix[row_index].append(current_element)
#
# print(even_matrix)