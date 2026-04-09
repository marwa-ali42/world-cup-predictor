import random
import pandas as pd
from simulate_random import simulate_match
from model.elo import run_elo
from collections import Counter

df = pd.read_csv('data/processed/clean_results.csv')
df = df.sort_values("date")
actual_ratings = run_elo(df)

def simulate_round(teams, ratings):
    winners = []
    for i in range(0, len(teams), 2):
        winner = simulate_match(teams[i], teams[i+1], ratings)
        winners.append(winner)
    return winners

sorted_teams = sorted(actual_ratings.items(), key= lambda x:x[1], reverse=True)[:16]
actual_teams = [team for team, _ in sorted_teams]
print(simulate_round(actual_teams, actual_ratings))

def simulate_tournament(teams, ratings):
    while (len(teams)>1):
        teams = simulate_round(teams, ratings)
        print(teams)
    return teams[0]
print(simulate_tournament(actual_teams, actual_ratings))

results = Counter()

for i in range(10000):
    winner = simulate_tournament(actual_teams, actual_ratings)
    results[winner] += 1
print(results)
