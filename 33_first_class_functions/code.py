def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError(
            f"Not possible to divide on zero"
        )
    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 0, operator=divide)
print(result)