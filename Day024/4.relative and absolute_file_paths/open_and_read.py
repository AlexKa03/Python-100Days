# Absolute file path example:
# with open("/Users/USERNAME/Desktop/my_file.txt") as file:
#     content = file.read()
#     print(content)

# Relative file path example:
with open("../../Desktop/my_file.txt") as file:
    content = file.read()
    print(content)
