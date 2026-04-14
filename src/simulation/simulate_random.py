# Simulates a match between two teams based on their Elo ratings,
# ignoring real world cup brackets and matchups.
# This is used to test the model's predictive power in a controlled environment.
import random
import pandas as pd
from src.model.elo import expected_score

# Simulate match outcome based on expected score
# Factors in real world randomness and upsets
def simulate_match(team_a, team_b, ratings):
    rating_a = ratings.get(team_a, 1500)
    rating_b = ratings.get(team_b, 1500)
    expected_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

    outcome = random.random()
    if outcome < expected_a:
        return team_a
    else:
        return team_b

def simulate_n_matches(team_a, team_b, ratings, n=1000):
    results = {team_a: 0, team_b: 0}
    for _ in range(n):
        winner = simulate_match(team_a, team_b, ratings)
        results[winner] += 1
    results[team_a] /= n
    results[team_b] /= n
    return results
