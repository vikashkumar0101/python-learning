try:
    result = 3 / 0
except ZeroDivisionError:
    print("The number is not divisible by 0")
finally:
    result = 1
    print(result)

try:
    raise Exception("An Error!")
except Exception as error:
    print(error)
