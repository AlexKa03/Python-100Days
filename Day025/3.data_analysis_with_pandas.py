import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Data.csv")

COLOR_DATA = data["Primary Fur Color"]

gray_count = len(data[COLOR_DATA == "Gray"])
cinnamon_count = len(data[COLOR_DATA == "Cinnamon"])
black_count = len(data[COLOR_DATA == "Black"])

data_dict = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count ": [gray_count, cinnamon_count, black_count]
}

squirrel_count = pandas.DataFrame(data_dict)
squirrel_count.to_csv("squirrel_count.csv")