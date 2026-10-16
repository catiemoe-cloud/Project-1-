# Apple Project 1 — Corporate Finance Application

## Finance decision and intended user

This project supports a buy-side investment committee deciding whether to initiate Apple (AAPL). The current, interim recommendation is **watch/defer** as of September 17, 2026: the recorded market price is $337.00 per share versus a base FCFF DCF result of approximately $224.42 per share. This is educational work, not investment advice.

## Visible result

Run `python3 analysis.py` to create `visible_output.json`. That frozen artifact exposes the as-of date, material DCF inputs, valuation result, decision, and limitations without requiring a grader to run the model.

## Setup and run

Requires Python 3.10+ and no third-party packages.

```bash
python3 dcf.py
python3 analysis.py
python3 apple_proforma.py
python3 apple_lab10_sensitivity.py --run
```

`peer_valuation.py` now runs the interim Microsoft/Alphabet P/E cross-check. It remains provisional and cannot be final evidence until the peer-selection policy is frozen and the required EV and equity-value multiples are added.

## Repository map

- `analysis.py` — generates the visible-output artifact from the FCFF DCF inputs.
- `dcf.py` — current FCFF DCF, WACC–growth grid, and reverse-DCF calculation.
- `apple_proforma.py` / `apple_lab10_sensitivity.py` — prior Apple pro-forma and one-at-a-time sensitivity work; currently FCFE-based and therefore not the final required FCFF engine.
- `project-1-edition-a.*` — preserved Edition A baseline.
- `project-1-edition-b.md` — working research-evolution brief.
- `docs/` — final-submission documentation in progress.
- `sources.md` — running source log.

## Data sources and point-in-time boundary

The current DCF evidence uses Apple’s Q3 FY2026 Form 10-Q for the June 27, 2026 financial position and September 17, 2026 market inputs documented in `AAPL_reverseDCF_9-10-26.md` and `AAPL_peer_comparison_2026-09-10.md`. Use only public information available by each displayed as-of date.

## Known limitations and required next work

This repository is **not final-submission ready**. It needs: an articulating five-year three-statement pro-forma producing FCFF; filing-based starting-FCFF and WACC support; normalization documentation; final bridge policy; predeclared peer policy plus EV and equity multiples; a semi-adjustable interface; the final locked changed-input record; and a clean-environment cold run. See `project-1-requirements-audit.md`.

## Security

No credentials are required. Do not commit `.env`, API keys, tokens, passwords, private data, or student-identifying data.

