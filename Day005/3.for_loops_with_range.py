# My own solution, I was just curious, if sum and range can work together- guess they can
print(f"Solution with sum and range: {sum(range(1, 101))}")

sum = 0
for i in range(1, 101):
    sum += i

print(f"Solution with for loop: {sum}")
