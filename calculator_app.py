#1. Create functions for each arithmetic operation (addition, subraction, multiplication, division)
#2. Use inputs to ask the user what operation they want to perform, and what
#   numbers they want to use.
#3. Ensure your code can handle division by zero and other potential errors.
#   So if you divide by 0, there is error handling set up to prevent an error from 
#   showing up on the console.
def add (num1, num2):
    numbers = [num1, num2]
    for num in numbers:
        print(f"Answer: {num1 + num2}")
        break

def subtract(num1, num2):
    numbers = [num1, num2]
    for num in numbers:
        print(f"Answer: {num1 - num2}")
        break

def multiply(num1, num2):
    numbers = [num1, num2]
    for num in numbers:
        print(f"Answer: {num1 * num2}")
        break

def divide(num1, num2):
    numbers = [num1, num2]
    for num in numbers:  
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = 0
        print(f"Answer: {result}")
        break

def calculator():
    while True:
        operator = ("add", "subtract", "multiply", "divide")
        task = input("Please enter what you would like to calculate (add/subtract/multiply/divide):\t").lower()
        if task not in operator:
            print("Invalid input, please try again")
            continue
        else:
            break
    while True:
        try:
            num1 = float(input("Enter the first number:\n"))
        except ValueError:
            print("Invalid input, please try again.")
            continue
        break
    while True:
        try:
            num2 = float(input("enter the second number:\n"))
        except ValueError:
            print("Invalid input, please try again.")
            continue
        break
    if task == "add":
        add(num1, num2)
    elif task == "multiply":
        multiply(num1, num2)
    elif task == "divide":
        divide(num1, num2)
    else:
        subtract(num1, num2)

calculator()