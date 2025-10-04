fruits = ["Cherry", "Apple", "Pear"]

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0]) #Delaware
print(states_of_america[-1]) #Hawaii

print(states_of_america[1])
states_of_america[1] = "Pencilvania"
print(states_of_america[1])
states_of_america[1] = "Pennsylvania"

states_of_america.append("Burgas")
print(states_of_america[-1]) #Burgas

states_of_america.extend(["Sofia", "Plovdiv", "Alexland"])
print(states_of_america[-1]) #Alexland
print(states_of_america[-2]) #Plovdiv
print(states_of_america[-3]) #Sofia
