def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


grades = []

print("welcome")
try:
    average = divide(sum(grades), len(grades))
    print(f"average is {average}")
except ZeroDivisionError as e:
    print("There are no grades yet")

