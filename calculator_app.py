#1. Create functions for each arithmetic operation (addition, subraction, multiplication, division)
#2. Use inputs to ask the user what operation they want to perform, and what
#   numbers they want to use.
#3. Ensure your code can handle division by zero and other potential errors.
#   So if you divide by 0, there is error handling set up to prevent an error from 
#   showing up on the console.

def calculator():
    while True:
        operator = ("add", "subtract", "multiply", "divide")
        task = input("Please enter what you would like to calculate (add/subtract/multiply/divide):\t")
        if task not in operator:
            print("Invalid input, please try again")
            continue
        else:
            break
    num1 = float(input("Enter the first number:\n"))
    num2 = float(input("enter the second number:\n"))
    num_list = [num1, num2]
    for answer in num_list:
        if task == "add":
            print(f"Answer: {sum(num_list)}")
            break
        
        elif task == "multiply":
            print(f"Answer: {num_list[0] * num_list[1]}")
            break
        elif task == "divide":
            print(f"Answer: {num_list[0] / num_list[1]}")
            break
        else:
            print(f"Answer: {num_list[0] - num_list[1]}")
            break
calculator()