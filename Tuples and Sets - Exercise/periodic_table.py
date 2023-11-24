n = int(input())
elements = set()


for line in range(n):
    element = input().split()
    for el in element:
        elements.add(el)


print("\n".join(elements))