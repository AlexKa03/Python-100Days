# Original code:
# age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}.")

# New code:
try: # Added try and except to catch invalid inputs
    age = int(input("How old are you?"))
except ValueError:
    print("You typed in an invalid input. Please try again with numerical input, like 22.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.") # Added f-string to properly format the output and indented the print statement
