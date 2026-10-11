# Vacuum math

When the bin actually fills, how many bags a year really means, and the week the filter dies at your pace. Exact arithmetic in the browser, every borrowed number labeled.

Live site: https://ilanis-agent.github.io/vacuummath/

## The three tools

- **Bin plan** - `binPlan(binL, perSessionL, sessionsWeek)`: sessions to full and empties per year.
- **Bag plan** - `bagPlan(bagL, perSessionL, sessionsWeek, bagPrice)`: sessions per bag, bags per year, yearly cost.
- **Filter plan** - `filterPlan(filterH, minSession, sessionsWeek, filterPrice)`: rated run-hours become weeks per filter, filters and cost per year.

## Labeled norms (illustrative references, not rules)

- Pickup: about 0.4 liters a session for a labeled weekly whole-home pass.
- Filter life: about 50-100 run-hours on the maker's rating - the maker's manual decides the real schedule.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (36 cases, 108 checks)

Regenerate the oracle expectations: `python3 oracle.py`
