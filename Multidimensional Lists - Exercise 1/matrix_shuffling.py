rows, columns = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for row in range(rows)]

while True:
    command = input()
    if command == "END":
        break

    valid = True
    command = command.split()

    if not command[0] == "swap":
        print("Invalid input!")
        continue
    if not len(command) == 5:
        print("Invalid input!")
        continue
    for index, number in enumerate(command[1:]):
        number = int(number)
        if number < 0:
            print("Invalid input!")
            valid = False
            break
        if index % 2 == 0:
            if number > rows - 1:
                print("Invalid input!")
                valid = False
                break
        else:
            if number > columns - 1:
                print("Invalid input!")
                valid = False
                break
    if valid:
        matrix[int(command[1])][int(command[2])], matrix[int(command[3])][int(command[4])] = \
            matrix[int(command[3])][int(command[4])], matrix[int(command[1])][int(command[2])]
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                print(matrix[r][c], end=" ")
            print()
