# Project 1 — Edition B: Research Evolution and Current Position

**Company:** Apple Inc. (NASDAQ: AAPL)  
**Original Edition A valuation date:** September 1, 2026  
**Current research cut-off:** September 17, 2026  
**Intended user:** Buy-side investment committee with no current Apple position  
**Current action:** **Watch / defer; do not initiate at $337.00 per share.**

> **Status:** This is a working Edition B, prepared after Edition A. It does not alter or replace `project-1-edition-a.md` or its submitted PDF. It records research completed after Edition A and must be combined with the unchanged Edition A in the final `Research-Evolution.pdf`.

## Current decision

I recommend that the committee **watch/defer** Apple rather than initiate a position at the September 17, 2026 closing price of **$337.00**. The current FCFF DCF estimates **$224.42 per diluted share** under a 7% five-year FCFF-growth path, 8% WACC, and 3% terminal growth. A limited, explicitly provisional P/E cross-check using Microsoft and Alphabet implies **$206.86–$239.69** per Apple share, with a $223.28 median. I do not average these methods: they answer different questions and the peer set has material business-model limitations.

This is not a claim that the market is wrong. Under the current reverse-DCF framing, the September 17 price requires substantially faster explicit cash-flow growth than the 7% base case. The recommendation changes only if the committee obtains evidence that supports a more durable cash-flow and margin path, accepts a different but documented valuation convention, or can buy at a price that supplies a margin of safety against the valuation range.

## A-to-B evidence table

| Item | Edition A | Edition B | Primary driver of change | Evidence or test justifying the change or stability |
|---|---|---|---|---|
| Thesis / recommendation | Watch/defer because valuation relative to price was unknown. | Watch/defer because the current base DCF and provisional peer check are below the observed price. | Own analysis; course instruction; AI-assisted research support. | `AAPL_reverseDCF_9-10-26.md`; `AAPL_peer_comparison_2026-09-10.md`. |
| Data / source choice | FY2025 10-K and Q3 FY2026 10-Q identified as primary evidence. | Added valuation-date prices, FCFF/bridge inputs, peer annual GAAP EPS, and a dated source log. | Own analysis. | `sources.md`; Q3 FY2026 10-Q; price locators cited in the DCF and peer files. |
| Assumption / model design | Planned a five-year forecast and DCF; assumptions were not yet specified. | FCFF DCF uses $131.0B starting FCFF, 7% explicit FCFF growth, 8% WACC, 3% terminal growth, $146.517B cash plus marketable securities, $84.344B debt, and 14.594B shares. | Own analysis; course instruction. | `AAPL_reverseDCF_9-10-26.md`; executable `dcf.py`. |
| Model architecture correction | The existing Apple workbench was described as a valuation model. | The workbench is classified as **FCFE** and cannot be the final Project 1 valuation engine, which must be FCFF. Its sensitivity evidence is retained, but final valuation work must reconcile the pro-forma to FCFF. | Course instruction; own model review. | `apple_proforma.py` labels and calculates FCFE; Project 1 brief requires FCFF. |
| Risk / limitation | Product cycle, China, regulation, supply chain, FX, and valuation inputs remained open questions. | Peer comparability, FCFF starting-point construction, terminal-value dependence, and bridge conventions are identified as specific limitations. | Own analysis; AI-generated skeptical review, independently assessed. | `AAPL_peer_comparison_2026-09-10.md`; `AAPL_reverseDCF_9-10-26.md`; `apple_lab10_sensitivity_output.md`. |

## Current valuation evidence

### FCFF DCF and reverse-DCF result

The FCFF DCF uses a five-year 7% growth path, 8% WACC, and 3% terminal growth. It produces **$224.42 per diluted share**; the terminal value represents **80.17%** of enterprise value. The WACC–terminal-growth grid spans $165.96–$360.32 per share, but this grid alone is not the required causal low/base/high case. The September 17 market price of $337.00 is above this base value. At that price, the reverse DCF indicates that the model needs approximately a **+9.955 percentage-point** uniform increase to each of the five explicit FCFF-growth assumptions, holding the starting FCFF, WACC, terminal growth, non-operating assets, debt, and shares fixed.

