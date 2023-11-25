def func_executor(*args):
    result = []
    for name, tuple_of_arguments in args:
        result.append(f"{name.__name__} - {name(*tuple_of_arguments)}\n")
    return "".join(result)


# def sum_numbers(num1, num2):
#     return num1 + num2
#
# 
# def multiply_numbers(num1, num2):
#     return num1 * num2
#
#
# print(func_executor(
#
#     (sum_numbers, (1, 2)),
#
#     (multiply_numbers, (2, 4))
#
# ))
