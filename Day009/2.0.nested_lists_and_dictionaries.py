capitals = {
    "Bulgaria": "Sofia",
    "Italy": "Rome",
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary
travel_log1 = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Stuttgart", "Munich", "Frankfurt am Main"],
}

print(travel_log1["France"][1])

# Nested List in List
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# Nested Dictionary in Dictionary
travel_log2 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 3,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Stuttgart", "Munich", "Frankfurt am Main"],
        "total_visits": 4,
    }
}

print(travel_log2["Germany"]["cities_visited"][1])
