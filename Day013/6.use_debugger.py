import random
import maths

# Original code:
# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = maths.add(new_item, item)
#     b_list.append(new_item)
#     print(b_list)


# mutate([1, 2, 3, 5, 8, 13])

# New code:
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item) # Indented this line to be inside the for loop, so that each new_item is added to b_list
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
