student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping trough dictionaries
for (key, value) in student_dict.items():
    print(value)

import pandas

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

# Looping trough DataFrame with for loop - not that useful
for (key, value) in student_dataframe.items():
    print(value)

# Loop trough rows of a DataFrame
for (index, row) in student_dataframe.iterrows():
    print(row.student)