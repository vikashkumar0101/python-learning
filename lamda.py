number = lambda num: num + 10  # 10 is added to an argument
print(number(5))

x = lambda a, b, c: a + b + c
print(x(4, 7, 8))


def myfunc(n):
    return lambda j : j * 3
    mytripler = myfunc(3)
    print(mytripler(6))
