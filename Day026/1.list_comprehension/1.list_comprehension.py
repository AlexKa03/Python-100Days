# Increase each number in the list by 1 using list comprehension
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

# What will be the output of the following list comprehensions?
name = "Alex"
letters_list = [letter for letter in name] # the name seperated into letters

# Create a list using range and list comprehension and multiply each number by 2
range_list = [num * 2 for num in range(1,5)]

# Conditional list comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

# Create a list of names in uppercase where the length of the name is greater than 5
long_names = [name.upper() for name in names if len(name) > 5]