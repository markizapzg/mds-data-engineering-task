# Bonus – Tournament Scheduling

This bonus provides a simple heuristic solution to the tournament scheduling problem.

## Approach

- Players are randomly shuffled each round.
- All tables are always used.
- Winners are selected per table.
- A history of player pairings is tracked to maximize diversity of opponents,
  especially for non winning players.

## Notes

The solution is heuristic and prioritizes clarity and extensibility
over optimality.
