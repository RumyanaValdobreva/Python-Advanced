def age_assignment(*args, **kwargs):
    data = {}
    for key, value in kwargs.items():
        for name in args:
            if key == name[0]:
                data[name] = value
    data = dict(sorted(data.items(), key=lambda x: x[0]))
    return "\n". join([f"{key} is {value} years old." for key, value in data.items()])


# print(age_assignment("Peter", "George", G=26, P=19))