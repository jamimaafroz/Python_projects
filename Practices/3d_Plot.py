import matplotlib.pyplot as plt
import pandas as pd


data = {
    "Salary": [50000, 75000, 45000, 90000, 60000, 115000, 80000, 105000, 70000, 130000,
               85000, 140000, 95000, 165000, 110000, 150000, 120000, 180000, 135000, 195000],
    "dept": ["HR", "IT", "Finance", "IT", "HR", "Finance", "IT", "HR", "IT", "Finance"] * 2,
    "age": [22, 26, 24, 30, 28, 35, 32, 38, 31, 43, 34, 46, 36, 52, 40, 48, 42, 55, 45, 60],
    "experience": [1, 5, 2, 8, 6, 12, 10, 15, 9, 20, 11, 22, 14, 28, 18, 25, 19, 32, 22, 36]
}

df = pd.DataFrame(data)
df
ax= plt.axes(projection = '3d')
ax.scatter(df['age'],df['Salary'],df['experience'])
ax.set_xlabel('Age')
ax.set_ylabel('Salary')
ax.set_zlabel('Experience')
plt.show()