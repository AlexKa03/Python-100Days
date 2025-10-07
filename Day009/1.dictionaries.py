programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Printing value of a specific key from dictionary
# print(programming_dictionary["Bug"])

# Adding a new Key-Value pair in dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary["Loop"])

# Empty dictionary
# empty_dictionary = {}
# empty_dictionary["nothing"] = "Yes, nothing"

# Wipe dictionary
# print(programming_dictionary)
# programming_dictionary = {}
# print(programming_dictionary)

# Edit item in dictionary
#print(programming_dictionary["Bug"])
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary["Bug"])

# Loop trough dictionary
for key in programming_dictionary:
    print(key) # Will print only the key
    print(programming_dictionary[key]) # Will print only the value of the key
