n = int(input())
stack = []

for line in range(n):
    query = input().split()
    if len(query) > 1 and "1" in query:
        stack.append(int(query[1]))
    elif stack:
        if "2" in query:
            stack.pop()
        if "3" in query:
            print(max(stack))
        if "4" in query:
            print(min(stack))

while stack:
    print(stack.pop(), end="")
    if stack:
        print(", ", end="")


