rows = int(input())
matrix = []

for row in range(rows):
    elements = [int(x) for x in input().split(', ')]
    matrix.append(elements)

flattened = []

# flattened = [num for sublist in matrix for num in sublist]
# print(flattened)

for row in range(rows):
    for column in range(len(matrix[row])):
        flattened.append(matrix[row][column])

print(flattened)