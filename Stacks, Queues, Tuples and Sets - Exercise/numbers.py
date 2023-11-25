first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    command_ = command[0] + " " + command[1]
    numbers = [int(x) for x in command[2:]]

    if command_ == "Add First":
        first_sequence.update(numbers)
    if command_ == "Add Second":
        second_sequence.update(numbers)
    if command_ == "Remove First":
        first_sequence.difference_update(numbers)
    if command_ == "Remove Second":
        second_sequence.difference_update(numbers)
    if command_ == "Check Subset":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))


print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
