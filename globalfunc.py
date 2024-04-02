from functools import reduce

numbers = [1, 2, 3, 4, 6, 7, 8]


def double(a):
    return a * 2


result = map(double, numbers)
print(list(result))

numbers1 = [1, 2, 3, 4, 5, 6]
result1 = filter(lambda a : a % 2  == 0, numbers1)
print(list(result1), "Are the even numbers:")

expenses = [("Dinner", 80), ("Wash", 120)]
sum = reduce(lambda a, b : a[1] + b[1], expenses)
print(sum)