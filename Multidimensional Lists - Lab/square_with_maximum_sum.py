rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for row in range(rows):
    elements = [int(x) for x in input().split(', ')]
    matrix.append(elements)

max_sum = float('-inf')
sub_matrix = []

for row_index in range(rows-1):
    for column_index in range(columns-1):
        current_element = matrix[row_index][column_index]
        next_element = matrix[row_index][column_index+1]
        element_below = matrix[row_index+1][column_index]
        diagonal_element = matrix[row_index+1][column_index+1]

        sum_of_elements = current_element + next_element + element_below + diagonal_element
        if max_sum < sum_of_elements:
            max_sum = sum_of_elements
            sub_matrix = [[current_element, next_element], [element_below, diagonal_element]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)