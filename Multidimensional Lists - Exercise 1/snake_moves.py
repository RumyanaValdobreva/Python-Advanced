rows, columns = [int(x) for x in input().split()]
initial_string = input()
string = initial_string
matrix = [["" for col in range(columns)] for row in range(rows)]


for row in range(rows):
    if row % 2 == 0:
        for column in range(columns):
            matrix[row][column] = string[0]
            string = string[1:]
            if string == "":
                string = initial_string
    elif row % 2 == 1:
        for column in range(columns - 1, -1, -1):
            matrix[row][column] = string[0]
            string = string[1:]
            if string == "":
                string = initial_string

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        print(matrix[r][c], end="")
    print()