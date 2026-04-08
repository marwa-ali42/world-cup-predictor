# Calculates expected score of a match based on ELO ratings
def expected_score(rating_a, rating_b):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

# Updates ELO ratings based on match result
def update_elo_ratings(rating_home, rating_away, score_home, k=32):
    expected_home = expected_score(rating_home, rating_away)
    expected_away = expected_score(rating_away, rating_home)

    new_rating_home = rating_home + k * (score_home - expected_home)
    new_rating_away = rating_away + k * ((1 - score_home) - expected_away)

    return new_rating_home, new_rating_away

# Main function to run ELO rating calculations
def run_elo(df):
    # Sort matches by date to ensure chronological processing
    df = df.sort_values('date')
    # Initialize ratings for all teams
    teams = set(df['home_team']).union(set(df['away_team']))
    ratings = {team: 1500 for team in teams}

    for _, row in df.iterrows():
        home_team = row['home_team']
        away_team = row['away_team']
        home_score = row['home_score']
        away_score = row['away_score']

        # Set score for home team: 1 for win, 0 for loss, 0.5 for draw
        if home_score > away_score:
            score_home = 1
        elif home_score < away_score:
            score_home = 0
        else:
            score_home = 0.5

        # Update ELO ratings based on match result
        ratings[home_team], ratings[away_team] = update_elo_ratings(
            ratings[home_team], ratings[away_team], score_home)

    return ratings
