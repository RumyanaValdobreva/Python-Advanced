def recursive_power(number, power):
    if power == 1:
        return number
    return number * recursive_power(number, power - 1)

# def recursive_power(number, power, counter=1):
#     if counter == power:
#         return number
#     counter += 1
#     return number * recursive_power(number, power, counter)

# print(recursive_power(2, 10))
# print(recursive_power(10, 100))