The result should be read as a required assumption under this model—not as proof that Apple is overvalued. It is most useful as a diligence question: what evidence supports a cash-flow trajectory materially above the base case?

### Comparable-company cross-check

Microsoft and Alphabet are **qualified leads**, not final peers. Their P/E multiples imply an Apple range of **$206.86–$239.69**, median **$223.28**, using September 17 closing prices and annual GAAP diluted EPS. Microsoft has much higher enterprise software and cloud exposure; Alphabet relies much more heavily on advertising. Their mismatch to Apple’s hardware-led ecosystem is a constraint on the transferability of their multiples, not a reason to adjust the result toward a desired price.

### Sensitivity evidence

The existing workbench’s one-at-a-time sensitivity tests show that, over its chosen ranges, revenue growth is more consequential than gross margin. A 3% versus 7% revenue-growth path changes the workbench’s value-per-share output from **$173.12 to $209.00**, while a 45.5% versus 47.5% gross-margin path changes it from **$185.93 to $194.90**. This ranking is range-dependent and uses FCFE; it is decision evidence about operating-driver exposure, not the final required FCFF valuation result.

## Evidence ledger and current conventions

| Item | Classification | Value / unit | Period / as-of | Primary source or calculation | Treatment and uncertainty |
|---|---|---:|---|---|---|
| AAPL market price | Reported fact | $337.00/share | Sep. 17, 2026 close | Price locator in `AAPL_peer_comparison_2026-09-10.md` | Used for market comparison only; verify the final price-source export before submission. |
| Cash plus marketable securities | Reported fact | $146.517B | Jun. 27, 2026 | Apple Q3 FY2026 Form 10-Q | Included as non-operating assets in the current FCFF DCF; final policy must explain whether every marketable security is excess cash. |
| Commercial paper plus term debt | Reported fact | $84.344B | Jun. 27, 2026 | Apple Q3 FY2026 Form 10-Q | Included in the bridge. Lease policy remains unresolved. |
| Diluted-share convention | Reported fact / convention | 14.594B shares | Jul. 17, 2026 | Apple Q3 FY2026 Form 10-Q cover page | Point-in-time shares are used in the current DCF; final work must disclose the difference from weighted-average diluted shares. |
| Starting FCFF | Forecast assumption / calculated input | $131.0B | TTM estimate as of Sep. 2026 | `AAPL_reverseDCF_9-10-26.md` | Needs a transparent reconciliation from operating cash flow, capex, taxes, and working-capital treatment before final submission. |
| Explicit FCFF growth | Forecast assumption | 7% annually | Years 1–5 | `dcf.py` | Base case only; reverse DCF tests whether price implies a stronger path. |
| WACC | Forecast assumption | 8% | Valuation date | `dcf.py` | Must be rebuilt from documented cost-of-capital inputs for the final model. |
| Terminal growth | Forecast assumption | 3% | Post-Year 5 | `dcf.py` | Sensitive long-run assumption; must remain below WACC and be stress-tested. |
| FCFF DCF value | Calculated output | $224.42/share | Sep. 17, 2026 case | `dcf.py`; `AAPL_reverseDCF_9-10-26.md` | Not an observed price; dependent on the assumptions above. |
| P/E cross-check | Calculated output | $206.86–$239.69/share | Sep. 17, 2026 | `peer_valuation.py`; peer-comparison memo | Provisional because peer policy and comparability remain incomplete. |

## Validation completed and still required

### Completed evidence

- The DCF runs from `python3 dcf.py` and reports its base case, sensitivity grid, and reverse-DCF result.
- The peer P/E calculation includes a manual Microsoft check: $497.75 ÷ $17.95 = 27.729805x.
- The existing sensitivity workbench records a pre-run prediction, changed input, actual result, and restored-base check in `apple_lab10_locked_record.md` and `apple_lab10_sensitivity_output.md`.
- The FCFE workbench’s accounting checks pass for the displayed sensitivity cases.

### Must-fix before final Project 1 submission

