size_of_matrix = int(input())

matrix = [[int(x) for x in input().split()] for row in range(size_of_matrix)]
primary_diagonal = []
secondary_diagonal = []

for i in range(size_of_matrix):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][size_of_matrix - 1 - i])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))