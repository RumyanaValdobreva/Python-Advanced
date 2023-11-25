from collections import deque

expression = input().split()
numbers = deque()

for el in expression:
    if el not in "+-*/":
        numbers.append(int(el))
    else:
        while len(numbers) > 1:
            first_number = numbers.popleft()
            second_number = numbers.popleft()
            if el == "+":
                numbers.appendleft(first_number + second_number)
            if el == "-":
                numbers.appendleft(first_number - second_number)
            if el == "*":
                numbers.appendleft(first_number * second_number)
            if el == "/":
                numbers.appendleft(first_number // second_number)

print(numbers[0])