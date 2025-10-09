# Modifying Global Scope

enemies = 1
hostile = 1

def increase_enemies():
    global hostile
    hostile += 1
    print(f"enemies | hostile inside function: {enemies} | {hostile}")
    return enemies +1


enemies = increase_enemies()
print(f"enemies | hostile outer function: {enemies} | {hostile}")
