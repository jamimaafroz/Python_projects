import pandas as pd
import matplotlib.pyplot as plt

# =====================
# LOAD DATA
# =====================
df = pd.read_csv("anime_list.csv")


# =====================
# DASHBOARD FUNCTIONS
# =====================

def show_summary():
    print("\n===== SUMMARY =====")
    print("Total Anime:", len(df))
    print("Average Rating:", round(df["Rating"].mean(), 2))
    print("Total Episodes:", df["Episodes"].sum())


def show_top_anime():
    print("\n===== TOP 5 ANIME =====")
    print(df.sort_values(by="Rating", ascending=False).head(5))


def genre_analysis():
    genre_count = df["Genre"].value_counts()
    genre_rating = df.groupby("Genre")["Rating"].mean()

    print("\n===== GENRE COUNT =====")
    print(genre_count)

    print("\n===== AVG RATING BY GENRE =====")
    print(genre_rating)

    return genre_count


def filter_by_genre():
    genre = input("\nEnter genre (Action/BL/Comedy): ")
    filtered = df[df["Genre"] == genre]

    print("\n===== FILTER RESULT =====")
    print(filtered)


# =====================
# VISUALIZATION FUNCTIONS
# =====================

def plot_genre_distribution():
    genre_count = df["Genre"].value_counts()

    plt.figure(figsize=(6, 6))
    plt.pie(
        genre_count,
        labels=genre_count.index,
        autopct="%1.1f%%"
    )

    plt.title("Anime Genre Distribution")
    plt.savefig("Anime Genre Distribution")
    plt.show()


def plot_top_anime():
    top5 = df.sort_values(by="Rating", ascending=False).head(5)

    plt.figure(figsize=(8, 5))
    plt.bar(top5["Anime"], top5["Rating"])

    plt.title("Top Rated Anime")
    plt.xlabel("Anime")
    plt.ylabel("Rating")
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.savefig("Top Rated Anime") 

    plt.show()


def plot_rating_trend():
    sorted_df = df.sort_values(by="Rating")

    plt.figure(figsize=(10, 5))
    plt.plot(sorted_df["Anime"], sorted_df["Rating"], marker="o")

    plt.title("Anime Rating Trend")
    plt.xlabel("Anime")
    plt.ylabel("Rating")
    plt.xticks(rotation=45)
    plt.grid()
    plt.savefig('Anime Rating Trend')

    plt.show()


# =====================
# MENU SYSTEM
# =====================

def menu():
    print("\n===== ANIME DASHBOARD =====")
    print("1. Summary")
    print("2. Top Anime")
    print("3. Genre Analysis")
    print("4. Genre Pie Chart")
    print("5. Top Anime Bar Chart")
    print("6. Rating Trend Line Chart")
    print("7. Filter by Genre")
    print("0. Exit")


# =====================
# MAIN LOOP
# =====================

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        show_summary()

    elif choice == "2":
        show_top_anime()

    elif choice == "3":
        genre_analysis()

    elif choice == "4":
        plot_genre_distribution()

    elif choice == "5":
        plot_top_anime()

    elif choice == "6":
        plot_rating_trend()

    elif choice == "7":
        filter_by_genre()

    elif choice == "0":
        print("Exiting dashboard... 🚀")
        break

    else:
        print("Invalid choice. Try again.")