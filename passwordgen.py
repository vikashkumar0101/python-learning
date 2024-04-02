import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the password generator!")
num_lett = int(input("How many letters you want in your password\n"))
num_num = int(input("How many numbers you want in your password\n"))
num_sym = int(input("How many symbols you want in your password\n"))

# password = ""
# for char in range(1, num_lett+1):
#   password += random.choice(letters)

# for char in range(1,num_num+1):
#   password += random.choice(numbers)

# for char in range(1,num_sym+1):
#   password += random.choice(symbols)
# print("Here is your password",password)

password_list = []
for char in range(1, num_lett + 1):
    password_list += random.choice(letters)

for char in range(1, num_num + 1):
    password_list += random.choice(numbers)

for char in range(1, num_sym + 1):
    password_list += random.choice(symbols)
# print("Here is your password", password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is {password}")