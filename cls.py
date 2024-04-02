import animal # animal.py is an module i.e. imported here
class Animal:
    def walk(self):
        print("walking")
class Dog(Animal): # Animal parent class is inherited here
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")


roger = Dog("Roger", 8)
print(roger.name)
print(roger.age)
roger.walk()
roger.bark()
animal.halt()