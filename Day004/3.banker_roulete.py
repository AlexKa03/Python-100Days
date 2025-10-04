import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# First possible solution
print(random.choice(friends))

# Second possible solution
random_index = random.randint(0, 4)
print(friends[random_index])
