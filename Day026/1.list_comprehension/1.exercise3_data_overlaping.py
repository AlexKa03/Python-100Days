with open("file1.txt") as file1:
    file1 = [number.strip() for number in file1]

with open("file2.txt") as file2:
    file2 = [number.strip() for number in file2]

result = [int(match) for match in file1 if match in file2]

print(result)