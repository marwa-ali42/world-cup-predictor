# Simulates a match between two teams based on their Elo ratings,
# ignoring real world cup brackets and matchups.
# This is used to test the model's predictive power in a controlled environment.
import random
import pandas as pd
from model.elo import expected_score, run_elo

df = pd.read_csv('data/processed/clean_results.csv')
df = df.sort_values("date")
ratings = run_elo(df)

def simulate_match(team_a, team_b, ratings):
    rating_a = ratings.get(team_a, 1500)
    rating_b = ratings.get(team_b, 1500)
    expected_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

    # Simulate match outcome based on expected score
    outcome = random.random()
    if outcome < expected_a:
        return team_a
    else:
        return team_b
    
# def simulate_round(teams, ratings):
    
# def simulate_tournament(teams, ratings):

for _ in range(10):
    print(simulate_match("France", "Brazil", ratings))

print(ratings.get("France", 1500), ratings.get("Brazil", 1500))
print(min(ratings.values()), max(ratings.values()))