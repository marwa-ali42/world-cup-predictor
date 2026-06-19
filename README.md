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


Final 2026 World Cup ranking:

```text
Spain: 18.36%
Argentina: 13.82%
Morocco: 12.14%
France: 7.10%
Japan: 6.40%
Portugal: 5.36%
Algeria: 5.27%
England: 4.39%
Brazil: 4.18%
Mexico: 3.81%
Senegal: 3.75%
Ecuador: 3.52%
Germany: 3.49%
Nigeria: 3.01%
Colombia: 2.81%
Turkey: 2.59%
```
## To run

```bash
python -m src.main
```
