from model.elo import predict_match

def evaluate_elo_predictions(df, ratings):
    correct, total = 0, 0
    for _, row in df.iterrows():
        home_team = row['home_team']
        away_team = row['away_team']
        prediction = predict_match(home_team, away_team, ratings)
        actual = ("Draw" if row['home_score'] == row['away_score']
                else home_team if row['home_score'] > row['away_score']
                else away_team)
        if prediction == actual:
            correct += 1
        total += 1

    accuracy = correct / total
    return accuracy