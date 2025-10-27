# with open("weather_data.csv") as csv_file:
#     csv_reader = csv_file.readlines()
#
# print(csv_reader)

import csv

with open("weather_data.csv") as csv_file:
    data = csv.reader(csv_file)
    temperatures = []
    for row in data:
        temp = row[1]
        if temp.isdigit():
            temperatures.append(float(temp))

print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)