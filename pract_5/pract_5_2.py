import pandas as pd
import matplotlib.pyplot as plt

url = 'https://github.com/Newbilius/Old-Games_DOS_Game_Gauntlet/raw/master/GAMES.csv'
df = pd.read_csv(url)

column_names = ["Title", "Genre", "html", "Year"]
df = pd.read_csv(url, delimiter=';', names=column_names, header=None)


def year():
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df.dropna(subset=['Year'], inplace=True)
    df['Year'] = df['Year'].astype(int)

    games_per_year = df['Year'].value_counts().sort_index()

    plt.figure(figsize=(12, 6))
    plt.bar(games_per_year.index, games_per_year.values, color='black')
    plt.title('Number of Games Released Per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Games')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def genre():
    genre_year = df.groupby(['Year', 'Genre']).size().unstack(fill_value=0)

    plt.figure(figsize=(14, 8))
    for genre in genre_year.columns:
        plt.bar(genre_year.index, genre_year[genre], label=genre, alpha=0.7)
    plt.title('Genre Popularity Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Games')
    plt.legend()
    plt.grid(True)
    plt.show()


year()
genre()
