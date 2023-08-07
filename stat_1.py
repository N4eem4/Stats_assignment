import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_grades.csv")
mean = df["Final Grade"].mean()
min = df["Final Grade"].min()
max = df["Final Grade"].max()
median = df["Final Grade"].median()

lower = df["Final Grade"].max() * 0.25
upper = df["Final Grade"].max() * 0.75
interquartile = upper - lower

print(mean)
print(min)
print(max)
print(median)
print(interquartile)