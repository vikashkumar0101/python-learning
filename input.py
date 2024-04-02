import random

Names = ["Vikash", "Rahul", "Abhishesk", "Avinash", "Aditya", "Honey", "Sumit"]
name = random.choice(Names)
print(name)

if name == "Vikash":
    print("The entered name is acceptable: ")
else:
    print("The name is not acceptable")
