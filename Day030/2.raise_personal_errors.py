height = float(input("Enter height in m: "))
weight = int(input("Enter weight in kg: "))

if height > 3:
    raise ValueError("Human height should not be greater than 3 meters.")

bmi = weight / height ** 2
print(bmi)
