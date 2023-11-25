def grocery_store(**kwargs):
    string = ""
    products_info = kwargs
    products_info = dict(sorted(products_info.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))

    result = [f"{key}: {value}" for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))]
    return "\n".join(result)


# print(grocery_store(
#     bread=5,
#     pasta=12,
#     eggs=12,
# ))