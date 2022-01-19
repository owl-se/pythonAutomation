def named(**kwargs):
    print(kwargs)

names = {"name": "Bob", "age": 25}

named(**names)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg} : {value}")


print_nicely(name="Nob", age=23)