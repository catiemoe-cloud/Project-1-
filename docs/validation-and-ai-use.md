# Validation and AI Use — Project 1 Working Source

## Decision, version, and as-of boundary

- **Decision/user:** Watch/defer Apple for a buy-side investment committee with no current position.
- **Source cut-off:** September 17, 2026 for market-price comparison; FY2025 audited statements for opening balances; Q3 FY2026 Form 10-Q for the bridge.
- **Environment:** Python standard library only; Python 3.9+ documented in README.
- **Repository:** https://github.com/catiemoe-cloud/Project-1-

## Validation register

| Claim/output | Failure mode | Test / expected result | Actual result | Disposition | Evidence |
|---|---|---|---|---|---|
| Three-statement articulation | DCF may calculate while balance sheet/cash do not tie | Run `python3 apple_fcff_model.py`; every gap/tie must be 0.00 | FY2026E–FY2030E each printed 0.00 | Pass | `apple_fcff_model.py`; `docs/cold-run.md` |
| FCFF calculation | Financing could leak into unlevered cash flow | Inspect NOPAT + D&A − capex − change NWC | Financing/capital return excluded from FCFF | Pass | `apple_fcff_model.py` |
| Enterprise-to-equity bridge | Cash/debt could be omitted or double counted | EV + $146,517M − $84,344M, divided by 14,594.18M shares | Base EV $1,858,503.5M; equity $1,920,676.5M; $131.61/share | Pass | `analysis.py`; Q3 FY2026 10-Q |
| Product guardrails | Incoherent inputs could show a false value | Render with WACC 5%; expected error | Returned “Input check failed” | Pass | `app.py`; `docs/cold-run.md` |
| Known answer | Code change could silently alter base case | Base model must return $131.61/share | Returned $131.61/share | Pass | `visible_output.json` |
| Published training known answer | DCF mechanics could be wrong despite an Apple output | Week 3 case must return $27.50/share; 11% WACC probe about $23.41 | $27.50 and $23.41 | Pass | `apple_fcff_model.py`; Week 3 worked example |
| DCF monotonicity and boundary | Sensitivity could move in the wrong direction or value an invalid terminal rate | WACC up must reduce value; terminal growth up must increase value; every grid cell has g < WACC | Passed; 8%–10% WACC and 2.0%–3.0% g grid | Pass | `apple_fcff_model.py`; `visible_output.json` |
| WACC component build | Discount rate could be an unsupported scalar | Recompute CAPM/market-value build from dated risk-free rate, beta, ERP, debt cost, tax rate, and capital weights | 9.45% calculated; 9.0% model input remains within the documented 0.5 percentage-point whole-percent rounding band | Pass, with limitation | `docs/wacc-build.md`; `apple_fcff_model.py` |
| Equity multiple | Peer P/E could be inconsistent | Manual MSFT check: $497.75 ÷ $17.95 | 27.729805x | Pass | `peer_valuation.py` |
| EV multiple | EV/revenue could mix definitions | Alphabet EV = price × shares − cash/securities + debt | $4,340,432.26M / $402,836M = 10.774688x | Pass with comparability limitation | `peer-policy.md` |
| README-only cold run | Hidden dependencies/steps | Fresh directory; execute documented commands | First attempt passed in under one second | Pass | `docs/cold-run.md` |

## Locked Changed-Input Record

The prediction below was supplied by the student. The baseline commit was created after that prediction timestamp and immediately before the run; this timing is disclosed rather than backdated.

- **Human AI-off prediction, written before changing the input:** Before changing the model, I predict that increasing annual revenue growth from 6.0% to 9.0%, while keeping all other factors the same, will increase Apple’s projected revenue, EBIT, FCFF, and DCF value per share. However, I do not think this will change my recommendation because the original valuation is still much lower than the current market price of $337.00.
- **Prediction timestamp:** October 9, 2026, 1:43 PM ET. I wrote the prediction on that date but did not create the baseline Git commit until October 16, 2026.
- **Baseline commit:** `0ba92e5`, created October 16, 2026, immediately before the changed-input run. It corroborates the run state but does not represent an October 9 pre-run commit.
- **Changed input:** Revenue growth, old 6.0%, new 9.0%; units: annual percentage of prior-year revenue.
- **Expected direction:** Higher revenue growth should increase forecast FCFF and value per share, holding all other model inputs fixed.
- **Run command:** `python3 apple_fcff_model.py` after making the one input change, or use the product’s 9.0% revenue-growth control and press “Run valuation.”
- **Actual result:** Base value was $131.61/share. With only revenue growth changed to 9.0%, the value increased to $148.85/share. FY2026E revenue / EBIT / FCFF increased from $441,130.66M / $131,195.01M / $107,528.53M to $453,615.49M / $135,190.16M / $110,805.83M. FY2030E revenue / EBIT / FCFF increased from $556,917.29M / $165,448.90M / $135,781.38M to $640,315.28M / $191,414.74M / $156,318.22M. Base and changed cases passed every balance-sheet and cash-flow articulation check.
- **Decision effect:** Watch/defer did not change because the changed value, $148.85/share, remained below the $337.00 market price.
- **Diagnosis:** Higher revenue growth increased forecast revenue. With gross margin, operating expenses, capex, WACC, and terminal growth held fixed, the higher revenue path increased EBIT and FCFF; discounting that larger FCFF stream increased enterprise value and value per share.

The changed-input record is complete. Freeze the PDF only after confirming that the Markdown and PDF match exactly.

## Named AI-use register

| Tool / surface | Interaction date | Material task | Independent check | Disposition |
|---|---|---|---|---|
| Codex / generative AI | Oct. 2026 | Organized documentation, reviewed requirements, and assisted with code drafting and source reconciliation. | The model has executable checks, primary-filing links, and a cold run; student remains responsible for assumptions and final locked prediction. | Disclosed development aid. |

## Limitations and kill rule

Do not rely on the valuation if the source cut-off, bridge convention, base-case assumptions, or articulation checks cannot be reproduced. The forecast aggregates operating assets and liabilities instead of forecasting every Apple line item. The market-multiple work is a non-averaged cross-check, not proof that the DCF result is correct.
