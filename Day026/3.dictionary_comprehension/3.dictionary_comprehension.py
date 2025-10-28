import random

# Create a dictionary of students and their scores using dictionary comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_scores = {student:random.randint(1,100) for student in names}

# Create a new dictionary with students who passed (score >= 60)
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

print(students_scores)
print(passed_students)