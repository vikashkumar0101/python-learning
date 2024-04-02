# def greet():
#   print("Hello vikash")
#   print("how do you do")


# greet()


#   def greet_with_name( name, name2):
#      print(f"Hello Mr. {name} ")
#       print(f"How are you {name2}")

# greet_with_name("Vicky", "Rohit")


def greet_with_name(name2, name):
    print(f"Hello Mr. {name} ")
    print(f"How are you {name2}")


greet_with_name(name="Vicky", name2="Rohit")


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
        if is_prime:
            print("The entered number is prime number ")
            break
        else:
            print("Not a prime number")
            break


n = int(input("Enter a number to check whether it is a prime number or not.\n"))
prime_checker(number=n)
