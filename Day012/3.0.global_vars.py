# Modifying Global Scope
enemies = 1

def increase_enemies():
    global enemies # This fixes the below error, by making the variable global
    enemies += 1 # Errors out, if it is local only
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
