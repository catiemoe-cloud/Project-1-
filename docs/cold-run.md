# README-Only Cold-Run Record

**Run date:** October 16, 2026, America/New_York  
**Repository state:** uncommitted working tree during final-model rebuild  
**Environment:** fresh temporary directory; macOS system Python 3.9; no packages installed or network access required.

## Procedure and result

1. Copied only `README.md`, `apple_fcff_model.py`, `analysis.py`, `peer_valuation.py`, and `app.py` into a fresh directory.
2. Ran the four README commands and the workbench render checks.
3. Result: **pass on first attempt**; elapsed time was less than one second (shell display rounded to 0 seconds).

| Command / check | Result | Evidence |
|---|---|---|
| `python3 -B apple_fcff_model.py` | Pass | FY2026E–FY2030E balance-sheet gaps and cash-flow ties each printed 0.00; base value $131.61/share. |
| `python3 -B analysis.py` | Pass | Regenerated `visible_output.json` from the final FCFF engine. |
| `python3 -B peer_valuation.py` | Pass | P/E cross-check and Alphabet EV/revenue evidence printed. |
| `app.render({})` | Pass | Rendered base workbench, including $131.61/share output. |
| `app.render({'wacc': ['5']})` | Pass | Returned visible “Input check failed” rather than a valuation. |

## First failure and repair

No runtime failure occurred in the cold run. Before this record, source review caught a model-opening balance mismatch caused by double-counting the current portion of intangible assets in aggregated operating assets; the model stopped with a balance-sheet assertion. The opening operating-assets aggregate was corrected from $179,195M to $176,987M, which reconciles to Apple’s FY2025 reported total assets. The check now fails loudly if a balance sheet does not balance.

## Highest-risk test

The highest-risk test is the **FCFF articulation test**: each forecast year must have both a zero balance-sheet gap and a zero cash-flow tie. This addresses the risk that a DCF appears to calculate while statements do not actually articulate. The base run passed every year. The separate invalid-WACC test verifies that the product rejects an incoherent terminal-growth/WACC relationship instead of showing a false valuation.
