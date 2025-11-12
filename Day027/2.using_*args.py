# Create a function that can take any number of arguments and returns their sum. 

def add(*args):
    print(args)  # This will print the tuple of all arguments passed
    print(type(args))  # This will show that args is a tuple
    print(args[0])  # Accessing the first argument

    sum = 0
    for number in args:
        sum += number

    return sum

added_value = add(1, 2, 3, 4, 5)
print(added_value)  # Output: 15

added_value = add(10, 20, 30)
print(added_value)  # Output: 60
