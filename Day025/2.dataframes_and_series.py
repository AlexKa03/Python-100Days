import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data)) # DataFrame - Excel Sheet
print(type(data["temp"])) # Series - It can be Column or Row

data_dict = data.to_dict() # Convert from DataFrame to Dict (example, many more conversions available)
print(data_dict)

temp_list = data["temp"].to_list() # Convert Series to List
print(temp_list)

# Normal solution
temp_avg = sum(temp_list) / len(temp_list) # Average temperature
print(f"Average temp: {temp_avg}")

# Using Pandas solution
print(f"Average temp: {data["temp"].mean()}")

# Find the maximum temperature using pandas
print(f"Max temp: {data["temp"].max()}")

# Or other awesome things from panda
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])

# Print the row which had the highest temperature
print(data[data.temp == data.temp.max()])

# Print specific value from a column
monday = data[data.day == "Monday"]
print(monday.condition)
# Print the temperature in Fahrenheit
print((monday.temp * 9/5) + 32)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
students_grades = pandas.DataFrame(data_dict)
print(students_grades)

students_grades.to_csv("data.csv") # Export data to a CSV file, we only give where to be saved