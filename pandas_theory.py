import numpy as np
import pandas as pd

students = pd.read_csv("StudentsPerformance.csv")
# print(students.info())
# print(students.describe())
# print(students[::2])
# print(students[students["test preparation course"] == "completed"][["math score", "gender"]].describe())

students["total score"] = ((students["math score"]
                           + students["reading score"]
                           + students["writing score"]) / 3)

# def difficult_func(row):
#     return (row["math score"]    + row["reading score"] + row["writing score"]) / 3

# students["total score"] = students.apply(
#     lambda row: difficult_func(row),
#     axis=1
# )

# print(students.sort_values("total score", ascending=False).head())

# студенты2 = students.assign(ИтоговыйБалл = 
#     lambda row: difficult_func(row)
# )
# print(студенты2.sort_values("ИтоговыйБалл", ascending=False).head())

# agg_functions = {"total score": ["mean", "median", "max"], "reading score": ["min", "count"]}
# ret = students.groupby(["gender"]).agg(agg_functions)
# print(ret)

students["math score"].plot()

