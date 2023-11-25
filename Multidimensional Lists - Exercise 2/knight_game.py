def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def find_attacks(size, row, column):
    possible_attacks = [[row - 2, column - 1],
                        [row - 1, column - 2],
                        [row + 1, column - 2],
                        [row + 2, column - 1],
                        [row - 2, column + 1],
                        [row - 1, column + 2],
                        [row + 1, column + 2],
                        [row + 2, column + 1]]

    result = []
    for attack in possible_attacks:
        row, column = attack[0], attack[1]
        if not is_outside(row, column, size):
            result.append(attack)
    return result


size_of_matrix = int(input())
field = [list(input()) for row in range(size_of_matrix)]

knights_to_remove = 0
knights_attacks = {}

for row in range(size_of_matrix):
    for col in range(len(field[row])):
        if field[row][col] == "K":
            knights_attacks[(row, col)] = []

for knight in knights_attacks:
    knight_row, knight_col = knight[0], knight[1]
    attacks = find_attacks(size_of_matrix, knight_row, knight_col)
    for attack in attacks:
        row, col = attack[0], attack[1]
        if field[row][col] == "K":
            knights_attacks[knight].append((row, col))

knights_attacks = dict(sorted(knights_attacks.items(), key=lambda x: (-len(x[1]), x[0])))

while knights_attacks:
    knight = list(knights_attacks.keys())[0]
    kills = list(knights_attacks.values())[0]

    if len(kills) > 0:
        knights_to_remove += 1

    for victim in kills:
        knights_attacks[victim].remove(knight)

    del knights_attacks[knight]
    knights_attacks = dict(sorted(knights_attacks.items(), key=lambda x: (-len(x[1]), x[0])))

print(knights_to_remove)