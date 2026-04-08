from math import sqrt

# Home team advantage in ELO points
HOME_ADVANTAGE = 100

# Calculates expected score of a match based on ELO ratings
def expected_score(rating_a, rating_b):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

# Determines K-factor based on tournament type
def get_k(tournament):
    if "FIFA World Cup qualification" in tournament:
        return 30
    elif "FIFA World Cup" in tournament:
        return 60
    elif "Friendly" in tournament:
        return 25
    elif "UEFA Euro qualification" in tournament:
        return 40
    elif "African Cup of Nations" in tournament:
        return 20
    else:
        return 10

# Updates ELO ratings based on match result
def update_elo_ratings(rating_home, rating_away, home_score, away_score, k=32, advantage=0):
    goal_diff = abs(home_score - away_score)
    multiplier = 1 if goal_diff == 0 else sqrt(goal_diff)
    k *= multiplier

    expected_home = expected_score(rating_home + advantage, rating_away)
    expected_away = expected_score(rating_away, rating_home + advantage)

    new_rating_home = rating_home + k * (home_score - expected_home)
    new_rating_away = rating_away + k * (away_score - expected_away)

    return new_rating_home, new_rating_away

# Main function to run ELO rating calculations
def run_elo(df):
    # Sort matches by date to ensure chronological processing    
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

        # Calculate home team advantage
        advantage = 0 if row['neutral'] else HOME_ADVANTAGE
 
        # Update ELO ratings based on match result
        ratings[home_team], ratings[away_team] = update_elo_ratings(
            ratings[home_team], ratings[away_team], home_score, away_score, get_k(row['tournament']), advantage)

    return ratings

def predict_match(team_a, team_b, ratings):
    rating_a = ratings.get(team_a, 1500)
    rating_b = ratings.get(team_b, 1500)
    expected_a = expected_score(rating_a, rating_b)

    if abs(expected_a - 0.5) < 0.05:  # If the match is expected to be close
        return "Draw"
    elif expected_a > 0.5:
        return team_a
    else:
        return team_b
