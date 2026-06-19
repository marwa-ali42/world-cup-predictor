import pandas as pd

raw_data = pd.read_csv('~/projects/world-cup-predictor/data/raw/results.csv')

filtered_data = raw_data[raw_data['date'] >= '2016-01-01']
filtered_data = filtered_data[filtered_data['date'] < '2026-06-11']
filtered_data = filtered_data.dropna(subset=['home_score', 'away_score'], how='any')
filtered_data = filtered_data[['date', 'tournament', 'home_team', 'away_team',
                               'home_score', 'away_score', 'neutral']]
print(filtered_data.head())
print(filtered_data.shape)
print(filtered_data.tail())

filtered_data.to_csv('~/projects/world-cup-predictor/data/processed/clean_results.csv', index=False)
