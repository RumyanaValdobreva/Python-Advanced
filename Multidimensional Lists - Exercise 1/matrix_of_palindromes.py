rows, columns = [int(x) for x in input().split()]
matrix = []
palindrome = ""


for row in range(rows):
    for column in range(columns):
        first_last = chr(row + 97)
        middle = chr(row + column + 97)
        palindrome = first_last + middle + first_last
        print(palindrome, end=" ")
    print()
