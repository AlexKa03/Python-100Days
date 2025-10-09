enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

#Local Scope
def drink_potion():
    potion_strength = 2
    print(f"Inner print: {potion_strength}")

drink_potion()
# print(f"Outer print: {potion_strength}")

#Global Scope
player_health = 10

def game():
    def check_health():
        potion_strength = 2
        print(f"Inner print: {player_health}")

    check_health() #Accessable only inside the game function

print(f"Outer print: {player_health}")
