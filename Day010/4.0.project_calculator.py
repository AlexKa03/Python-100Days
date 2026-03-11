# Demo: https://appbrewery.github.io/python-day10-demo/

import art

def add(n1, n2):
    """Adds two numbers together - mathematical operation"""
    return n1 + n2

#TODO: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    """Subtracts two numbers together - mathematical operation"""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies two numbers together - mathematical operation"""
    return n1 * n2

def divide(n1, n2):
    """Divides two numbers together - mathematical operation"""
    return n1 / n2

#TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
#print(operations["*"](4, 8))

#TODO:
# 1. Done: Program asks the user to type the first number.
# 2. Done: Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
# 3. Done: Program asks the user to type the second number.
# 4. Done: Program works out the result based on the chosen mathematical operator.
# 5. Done: Program asks if the user wants to continue working with the previous result.
# 6. Done: If yes, program loops to use the previous result as the first number and then repeats the calculation process.
# 7. Done: If no, program asks the user for the fist number again and wipes all memory of previous calculations.
# 8. Done: Add the logo from art.py
# 9. Done:  Self made option- add quit ot hte program

print(art.logo)

result = 0
status = True
old_number = False
while status:
    if not old_number:
        first_number = float(input("Enter the first number: "))
    else:
        first_number = result
        result = 0
    operator = input("Select operation:\n+\n-\n*\n/\n")
    second_number = float(input("Enter the second number: "))

    result += operations[operator](first_number, second_number)
    print(f"{first_number:.2f} {operator} {second_number:.2f} = {result:.2f}")

    continue_calculation = input(f"Type 'y' to continue your calculations with {result:.2f}, type 'n' if you want a new calculation or type 'q' you want to quit the calculator. (y/n/q): ")
    if continue_calculation == "y":
        old_number = True
    elif continue_calculation == "n":
        old_number = False
        result = 0
        print("\n" * 20)
    else:
        status = False
        print(f"Thank you for using this calculator. Goodbye!")
