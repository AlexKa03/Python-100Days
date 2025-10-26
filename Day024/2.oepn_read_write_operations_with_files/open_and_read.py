# OPEN AND READ OPERATIONS WITH FILES

# Opening and reading a file
# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close

# Using 'with' statement to handle file operations, no need to remember the close()
# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

# OPEN AND WRITE OPERATIONS WITH FILES

# Writing to a file (this will overwrite existing content) | mode="w" stands for write
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# Appending to a file (this will add to existing content) | mode="a" stands for append
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# If the mode is write and the file is not created, a new file will be created with the given name and it will write to it
# with open("new_file.txt", mode="w") as file:
#     file.write("New text.")