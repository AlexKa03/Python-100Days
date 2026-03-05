# You can combine different conditions using logical operators.
# A and B #Both conditions need to be true
# C or D #Only one condition needs to be true
# not E #The condition must be false

# PAUSE 1 - Age 45 to 55 Modifier
# Update the code so that people age 45 to 55 (inclusive of both ages) ride for free. Use logical operators to check that the age is greater than 45, and it's also less than 55.
# NOTE: The warning for simplification is just a suggestion. You can consider it and chose it, or you can ignore it. In this lesson I wanted to show you the and, or and not logical operators. So I recommend keeping the original code in case you come back to this lesson for review.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok. You can have a free ride on us.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
