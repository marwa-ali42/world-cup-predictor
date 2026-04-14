import pandas as pd
from src.simulation.simulate_random import simulate_match
from src.model.elo import run_elo
from collections import Counter

df = pd.read_csv('data/processed/clean_results.csv')
df = df.sort_values("date")
actual_ratings = run_elo(df)

def simulate_round(teams, ratings):
    winners = []
    no_of_teams = len(teams)
    for i in range(0, no_of_teams//2):
        winner = simulate_match(teams[i], teams[no_of_teams-i-1], ratings)
        winners.append(winner)
    return winners

def seed_teams():
    sorted_teams = sorted(actual_ratings.items(), key= lambda x:x[1], reverse=True)[:16]
    return sorted_teams

actual_teams = [team for team, _ in seed_teams()]
print(f"Simulating a round gives results: {simulate_round(actual_teams, actual_ratings)}")

def simulate_tournament(teams, ratings):
    while (len(teams)>1):
        teams = simulate_round(teams, ratings)
        # print(teams)
    return teams[0]
print(f"Simulating a tournament gives result: {simulate_tournament(actual_teams, actual_ratings)}")

results = Counter()

number_of_tournaments = 10000
for i in range(number_of_tournaments):
    winner = simulate_tournament(actual_teams.copy(), actual_ratings)
    results[winner] += 1
print(f"Simulating {number_of_tournaments} tournaments gives result: {results}")

print(f"For each team, probability of winning the world cup, calculated using {number_of_tournaments} simulations, is: ")
for team, count in sorted(results.items(), key=lambda x:x[1], reverse=True):
    print(f"{team}: {count/number_of_tournaments *100}%")
