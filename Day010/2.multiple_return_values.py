def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide a valid input"

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result:{formated_f_name} {formated_l_name}"

print(format_name("ALEX", "kadIYSKI"))

print(format(input("What is your first name? "), input("hat is your last name? ")))