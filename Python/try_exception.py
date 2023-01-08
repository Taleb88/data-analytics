def numbers(x):
    try:
        return 58 / x
    except ZeroDivisionError:
        print("Error. Fail.")

print(numbers(100))
print(numbers(0)) # Error, Fail. None.
print(numbers(15))
print(numbers(165.32))