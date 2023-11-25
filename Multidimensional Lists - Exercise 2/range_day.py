def get_next_position(row, column, direction, steps):
    if direction == "up":
        return row - steps, column
    elif direction == "down":
        return row + steps, column
    elif direction == "left":
        return row, column - steps
    elif direction == "right":
        return row, column + steps


def is_inside(row, column, size):
    return 0 <= row < size and 0 <= column < size


matrix = []
size = 5
targets = 0
player_row = 0
player_column = 0

for row in range(size):
    row_elements = input().split()
    for column in range(size):
        if row_elements[column] == "A":
            player_row = row
            player_column = column
        elif row_elements[column] == "x":
            targets += 1
    matrix.append(row_elements)

matrix[player_row][player_column] = "."
hit_targets = []

for line in range(int(input())):
    command_parts = input().split()
    command = command_parts[0]
    direction = command_parts[1]
    if command == "move":
        steps = int(command_parts[2])
        next_row, next_column = get_next_position(player_row, player_column, direction, steps)
        if is_inside(next_row, next_column, size) and matrix[next_row][next_column] == ".":
            player_row, player_column = next_row, next_column
    else:
        bullet_row, bullet_column = get_next_position(player_row, player_column, direction, 1)
        while is_inside(bullet_row, bullet_column, size):
            if matrix[bullet_row][bullet_column] == "x":
                targets -= 1
                matrix[bullet_row][bullet_column] = "."
                hit_targets.append([bullet_row, bullet_column])
                break
            else:
                bullet_row, bullet_column = get_next_position(bullet_row, bullet_column, direction, 1)
        if targets == 0:
            break

if targets == 0:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")
for target in hit_targets:
    print(target)