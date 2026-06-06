import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")
print(df)

# print(df.info())
print(df.head())
# print(df.describe())

## Calculating avarage
df['Avarage'] = (
    df['Math']+ df['Physics']+df['Chemistry']
)/3
print(df)

# finding top Student

top_student = df.loc[df['Avarage'].idxmax()]
print(top_student)

# topper based on individual subject

ace_math = df.loc[df['Math'].idxmax()]
print(ace_math['Name'])

ace_chem = df.loc[df['Chemistry'].idxmax()]
print(ace_chem['Name'])

ace_phy = df.loc[df['Physics'].idxmax()]
print(ace_phy['Name'])

def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    else:
        return "C"

df['Grade'] = (df['Avarage'].apply(grade))
print(df)

plt.bar(df['Avarage'],df['Name'], color='red')
plt.xlabel('Avarage')
plt.ylabel("Name")
plt.grid()
plt.show()


# Maximum Avarage 
print(df['Avarage'].max())

# Minimum Avarage

print(df['Avarage'].min())

# Class Avarage 

print(df['Avarage'].mean())

# Grade distribution 

print(df['Grade'].value_counts())
