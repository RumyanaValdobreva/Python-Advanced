from collections import deque

chocolate = [int(x) for x in input().split(", ")]
cups_of_milk = deque([int(x) for x in input().split(", ")])
milkshake = 0

while milkshake < 5 and chocolate and cups_of_milk:
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue

    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue

    if chocolate[-1] == cups_of_milk[0]:
        chocolate.pop()
        cups_of_milk.popleft()
        milkshake += 1
    else:
        cups_of_milk.rotate(-1)
        chocolate[-1] -= 5

if milkshake == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join([str(x) for x in chocolate]) if chocolate else 'empty'}")
print(f"Milk: {', '.join([str(x) for x in cups_of_milk]) if cups_of_milk else 'empty'}")
