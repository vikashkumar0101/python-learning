# complete https://youtu.be/eWRfhZUzrAc
# FastAPI - Python Framework - https://youtu.be/tLKKmouUams
# Postgresql -  https://youtu.be/SpfIwlAYaKk
# Git & Github - https://youtu.be/RGOj5yH7evk

from enum import  Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color['RED'].value)
print(list(Color))

class State(Enum):
    ACTIVE = 1
    INACTIVE = 0

print(State['ACTIVE'].value)


# conditional_statement

condition = False
if condition == True:
    print("The condition was true")
    print("The condition is outside")

else:
    print("The condition was false")

# Lists

dogs = ["roger", 1, "Holland", False, "Belle", "Hawllet", True]
dogs[0] = "salim"
dogs.append("Patty")
print("roger" in dogs)
print(dogs[0])
print(len(dogs))
print(dogs)

# item lists

items = ["Peter", 4, "Nelson", 9, "Hopman", "richard"]
items.append("Rohman")
items.insert(1, "renny")
items[1:2] = ["test1", "test2"]
print(items)

# sorting in lists

name = ["Vikash", "Satish", "Sandip", "virat", "Abhishek", "Zeenat", "Warren", "Xavier", "Vinay"]
namecopy = name[:]
name.sort()
print(name)
print(namecopy)

# tuples examples

name = ("Roger", "Peter", "Luxumb", "Christy")
print(name)
print(name[-1])
print(len(name))
print("Roger" in name)

newTuple = name  + ("Vikash", "guina")
print(newTuple)

# dictionaries

dog = {"Name": "Roger", "age": "8", "color": "brown"}
print(dog.get("Name"))
print("color" in dog)
print(dog.pop("Name"))
print(list(dog.items()))
print(len(dog))
print(dog)

# sets demo programs
print("Examples of set operations")
set1 = {"Roger", "peter", "harris"}
set2 = {"Lillyput", "peter"}

mod = set1 | set2
print(mod)
intersection = set1 & set2
print(intersection)
print(list(set1))
print("harris" in set1)

number1 = int(input("Enter a number\n"))
print(f"The number is  {number1}")
if number1 % 2  == 0:
    print("Number entered is an even number")
else:
    print("The number entered is odd number")


#function

def hello(name):
    print("Hello" + name)
hello("Vikash")
hello("rocky")