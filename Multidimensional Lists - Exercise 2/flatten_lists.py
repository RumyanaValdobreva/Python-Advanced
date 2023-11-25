matrix = [[int(y) for y in x.split()]for x in input().split("|")]

print(*(list(number for x in reversed(matrix) for number in x)), sep=" ")
