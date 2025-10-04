print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $5.")
        bill += 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill += 7
    else:
        print("Adult tickets are $12.")
        bill += 12

    wants_photo = input("Would you like to have a photo? (Y/N): ").lower()
    if wants_photo == "Y":
        print("Your photo is $3.")
        bill += 3

    print(f"Your bill is: ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
