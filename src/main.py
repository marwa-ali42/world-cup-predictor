import pandas as pd
from model.elo import run_elo
df = pd.read_csv('data/processed/clean_results.csv')

# Calculate ELO ratings
ratings = run_elo(df)
sorted_ratings = sorted(ratings.items(), key=lambda x: x[1], reverse=True)
for team, rating in sorted_ratings[:10]:
    print(f"{team}: {rating:.2f}")
