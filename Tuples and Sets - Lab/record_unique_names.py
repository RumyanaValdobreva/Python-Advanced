number_of_lines = int(input())
names = []

for line in range(number_of_lines):
    name = input()
    names.append(name)

for name in set(names):
    print(name)