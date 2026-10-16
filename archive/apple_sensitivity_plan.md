# Apple Sensitivity Plan

All money amounts are USD millions unless noted. The model uses FCFE consistently.

| Driver | Base | Lower case | Higher case | Units and years | Range reason |
|---|---:|---:|---:|---|---|
| Revenue growth | 5.0% | 3.0% | 7.0% | Annual growth rate in FY2026E–FY2030E; replace the same input in every year | Reported Apple revenue growth was -2.8%, 2.0%, and 6.4% in FY2023–FY2025. The range tests a slower demand environment versus growth near the latest rebound. |
| Gross margin | 46.5% | 45.5% | 47.5% | Percent of revenue in FY2026E–FY2030E; a -1.0 or +1.0 percentage-point shift in every year | FY2023–FY2025 gross margin ranged from 44.13% to 46.91%. The range tests product mix, costs, tariffs, and Services mix without changing revenue growth. |

Each run changes only one independent input and holds every other assumption at its base value.

## Comparable outputs

Use the same outputs for every case:

- FY2030E operating income, USD millions
- FY2030E FCFE, USD millions
- Value per share, USD

Base-case outputs from `apple_proforma.py`: FY2030E operating income $200,169.0M, FY2030E FCFE $156,119.3M, and value per share $190.41.

## Locked Changed-Input Record

**Timestamp:** 2026-09-29 14:00 EDT

**Input to change after partner review:** Revenue growth, 5.0% to 3.0%, a 2.0 percentage-point reduction applied to each of FY2026E–FY2030E.

**Prediction before running:** FY2030E operating income, FY2030E FCFE, and value per share will all fall by roughly 8%–12%, because lower annual sales compound for five years while the margin and all other inputs remain unchanged.

**Partner check:** Confirm that revenue growth is a percentage rate, not a dollar change; that the 2.0 percentage-point reduction applies to all five forecast years; and that gross margin and every other input stay at base case for this run.

**Partner confirmation:** Confirmed. Revenue growth is the only changed input, and the percentage-point change applies to FY2026E–FY2030E.

## Revenue-Growth Results

All cases hold every non-growth input at base case. FY2030E FCFE is the model's equity cash flow measure.

| Revenue-growth path, FY2026E–FY2030E | FY2030E operating income, $M | FY2030E FCFE, $M | Value per share, $ |
|---|---:|---:|---:|
| 3.0% each year | 180,696.3 | 140,307.3 | 173.12 |
| 5.0% each year — base | 200,169.0 | 156,119.3 | 190.41 |
| 7.0% each year | 221,183.3 | 173,172.5 | 209.00 |

The locked 5.0% to 3.0% prediction was directionally correct: value per share fell about 9%, FY2030E operating income about 10%, and FY2030E FCFE about 10%.

## Locked Changed-Input Record — Gross Margin

**Timestamp:** 2026-09-29 14:09 EDT

**Input to change after partner review:** Gross margin, 46.5% to 45.5% or 47.5%, a -1.0 or +1.0 percentage-point shift applied to each of FY2026E–FY2030E.

**Prediction before running:** A 1.0 percentage-point decrease in gross margin will reduce FY2030E operating income by about $4.5bn, reduce FCFE, and lower value per share, because less of every revenue dollar becomes gross profit. The higher case will have the opposite effect.

**Partner check needed:** Confirm that this is a percentage-point shift, not a 1% percent change; that it applies to all five forecast years; and that revenue growth remains at 5.0% with every other input unchanged.
