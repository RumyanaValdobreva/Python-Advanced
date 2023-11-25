size_of_matrix = int(input())

matrix = [[int(x) for x in input().split(", ")] for row in range(size_of_matrix)]
primary_diagonal = []
secondary_diagonal = []

for i in range(size_of_matrix):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][size_of_matrix - 1 - i])

print(f"Primary diagonal: {', '.join(list(map(str, primary_diagonal)))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(list(map(str, secondary_diagonal)))}. Sum: {sum(secondary_diagonal)}")