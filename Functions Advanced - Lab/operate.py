def operate(operator, *args):

    def add():
        return sum(args)

    def subtract():
        result = args[0]
        for num in range(1, len(args)):
            result -= args[num]
        return result

    def multiply():
        result = 1
        for num in args:
            result *= num
        return result

    def divide():
        result = args[0]
        for num in range(1, len(args)):
            result /= args[num]
        return result

    if operator == '+':
        return add()
    elif operator == '-':
        return subtract()
    elif operator == '*':
        return multiply()
    elif operator == '/':
        return divide()

# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
#
# from functools import reduce
#
# def operate(operator, *args):
#
#     def add():
#         return reduce(lambda a, b: a + b, args)
#
#     def subtract():
#         return reduce(lambda a, b: a - b, args)
#
#     def multiply():
#         return reduce(lambda a, b: a * b, args)
#
#     def divide():
#         return reduce(lambda a, b: a / b, args)
#
#     if operator == '+':
#         return add()
#     elif operator == '-':
#         return subtract()
#     elif operator == '*':
#         return multiply()
#     elif operator == '/':
#         return divide()

# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
