sum_of_matrix = int(input())
matrix = []

for row in range(sum_of_matrix):
    elements = list(input())
    matrix.append(elements)

element = input()
is_found = False

for rows in range(sum_of_matrix):
    if is_found:
        break
    for column in range(len(matrix[rows])):
        current_element = matrix[rows][column]
        if current_element == element:
            is_found = (rows, column)

if not is_found:
    print(f"{element} does not occur in the matrix")
else:
    print(is_found)