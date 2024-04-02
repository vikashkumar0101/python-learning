import random

a = 50
print(type(a))
number = 78
print(type(number))
print(isinstance(number, int))
j = float(78)
print(type(j))

food = ["hen", "chicken", "pizza", "jelly"]
print(random.choice(food))

s = 4 / 2
print(s)

name = "Harry"
name += "is my name"
print(name)

print(""" Harri

39

years old

""")

print("Harry".upper())
print("VIKASH".lower())
print("HJKGF".isupper())

name1 = "Vikash"
print(name1.lower())
print(len(name1))
print("ash" in name1)

name2 = "\"Viswash\""
name3 = "Vis\nwash"

print(name2)
print(name3)
print(name2[4])
print(name2[-2])
print(name2[1:6])

# bool with global function "any" global function

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])
print(read_any_book)

# bool with global function "all" global function

item_purchased = True
item_left = False

all_items = all([item_purchased, item_left])
print(all_items)


print(abs(-9.7))

print(round(7.654, 1))

print(round(98.87654, 3))