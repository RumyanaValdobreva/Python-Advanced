# Python Advanced Exam - 22 October 2022

from collections import deque

caffeine_milligrams = list(map(int, input().split(", ")))
energy_drinks = deque([int(x) for x in input().split(", ")])
current_caffeine = 0
max_caffeine = 300

while True:
    if not energy_drinks:
        break
    if not caffeine_milligrams:
        break

    current_caffeine = caffeine_milligrams.pop()
    current_energy_drink = energy_drinks.popleft()
    result = current_caffeine * current_energy_drink

    if result + current_caffeine <= max_caffeine:
        current_caffeine += result
    else:
        energy_drinks.append(current_energy_drink)
        current_caffeine -= 30
        if current_caffeine < 0:
            current_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {current_caffeine} mg caffeine.")