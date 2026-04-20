# World Cup Predictor
Predicts and simulates the 2026 FIFA World Cup using historical international tournament outcomes and probabilistic models.

## Overview
This project uses an Elo rating system to model team strength based on past results.
It then simulates matches and full tournaments to estimate how likely each team is to win.

Instead of predicting a single outcome, the tournament is simulated many times and the results are aggregated into probabilities.


## Models
- **Baseline model** 
  Ranks teams using historical win counts as a simple benchmark.
- **Elo model** 
  A dynamic rating system that updates team strength over time using
  - match results
  - expected outcomes
  - goal differences
  - match importance (k-factor)

## Simulation
- Elo ratings are trained and evaluated on a training-test data split
- For tournament simulation, ratings are recomputed using the full dataset
- Match outcomes are sampled using Elo-derived probabilities
- A knockout tournament is simulated round-by-round
- The full tournament is ran repeatedly (Monte Carlo simulation)
- Results are aggregated into win probabilities

Example output:

```text
Spain: 21.34%
Argentina: 12.92%
Morocco: 12.59%
France: 10.44%
Senegal: 6.79%
Japan: 6.35%
Portugal: 3.86%
England: 3.86%
Algeria: 3.66%
Nigeria: 3.24%
Germany: 3.11%
Ecuador: 2.65%
Netherlands: 2.61%
Brazil: 2.24%
Australia: 2.24%
Turkey: 2.10%
```
## To run

```bash
python -m src.main
```
