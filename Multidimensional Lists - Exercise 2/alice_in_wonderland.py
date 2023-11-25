size_of_matrix = int(input())
matrix = []

alice_row, alice_column = 0, 0
tea_bags = 10

for row in range(size_of_matrix):
    elements = input().split()
    matrix.append(elements)
    for column in range(size_of_matrix):
        if elements[column] == "A":
            alice_row, alice_column = row, column

direction = {'up': lambda r, c: (r - 1, c),
             'down': lambda r, c: (r + 1, c),
             'right': lambda r, c: (r, c + 1),
             'left': lambda r, c: (r, c - 1)}

while True:
    command = input()
    matrix[alice_row][alice_column] = "*"
    alice_row, alice_column = direction[command](alice_row, alice_column)

    if 0 <= alice_row < size_of_matrix and 0 <= alice_column < size_of_matrix:
        if matrix[alice_row][alice_column] == "R":
            matrix[alice_row][alice_column] = "*"
            print(f"Alice didn't make it to the tea party.")
            break
        elif matrix[alice_row][alice_column].isdigit():
            tea_bags -= int(matrix[alice_row][alice_column])
            matrix[alice_row][alice_column] = "*"
            if tea_bags <= 0:
                print(f"She did it! She went to the party.")
                break
    else:
        print(f"Alice didn't make it to the tea party.")
        break

for element in matrix:
    print(' '.join(str(x) for x in element))