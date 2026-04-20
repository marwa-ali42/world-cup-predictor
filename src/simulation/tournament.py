import pandas as pd
from src.simulation.simulate_random import simulate_match
from collections import Counter
from itertools import islice

def simulate_round(teams, ratings):
    winners = []
    no_of_teams = len(teams)
    for i in range(0, no_of_teams//2):
        winner = simulate_match(teams[i], teams[no_of_teams-i-1], ratings)
        winners.append(winner)
    return winners

def seed_teams(sorted_teams):
    seeded_teams = sorted(sorted_teams.items(), key= lambda x:x[1], reverse=True)
    return seeded_teams

def simulate_tournament(teams, ratings):
    while len(teams)>1 :
        teams = simulate_round(teams, ratings)
    return teams[0]

def run_monte_carlo(top_teams, ratings, number_of_tournaments = 10000):
    results = Counter()

    for _ in range(number_of_tournaments):
        winner = simulate_tournament(top_teams, ratings)
        results[winner] += 1
    print(f"Simulating {number_of_tournaments} tournaments gives result: {results}")

    print("For each team, probability of winning the world cup, "
          f"calculated using {number_of_tournaments} simulations, is: ")
    for team, count in sorted(results.items(), key=lambda x:x[1], reverse=True):
        print(f"{team}: {100*(count/number_of_tournaments):.2f}%")
