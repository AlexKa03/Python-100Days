# There is no Block Scope in Python

game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

#print(new_enemy) Cant print it, since the local scope is only inside the create_enemy function

create_enemy()
