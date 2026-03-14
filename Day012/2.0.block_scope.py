# There is no Block Scope in Python

game_level = 3
enemie = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = "" # Recommended- due to linter
    if game_level < 5:
        new_enemy = enemie[0]

    print(new_enemy)

create_enemy()
