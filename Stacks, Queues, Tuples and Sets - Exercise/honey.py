from collections import deque


working_bees = deque(int(x) for x in input().split())
nectar_value = [int(x) for x in input().split()]
symbols = deque(x for x in input().split())
collected_nectar = deque()
total_honey = 0

operations = {"+": lambda x, y: x + y,
              "-": lambda x, y: abs(x - y),
              "*": lambda x, y: x * y,
              "/": lambda x, y: x // y}


while working_bees and nectar_value:
    if nectar_value[-1] >= working_bees[0]:
        if nectar_value[-1] == 0 and working_bees[0] == 0:
            working_bees.popleft()
            nectar_value.pop()
            continue
        collected_nectar.append([working_bees.popleft(), nectar_value.pop(), symbols.popleft()])
    else:
        nectar_value.pop()
        continue


while collected_nectar:
    bee, nectar, symbol = collected_nectar.popleft()
    total_honey += operations[symbol](bee, nectar)

print(f"Total honey made: {total_honey}")

if working_bees:
    bees_left = list(map(str, working_bees))
    print(f"Bees left: {', '.join(bees_left)}")

if nectar_value:
    nectar_left = list(map(str, nectar_value))
    print(f"Nectar left: {', '.join(nectar_left)}")


