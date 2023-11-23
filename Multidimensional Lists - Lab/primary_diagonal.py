size_of_matrix = int(input())
matrix = []

for row in range(size_of_matrix):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

diagonal = 0

for rows in range(size_of_matrix):
    diagonal += matrix[rows][rows]

print(diagonal)