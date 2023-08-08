import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_grades.csv")
min = df["Midterm Grade"].min()
max = df["Midterm Grade"].max()
median = df["Midterm Grade"].median()

lower = df["Final Grade"].quantile(0.25) 
upper = df["Final Grade"].quantile(0.75)
interquartile = upper - lower


highRange = df["Attendance Grade"].max()
lowRange = df["Attendance Grade"].min()
range = highRange - lowRange

print(min)
print(max)
print(median)
print(interquartile)
print(range)