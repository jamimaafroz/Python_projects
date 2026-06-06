import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('anime_list.csv')
df = pd.DataFrame(data)
print(df)

print(df["Rating"].mean())
print(df["Episodes"].sum())

top_anime = df.sort_values(
    by="Rating",
    ascending=False
)

print(top_anime)

genre_count = df["Genre"].value_counts()

print(genre_count)


genre_rating = df.groupby("Genre")["Rating"].mean()

print(genre_rating)

plt.pie(
    genre_count,
    labels=genre_count.index,
    autopct="%1.1f%%"
)

plt.title("Anime Genre Distribution")
plt.savefig('Anime Genre Distribution')
plt.show()


top5 = df.sort_values(
    by="Rating",
    ascending=False
).head(5)

plt.bar(
    top5["Anime"],
    top5["Rating"]
)

plt.title("Top Rated Anime")
plt.show()

