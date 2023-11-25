# # FIRST OPTION
# #
# numbers_dictionary = {}
#
# line = input()
#
# while line != "Search":
#     number_as_string = line
#     try:
#         number = int(input())
#     except ValueError:
#         print("The variable number must be an integer")
#     else:
#         numbers_dictionary[number_as_string] = number
#     line = input()
#
# line = input()
#
# while line != "Remove":
#     searched = line
#     if searched in numbers_dictionary:
#         print(numbers_dictionary[searched])
#     line = input()
#
# line = input()
#
# while line != "End":
#     searched = line
#     try:
#         del numbers_dictionary[searched]
#     except KeyError:
#         print("Number does not exist in dictionary")
#     line = input()
#
# print(numbers_dictionary)

# # SECOND OPTION
numbers_dictionary = {}

while True:
    try:
        number_as_string = input()
        if number_as_string == "Search":
            break
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")

while True:
    searched = input()
    if searched == "Remove":
        break
    if searched in numbers_dictionary: # -> We can use try/except to check if the searched number is in the dictionary.
        print(numbers_dictionary[searched])


while True:
    try:
        searched = input()
        if searched == "End":
            break
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    break

print(numbers_dictionary)
