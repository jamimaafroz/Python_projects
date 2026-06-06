import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('anime_list.csv')
df = pd.DataFrame(data)
print(df)