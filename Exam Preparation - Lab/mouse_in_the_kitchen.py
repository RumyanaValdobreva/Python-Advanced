rows, columns = [int(x) for x in input().split(',')]
matrix = []
mouse_row, mouse_col = None, None
cheese_count = 0
command = ""

for r in range(rows):
    row = list(input())
    matrix.append(row)
    if "M" in row:
        mouse_row = r
        mouse_col = row.index("M")
    if "C" in row:
        cheese_count += row.count("C")

while cheese_count != 0:

    command = input()

    if command == "danger":
        break
    next_row, next_col = None, None

    if command == "up" and 0 <= mouse_row - 1 < rows:
        next_row, next_col = mouse_row - 1, mouse_col
    elif command == "down" and 0 <= mouse_row + 1 < rows:
        next_row, next_col = mouse_row + 1, mouse_col
    elif command == "left" and 0 <= mouse_col - 1 < columns:
        next_row, next_col = mouse_row, mouse_col - 1
    elif command == "right" and 0 <= mouse_col + 1 < columns:
        next_row, next_col = mouse_row, mouse_col + 1

    if next_row is None or next_col is None:
        print("No more cheese for tonight!")
        break

    if matrix[next_row][next_col] == "@":
        continue

    if matrix[next_row][next_col] == "T":
        matrix[mouse_row][mouse_col] = "*"
        mouse_row, mouse_col = next_row, next_col
        matrix[mouse_row][mouse_col] = "M"
        print("Mouse is trapped!")
        break

    if matrix[next_row][next_col] == "*":
        matrix[mouse_row][mouse_col] = "*"
        mouse_row, mouse_col = next_row, next_col
        matrix[mouse_row][mouse_col] = "M"
        continue

    if matrix[next_row][next_col] == "C":
        cheese_count -= 1
        matrix[mouse_row][mouse_col] = "*"
        mouse_row, mouse_col = next_row, next_col
        matrix[mouse_row][mouse_col] = "M"
else:
    print("Happy mouse! All the cheese is eaten, good night!")

if cheese_count and command == "danger":
    print("Mouse will come back later!")

for row in matrix:
    print("".join(row))