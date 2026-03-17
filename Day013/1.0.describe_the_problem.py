def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
    # It counts from 1 to 19 (including)
# 2. When is the function meant to print "You got it"?
    # When the i = 20
# 3. What are your assumptions about the value of i?
    # The variable i will never reach 20, since the range() function is not inclusive for the stop number

# How to fix
    # Just change the range function to count to 21
