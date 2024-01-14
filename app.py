def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculator():

    num1 = float(input("Enter number 1: "))
    operator = input("pick: (+, -, *, /): ")
    num2 = float(input("Enter number 2: "))

    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    else:
        result = "not on list"

    print(f"{result}")

calculator()