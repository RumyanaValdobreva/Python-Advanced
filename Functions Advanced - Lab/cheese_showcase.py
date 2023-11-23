def sorting_cheeses(**kwargs):
    sorted_dictionary = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ''

    for name, qty in sorted_dictionary:
        result += f'{name}\n'
        sorted_qty = sorted(qty, reverse=True)
        result += '\n'.join(map(str, sorted_qty))
        result += '\n'
    return result


# print(
#     sorting_cheeses(
#         Parmesan=[102, 120, 135],
#         Camembert=[100, 100, 105, 500, 430],
#         Mozzarella=[50, 125],
#     )
# )