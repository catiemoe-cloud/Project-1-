# Apple Project 1 — FCFF Valuation Workbench

## Decision and intended user

This locally runnable workbench supports a buy-side investment committee deciding whether to initiate Apple (AAPL). As of **September 17, 2026**, the base FCFF case indicates **watch/defer**: $131.61 per share versus the recorded $337.00 market price. This is educational analysis, not investment advice.

## Setup and run

Python 3.9+ is required; there are no third-party dependencies or credentials.

```bash
python3 apple_fcff_model.py
python3 analysis.py
python3 peer_valuation.py
python3 app.py
```

Open `http://127.0.0.1:8000` after starting `app.py`. The app has bounded operating/valuation controls, a base reset, causal cases, and visible balance-sheet/cash-flow checks. An incoherent input fails visibly rather than returning a number.

`python3 analysis.py` regenerates `visible_output.json`, the executed-output artifact. The app and model use USD millions except rates and per-share values.

## Finance method

`apple_fcff_model.py` starts with Apple FY2025 audited financial statements, forecasts FY2026–FY2030 income statement, operating balance sheet, and cash flow, and derives FCFF from NOPAT + D&A − capex − change in operating net working capital. The model checks that each forecast balance sheet balances and that cash flow ties to the balance-sheet cash change.

The enterprise-to-equity bridge uses the Q3 FY2026 Form 10-Q: add $146,517M of cash plus marketable securities; subtract $84,344M of commercial paper plus term debt; divide by 14,594.18M shares outstanding. Operating lease liabilities remain in operating liabilities, so they are not double counted as debt. The base case uses 6% revenue growth, 47.0% gross margin, 15.0% operating expense / revenue, 3.0% capex / revenue, 9.0% WACC, and 2.5% terminal growth. The 9.0% model input is the nearest whole-percent representation of a dated 9.45% component calculation; see `docs/wacc-build.md`. Forecast assumptions remain distinct from reported facts.

The engine also prints causal low/base/high cases, a 3×3 WACC–terminal-growth grid, terminal-value share, a reverse-DCF search, the published Week 3 training-case reconciliation, and monotonicity/bridge checks. See `docs/assumption-challenge-record.md` for the base-year contamination catalog, every load-bearing driver, its basis, challenge, and evidence that would change it.

## Repository map

The runnable final path is the four commands in **Setup and run** and the files listed below. Dated top-level lab and working files are retained only as traceable development history; they are not final valuation evidence and must not be used in place of `apple_fcff_model.py`, `visible_output.json`, or the `docs/` final artifacts.

- `apple_fcff_model.py` — final three-statement FCFF engine, cases, bridge, and checks.
- `app.py` — semi-adjustable local analyst product used for the live demo.
- `analysis.py` / `visible_output.json` — visible executed output.
- `peer_valuation.py` and `peer-policy.md` — peer policy and market cross-check.
- `docs/assumption-challenge-record.md` — normalization, driver basis, and challenge record.
- `docs/` — research evolution, decision memo, validation/AI-use record, and video transcripts.
- `sources.md` — source log; `apple-2025-10k-filing-facts.md` — filing-based company research.

## Data sources and limitations

The historical opening balance sheet and operating data are from Apple’s FY2025 Form 10-K. The valuation-date bridge and shares are from Apple’s Q3 FY2026 Form 10-Q (June 27, 2026); the recorded price is September 17, 2026. See `sources.md`, `apple_fcff_model.py`, and `peer-policy.md` for links and treatment.

This is a simplified aggregate three-statement forecast: operating assets and liabilities are forecast as ratios of revenue and residual cash return is presented as financing/capital return. It does not forecast every Apple line item or claim a price target. The comparable-company result is a cross-check, not an averaged valuation, and its comparability limitations remain disclosed.

## Security

No credentials are required. `.env.example` is intentionally empty. Do not commit passwords, tokens, API keys, private data, or `.env` files.
