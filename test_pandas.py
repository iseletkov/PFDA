import numpy as np
import pandas as pd

# s = pd.Series(np.random.randint(-10, 10, 50))

# print(s[(s <-5) | (s>5)])

# if x>0 and x<10:

# students_marks_dict = {
#     "student": ["Студент_1", "Студент_2", "Студент_3"],
#     "math": [5, 3, 4],
#     "physics": [4, 5, 5]
# }
# students = pd.DataFrame(students_marks_dict)
# students.index = ["A", "E", "C"]
# print(students)

# print(students.columns)

# print(students.loc["A":"C"])

# students.to_json("students_test.json")

students = pd.read_json("students_test.json")
print(students)