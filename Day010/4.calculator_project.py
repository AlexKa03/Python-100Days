import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

continue_calculation = "n"
total = 0

while continue_calculation != "exit":
    if continue_calculation == "y":
        number_one = total
    else:
        number_one = float(input("What's the first number? "))
    print("+\n-\n*\n/")
    operation = input("Pick an operation? ")
    number_two =  float(input("What's the next number? "))

    for operand in operations:
        if operand == operation:
            total = operations[operand](number_one, number_two)

    continue_calculation = input(f"Type 'y' to continue calculating with {total}, type 'n' to start a new calculation or 'exit' if you wish to exit the program: ").lower()
    if continue_calculation == "n":
        print("\n" * 20)

# DONE-1: Write out the other 3 functions - subtract, multiply and divide.
# DONE-2: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
# DONE-3: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
