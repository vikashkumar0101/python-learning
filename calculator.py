def calculator():
    print("Welcome to the calculator")
    print("Enter the first number.")
    num1 = float(input())
    print("Enter second number.")
    num2 = float(input())
    print("Enter the operator (+, -, /, *):")
    op = input()
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        print("Invalid operator")
        return
    print(f"The result is:->{result}")

calculator()
