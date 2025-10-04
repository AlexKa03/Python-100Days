print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

print(f"Each person should pay: ${round((bill / people) * (1 + (tip / 100)), 2)}")

#Other possible calculation
total = (tip / 100 * bill + bill) / people
print(f"Each person should pay: ${round(total, 2)}")