1. Produce a five-year **three-statement pro-forma driven by Apple-specific inputs**, with the balance sheet balancing every year and cash flow tying to balance-sheet cash.
2. Convert/rebuild the workbench’s cash-flow output from FCFE to **FCFF**, then feed that FCFF forecast into the DCF.
3. Reconcile the $131.0B starting FCFF to filed cash-flow items and a documented tax / working-capital convention.
4. Identify and label any one-time item or basis change in the historical base year; normalize or explicitly retain it with a filing-note citation and rationale.
5. Calculate and document WACC from sourced components; retain WACC–growth sensitivity, terminal-value share, and causal low/base/high cases.
6. Set a peer-selection policy **before** treating any peer set as final; calculate at least one consistent EV multiple and one equity-value multiple.
7. Decide and document the enterprise-to-equity treatment of marketable securities, lease liabilities, pension obligations, and any other debt-like or non-common claims.
8. Build the required semi-adjustable analyst product: bounded driver controls, base reset, visible sensitivity results, and checks that fail loudly for incoherent inputs.
9. Create a new final Locked Changed-Input Record with a human-authored, AI-off prediction, pre-run timestamp and repository commit, old/new units, expected and actual direction, decision effect, and diagnosis. The existing lab record is supporting evidence but does not yet document every final-project field.
10. Run and preserve the known-answer reconciliation, independent source/definition check, highest-risk failure test, and clean-environment README-only cold run.
11. Create the final repository README, visible executed output, validation-and-AI-use record, decision memo/deck, corrected transcripts, three videos, and 12-row submission manifest.

## AI-use record for this Edition B

| Tool / surface | Material task | Independent check or limitation | Disposition |
|---|---|---|---|
| Codex / generative AI | Organized the research-evolution structure, located course requirements, and helped identify that the existing workbench uses FCFE rather than FCFF. | I inspected `apple_proforma.py` and compared its FCFE label/formula with the Project 1 FCFF requirement. | Accepted as a documentation and model-review aid; the required rebuild remains my responsibility. |
| Generative-AI skeptical-review prompt | Identified peer-comparability as the weakest supported assumption. | I checked the peer memo’s cited business-model differences and preserved the limitation rather than adding unsupported peers. | Qualified: Microsoft and Alphabet remain leads, not final peers. |

## Monitoring and reversal rules

- **Initiation condition:** An initiate recommendation requires either a price at or below a refreshed, validated valuation range without deteriorating business evidence, or independently sourced evidence sufficient to support a materially stronger FCFF / margin path than the current base case.
- **Downside monitoring:** Review each earnings release for Services growth, iPhone demand, Greater China performance, gross-margin movement, regulatory developments, and cash-flow conversion.
- **Model kill rule:** Do not rely on the current DCF if the FCFF starting-point reconciliation, WACC construction, enterprise-to-equity bridge, or three-statement articulation cannot be reproduced and passed under documented checks.

## Working-file map

- Edition A baseline: `project-1-edition-a.md` and `project-1-edition-a.pdf`
- FCFF DCF / reverse DCF: `dcf.py` and `AAPL_reverseDCF_9-10-26.md`
- Peer cross-check: `peer_valuation.py` and `AAPL_peer_comparison_2026-09-10.md`
- Prior pro-forma / sensitivity work: `apple_proforma.py`, `apple_sensitivity_plan.md`, `apple_lab10_locked_record.md`, and `apple_lab10_sensitivity_output.md`
- Source log: `sources.md`

## What changed from Edition A to Edition B, and why?

**No material change in action:** I remain at watch/defer. The action did not change because the new FCFF DCF and the provisional peer-multiple check both sit below the September 17 market price, while material limitations remain unresolved. The evidence changed substantially: Edition A contained a research plan and operating facts; Edition B adds dated valuation outputs, a reverse-DCF test, an imperfect but transparent market cross-check, source-led risk framing, and an explicit list of model defects that must be repaired before final submission.

The most consequential change is methodological. I determined through review of the existing code and the Project 1 brief that the Apple workbench is FCFE-based, but the required valuation architecture is FCFF plus WACC and an enterprise-to-equity bridge. I therefore classify the FCFF DCF as the current valuation engine and qualify the FCFE workbench as operating-driver sensitivity evidence only. This conclusion was shaped by course instruction and model inspection; AI assisted in organizing and challenging the work, while the code and course requirements supplied the check. The final conclusion remains conditional until the FCFF pro-forma, bridge, peer policy, validation record, and reproducible product are complete.
