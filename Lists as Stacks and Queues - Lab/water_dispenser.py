from collections import deque

water_qty = int(input())
name = input()
water_line = deque()

while name != 'Start':
    water_line.append(name)
    name = input()

command = input()

while command != 'End':
    if 'refill' in command:
        water_qty += int(command[-1])
    else:
        liters = int(command)
        if liters <= water_qty:
            water_qty -= liters
            print(f"{water_line.popleft()} got water")
        else:
            print(f"{water_line.popleft()} must wait")
    command = input()

print(f"{water_qty} liters left")
