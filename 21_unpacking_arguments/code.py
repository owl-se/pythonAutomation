def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(1, 2, 5))


def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))
num = {"x": 15, "y": 25}
print(add(num["x"], num["y"]))
print(add(**num))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator"


print(apply(1,2,3,4,5, operator="*"))