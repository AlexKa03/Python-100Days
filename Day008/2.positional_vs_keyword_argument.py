# Functions with input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")

# greet_with_name("Jack Bauer")

name = input("What is your name? ")
location = input("Where do you live in? ")
# greet_with(name, location)

greet_with(name = "Alex", location = "Burgas")
greet_with(location = "Provincetown", name = "Alex")
