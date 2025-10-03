print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoaster")
    if age <= 12:
        print("Your ticket is $5.")
    elif age <= 18:
        print("Your ticket is $7.")
    elif age <= 22:
        print("We understand you it's been hard to find a new job as a developer, the ticket is on us.")
    else:
        print("Your ticket is $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
