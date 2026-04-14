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
- Match outcomes are sampled using Elo-derived probabilities
- A knockout tournament is simulated round-by-round
- The full tournament is ran repeatedly (Monte Carlo simulation)
- Results are aggregated into win probabilities

Example output:

```text
Spain: 20.41%
Morocco: 13.200000000000001%
Argentina: 13.15%
France: 10.36%
Senegal: 6.72%
Japan: 6.54%
Portugal: 4.03%
Nigeria: 3.61%
England: 3.55%
Algeria: 3.4099999999999997%
Germany: 3.0700000000000003%
Ecuador: 2.65%
Netherlands: 2.64%
Brazil: 2.63%
Australia: 2.34%
Turkey: 1.69%
```
## To run

```bash
python -m src.simulation.tournament
```
