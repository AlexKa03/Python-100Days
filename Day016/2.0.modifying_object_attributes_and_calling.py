from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"]) # Pause 1
table.add_column("Type", ["Electric", "Water", "Fire"]) # Pause 1

table.align = "l" # Pause 2

print(table)
