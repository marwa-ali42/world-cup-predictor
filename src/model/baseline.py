import pandas as pd

df = pd.read_csv("data/processed/clean_results.csv")
print(df.head())

def get_results(row):
    if row['home_score'] > row['away_score']:
        return 'home_win'
    elif row['home_score'] < row['away_score']:
        return 'away_win'
    else:
        return 'draw'
    
df['result'] = df.apply(get_results, axis=1)
home_wins = df[df['result'] == 'home_win']['home_team'].value_counts()
away_wins = df[df['result'] == 'away_win']['away_team'].value_counts()
print(f"Number of home wins: {home_wins}")
print(f"Number of away wins: {away_wins}")

total_wins = home_wins.add(away_wins, fill_value=0)
print(f"Total wins per team: {total_wins.sort_values(ascending=False).head(10)}")

total_games = df['home_team'].value_counts().add(df['away_team'].value_counts(), fill_value=0)

win_rate = total_wins / total_games
print(f"Win rate per team: {win_rate.sort_values(ascending=False).head(10)}")