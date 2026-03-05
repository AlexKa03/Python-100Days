# We're going to build a tip calculator.
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay:
# (150.00 / 5) * 1.12 = 33.6
# After formatting the result to 2 decimal places = 33.60
# Demo: https://appbrewery.github.io/python-day2-demo/

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15 "))
people = int(input("How many people to split the bill? "))

tip_percentage = (tip / 100) * 1
total = bill * tip_percentage
bill_per_person = total / people

print(f"Each person should pay: ${round(bill_per_person, 2):.2f}")
# the :.2f rounding was not mentioned in the lesson