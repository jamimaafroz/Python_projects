import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("students.csv")

print("=== Student Data ===")
print(df)

# Calculate Average
df["Average"] = (
    df["Math"] +
    df["Physics"] +
    df["Chemistry"]
) / 3

# Find Top Student
top_student = df.loc[df["Average"].idxmax()]

print("\n=== Top Student ===")
print(f"Name: {top_student['Name']}")
print(f"Average Marks: {top_student['Average']:.2f}")

# Subject Toppers
math_topper = df.loc[df["Math"].idxmax()]
physics_topper = df.loc[df["Physics"].idxmax()]
chemistry_topper = df.loc[df["Chemistry"].idxmax()]

print("\n=== Subject Toppers ===")
print(f"Math: {math_topper['Name']}")
print(f"Physics: {physics_topper['Name']}")
print(f"Chemistry: {chemistry_topper['Name']}")

# Grade Calculation
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    else:
        return "C"

df["Grade"] = df["Average"].apply(grade)

print("\n=== Results ===")
print(df)

# Statistics
print("\n=== Statistics ===")
print(f"Highest Average : {df['Average'].max():.2f}")
print(f"Lowest Average  : {df['Average'].min():.2f}")
print(f"Class Average   : {df['Average'].mean():.2f}")

print("\n=== Grade Distribution ===")
print(df["Grade"].value_counts())

# Bar Chart
plt.figure(figsize=(8, 5))

plt.bar(df["Name"], df["Average"])

plt.title("Student Average Marks")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.grid(axis="y")

plt.savefig("student_average.png")

plt.show()

# Grade Distribution Pie Chart
grade_counts = df["Grade"].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
    grade_counts,
    labels=grade_counts.index,
    autopct="%1.1f%%"
)

plt.title("Grade Distribution")

plt.savefig("grade_distribution.png")

plt.show()