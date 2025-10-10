# Original code:
# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")

# New code:
def my_function():
    for i in range(1, 21): # Changed from 20 to 21
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing? it is iterating through numbers 1 to 20 after the change, before the change it was 1 to 19
# 2. When is the function meant to print "You got it"? When i is equal to 20
# 3. What are your assumptions about the value of i? That it will take on each integer value from 1 to 20, inclusive- after the change
