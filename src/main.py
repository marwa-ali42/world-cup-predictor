import pandas as pd
from model.elo import run_elo
from evaluation.evaluate_elo import evaluate_elo_predictions

df = pd.read_csv('data/processed/clean_results.csv')

# Sort matches by date to ensure chronological processing    
df = df.sort_values("date")
# Split data into training and testing sets
split_idx = int(len(df) * 0.8)
train_df = df.iloc[:split_idx]
test_df = df.iloc[split_idx:]
# Calculate ELO ratings using the training set
ratings = run_elo(train_df)
sorted_ratings = sorted(ratings.items(), key=lambda x: x[1], reverse=True)
for team, rating in sorted_ratings[:10]:
    print(f"{team}: {rating:.2f}")

#Evaluate ELO predictions on the test set
accuracy = evaluate_elo_predictions(test_df, ratings)
print(f"ELO Prediction Accuracy: {accuracy:.2%}")
