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

print("the minimum midterm grade is ", min)
print("the maximum midterm grade is ", max)
print("THe median midterm grade is ", median)
print("the interquartile range of the final grade is ", interquartile)
print("the range of the attendance grade is ", range)