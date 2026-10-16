# Project 1 — Edition B: Research Evolution and Current Position

**Company/security:** Apple Inc. common stock (AAPL)
**Intended user:** Buy-side investment committee; fund has no position
**Decision horizon / valuation date:** Initiation decision as of September 17, 2026
**Currency/share basis:** USD millions except per-share values; 14,594.18M point-in-time shares
**Action:** **Watch/defer; do not initiate at the recorded $337.00 per-share price.**

Edition A remains unchanged in project-1-edition-a.pdf. This Edition B records the post-checkpoint research, model, validation, and AI-use evolution.

## A-to-B change table

| Changed item | Edition A | Edition B | Primary driver of change | Evidence or test |
|---|---|---|---|---|
| Thesis / recommendation | Watch/defer while valuation relative to price was unknown. | Watch/defer at $337.00; DCF range remains below market. | Own analysis plus course architecture. | Final FCFF range: $87.07–$185.85/share. |
| Data/source choice | Identified Apple FY2025 10-K and Q3 FY2026 10-Q. | Anchored FY2025 opening statements to the 10-K and bridge to Q3 FY2026 cash, debt, and shares. | Own source reconciliation. | Model, source log, and challenge record. |
| Assumption/model design | Planned a valuation framework. | Built five-year articulating FCFF statements with cases, grid, reverse search, and product controls. | Course instruction and own model review. | Articulation, known-answer, monotonicity, bridge, and cold-run tests. |
| Risk/limitation | Product cycle, China, regulation, FX, and capital allocation were open. | Adds terminal-value dependence, WACC judgment, aggregate working-capital forecast, and peer mismatch. | Own analysis; AI-assisted model challenge independently checked. | Challenge record, peer policy, and validation record. |

## Final valuation evidence

The final model forecasts FY2026E–FY2030E revenue, EBIT, operating assets/liabilities, PP&E, cash flow, and FCFF. Base assumptions are 6% annual revenue growth, 47.0% gross margin, 15.0% operating expenses/revenue, 3.0% capex/revenue, 9.0% WACC, and 2.5% terminal growth. The 9.0% model rate is the nearest whole-percent representation of a dated 9.45% risk-free-rate, beta, ERP, debt-cost, tax-rate, and market-value-capital-structure build; its sources and limitations are in `docs/wacc-build.md`. Base enterprise value is $1,858,504M. The bridge adds $146,517M cash plus marketable securities and subtracts $84,344M commercial paper plus term debt, yielding $1,920,677M equity value, or **$131.61/share**.

Causal cases are **$87.07 low / $131.61 base / $185.85 high**. The WACC–terminal-growth grid spans $109.06 to $167.57 per share over 8%–10% WACC and 2.0%–3.0% terminal growth. Terminal value is 74.9% of base enterprise value. The reverse DCF cannot reach $337.00 using constant annual revenue growth from −10% to 30% while holding all other base inputs fixed; this is a bounded market-implied expectation, not proof of mispricing.

The P/E cross-check yields $206.86–$239.69 per Apple share from qualified Microsoft and Alphabet peers. Alphabet’s documented EV/revenue multiple is 10.7747x. These methods are not averaged: Microsoft has greater enterprise/cloud exposure and Alphabet is advertising-led, so they are market checks rather than interchangeable versions of Apple.

## Conditions, monitoring, and reversal

Initiate only if a refreshed, reproducible range supports the price or filed evidence supports a stronger sustainable FCFF path. Monitor Services growth, iPhone demand, Greater China, gross margin, capital spending, regulation, and cash-flow conversion. Reopen the model if the bridge convention, WACC evidence, operating-driver evidence, or statement articulation fails.

## AI-use and validation

Codex assisted with documentation organization, source reconciliation, and code drafting. I checked the accepted model output through the published Week 3 known answer, filing-based bridge input check, statement articulation, DCF monotonicity, peer-definition check, cold run, and changed-input test. The complete named disclosure and locked record are in docs/validation-and-ai-use.md.

## What changed from Edition A to Edition B, and why?

The action did not change, but the decision evidence did. Edition A established the research question and facts to investigate. Edition B supplies a reproducible FCFF engine, a valuation range, explicit bridge, documented driver challenges, market cross-checks, and validation results. The evidence supports watch/defer rather than a single-number claim because the base, downside, and upside cases all remain below the $337.00 price while material operating and discount-rate conditions remain monitorable.
