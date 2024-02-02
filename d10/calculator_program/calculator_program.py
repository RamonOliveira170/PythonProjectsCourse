import os
from art import logo

def result(first_number, operator, second_number):
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        return first_number / second_number
    else:
        print("Invalid operator.")
        return first_number

def calculator():
    print(logo)
    continue_calculating = True
    first_number = float(input("What's the first number?: "))

    while continue_calculating:
        print("+\n-\n*\n/")
        operator = input("Pick an operation: ")
        second_number = float(input("What's the second number?: "))
        total = result(first_number, operator, second_number)
        print(f"{first_number} {operator} {second_number} = {total}")
        should_continue = input(f"Type 'y' to continue calculating with {total}, \
or type 'n' to start a new calculation, 'Stop' to exit: ").capitalize().strip()
        if should_continue[0] == "Y":
            os.system("cls")
            first_number = total
            print(f"First number: {total}")
        elif should_continue[0] == "N":
            continue_calculating = False
            os.system("cls")
            calculator()
        elif should_continue == "Stop":
            continue_calculating = False

calculator()

print("Calculator has stopped")
