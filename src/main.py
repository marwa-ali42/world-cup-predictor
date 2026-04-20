import pandas as pd
from src.model.elo import run_elo
from src.evaluation.evaluate_elo import evaluate_elo_predictions
from src.simulation.tournament import run_monte_carlo, seed_teams
from itertools import islice

number_of_teams = 16
number_of_tournaments = 10000

df = pd.read_csv('data/processed/clean_results.csv')

# Sort matches by date to ensure chronological processing
df = df.sort_values("date")
# Split data into training and testing sets
split_idx = int(len(df) * 0.8)
train_df = df.iloc[:split_idx]
test_df = df.iloc[split_idx:]
# Calculate ELO ratings using the training set
ratings_training = run_elo(train_df)
sorted_ratings_training = sorted(ratings_training.items(), key=lambda x: x[1], reverse=True)
for team, rating in sorted_ratings_training[:number_of_teams]:
    print(f"{team}: {rating:.2f}")

# Evaluate ELO predictions on the test set
accuracy = evaluate_elo_predictions(test_df, ratings_training)
print(f"ELO Prediction Accuracy: {accuracy:.2%}")

# Simulate World Cup tournament 10000 times
full_ratings = run_elo(df)
top_teams = [team for team, _ in seed_teams(full_ratings)[:number_of_teams]]
run_monte_carlo(top_teams, full_ratings, number_of_tournaments)
