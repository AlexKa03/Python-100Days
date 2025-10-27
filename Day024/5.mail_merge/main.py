# Keep in mind that the if you open the whole project folder in your IDE, the open will result in errors
# because the working directory will be the project root folder, not the current folder of this file.
# Workaraund, either open the terminal in the folder where root is or provide the relative path to the file.

PLACEHOLDER = "[name]"

# Extracting the names
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Removing the new line (\n) and creating the new file
i = 0
for name in names:
    names[i] = name.replace("\n", "")
    name = name.strip()

    # Template letter
    with open("Input/Letters/starting_letter.txt") as template:
        letter = template.read()

    new_letter = letter.replace(PLACEHOLDER, name)

    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter_output:
        letter_output.write(new_letter)

    i += 1
