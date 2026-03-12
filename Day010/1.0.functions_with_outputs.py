# def my_function():
#     return 3 * 2
#
# output = my_function()
# print(output)

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

formated_string = format_name(first_name, last_name)
print(formated_string)

output = len("Alex")
