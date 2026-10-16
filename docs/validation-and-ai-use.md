# Validation and AI Use — Project 1 Working Source

## Decision, version, and as-of boundary

- **Decision/user:** Watch/defer Apple for a buy-side investment committee with no current position.
- **Source cut-off:** September 17, 2026 for market-price comparison; FY2025 audited statements for opening balances; Q3 FY2026 Form 10-Q for the bridge.
- **Environment:** Python standard library only; Python 3.10+ documented in README.
- **Repository:** https://github.com/catiemoe-cloud/Project-1-

## Validation register

| Claim/output | Failure mode | Test / expected result | Actual result | Disposition | Evidence |
|---|---|---|---|---|---|
| Three-statement articulation | DCF may calculate while balance sheet/cash do not tie | Run `python3 apple_fcff_model.py`; every gap/tie must be 0.00 | FY2026E–FY2030E each printed 0.00 | Pass | `apple_fcff_model.py`; `docs/cold-run.md` |
| FCFF calculation | Financing could leak into unlevered cash flow | Inspect NOPAT + D&A − capex − change NWC | Financing/capital return excluded from FCFF | Pass | `apple_fcff_model.py` |
| Enterprise-to-equity bridge | Cash/debt could be omitted or double counted | EV + $146,517M − $84,344M, divided by 14,594.18M shares | Base EV $1,858,503.5M; equity $1,920,676.5M; $131.61/share | Pass | `analysis.py`; Q3 FY2026 10-Q |
| Product guardrails | Incoherent inputs could show a false value | Render with WACC 5%; expected error | Returned “Input check failed” | Pass | `app.py`; `docs/cold-run.md` |
| Known answer | Code change could silently alter base case | Base model must return $131.61/share | Returned $131.61/share | Pass | `visible_output.json` |
| Equity multiple | Peer P/E could be inconsistent | Manual MSFT check: $497.75 ÷ $17.95 | 27.729805x | Pass | `peer_valuation.py` |
| EV multiple | EV/revenue could mix definitions | Alphabet EV = price × shares − cash/securities + debt | $4,340,432.26M / $402,836M = 10.774688x | Pass with comparability limitation | `peer-policy.md` |
| README-only cold run | Hidden dependencies/steps | Fresh directory; execute documented commands | First attempt passed in under one second | Pass | `docs/cold-run.md` |

## Locked Changed-Input Record — requires student completion

I cannot truthfully create the required **human-authored, AI-off pre-run prediction** or claim a commit was made before it. Complete the two bracketed lines yourself immediately before the recorded change; then run the stated command, save the output, commit it, and replace the brackets.

- **Human AI-off prediction, written before changing the input:** Before changing the model, I predict that increasing annual revenue growth from 6.0% to 9.0%, while keeping all other factors the same, will increase Apple’s projected revenue, EBIT, FCFF, and DCF value per share. However, I do not think this will change my recommendation because the original valuation is still much lower than the current market price of $337.00.
- **Prediction timestamp:** October 9, 2026, 1:43 PM ET.
- **Baseline commit:** Created after the prediction timestamp, immediately before the changed-input run; commit identifier recorded below after creation. This commit timing does not represent an October 9 pre-run commit.
- **Changed input:** Revenue growth, old 6.0%, new 9.0%; units: annual percentage of prior-year revenue.
- **Expected direction:** Higher revenue growth should increase forecast FCFF and value per share, holding all other model inputs fixed.
- **Run command:** `python3 apple_fcff_model.py` after making the one input change, or use the product’s 9.0% revenue-growth control and press “Run valuation.”
- **Actual result:** [record the exact displayed base and changed values from your run]
- **Decision effect:** [state whether watch/defer changes; do not state it changed unless the recorded output supports it]
- **Diagnosis:** [briefly explain the causal link from revenue through EBIT, FCFF, and DCF value]

This is the only remaining student-authorship block in the validation record. Do not freeze the PDF until those fields are completed and the Markdown and PDF match.

## Named AI-use register

| Tool / surface | Interaction date | Material task | Independent check | Disposition |
|---|---|---|---|---|
| Codex / generative AI | Oct. 2026 | Organized documentation, reviewed requirements, and assisted with code drafting and source reconciliation. | The model has executable checks, primary-filing links, and a cold run; student remains responsible for assumptions and final locked prediction. | Disclosed development aid. |

## Limitations and kill rule

Do not rely on the valuation if the source cut-off, bridge convention, base-case assumptions, or articulation checks cannot be reproduced. The forecast aggregates operating assets and liabilities instead of forecasting every Apple line item. The market-multiple work is a non-averaged cross-check, not proof that the DCF result is correct.
