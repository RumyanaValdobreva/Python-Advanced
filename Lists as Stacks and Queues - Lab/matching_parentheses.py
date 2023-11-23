text = input()
stack = []

for element in range(len(text)):
    if text[element] == '(':
        stack.append(element)
    elif text[element] == ')':
        last_parentheses = stack.pop()
        print(text[last_parentheses:element+1])