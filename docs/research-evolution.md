# Project 1 — Research Evolution

This Markdown companion contains the same two editions assembled in `research-evolution.pdf`: the preserved Edition A baseline followed by the final Edition B. Edition A retains its original September 1, 2026 planning valuation date. Edition B is the final September 17, 2026 decision and valuation record.

---

# Project 1 — Edition A

**Company:** Apple Inc. (NASDAQ: AAPL)  
**Valuation date:** September 1, 2026  
**Decision requested:** Whether an investment committee should authorize further diligence toward an initial public-equity position in Apple.  
**Initial view:** **Watch / defer.** Apple has demonstrated durable scale, strong profitability and growth in Services, but an initiate decision requires current valuation inputs and a more explicit assessment of product-cycle, China, regulatory and capital-allocation risks.

> **Prior-work disclosure:** This preliminary company baseline builds on my existing Apple course files and is not a final valuation or recommendation. Those working files were consulted for continuity of historical facts, forecast structure, sensitivity planning, and previously documented validation work. Current filing facts in this document are independently identified below and take precedence where they differ.
>
> **Existing files consulted:** [Apple FY2025 filing facts](../research/apple-2025-10k-filing-facts.md) · [Apple pro-forma model](../archive/apple_proforma.py) · [Apple sensitivity plan](../archive/apple_sensitivity_plan.md) · [Locked changed-input record](../archive/apple_lab10_locked_record.md) · [Sensitivity output](../archive/apple_lab10_sensitivity_output.md)

## Primary filing and financial evidence

**Primary sources:** Apple Inc.'s [Form 10-Q for the quarter ended June 27, 2026](https://www.sec.gov/Archives/edgar/data/320193/000032019326000020/aapl-20260627.htm), filed July 31, 2026 (accession **0000320193-26-000020**), and its [Form 10-K for fiscal year ended September 27, 2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm), filed October 31, 2025 (accession **0000320193-25-000079**). The 10-Q is the latest filed financial information available as of the September 1, 2026 valuation date. All financial figures below are in **U.S. dollars and millions**, unless stated otherwise.

| Required evidence | FY2025 observation | Filing location | Investment relevance |
|---|---:|---|---|
| Entity | Apple Inc. | Cover page | Legal registrant and issuer of AAPL common stock. |
| Reporting period | Fiscal year ended September 27, 2025 | Cover page | Establishes the financial-information date. |
| Filing date | October 31, 2025 | EDGAR filing index | Establishes public availability of the source. |
| Currency / units | U.S. dollars; financial statements in millions; shares in thousands (except per-share data) | Consolidated Statements of Operations, p. 29 | Prevents unit errors in valuation work. |
| Cash and cash equivalents | $39,544 | Q3 2026 Form 10-Q, Condensed Consolidated Balance Sheets, p. 2 | Cash is an enterprise-to-equity bridge asset, subject to the treatment of restricted cash and operating-cash needs. |
| Commercial paper | $1,997 | Q3 2026 Form 10-Q, Condensed Consolidated Balance Sheets, p. 2 | Short-term interest-bearing borrowing; included in debt under the stated bridge convention. |
| Current term debt | $11,007 | Q3 2026 Form 10-Q, Condensed Consolidated Balance Sheets, p. 2 | Current portion of interest-bearing debt. |
| Non-current term debt | $71,340 | Q3 2026 Form 10-Q, Condensed Consolidated Balance Sheets, p. 2 | Long-term interest-bearing debt. |
| Total reported term debt | $82,347 | Q3 2026 Form 10-Q, Note 6, “Term Debt,” p. 10 | Carrying amount before adding commercial paper. |
| Total debt used in initial bridge | $84,344 | $1,997 commercial paper + $82,347 term debt | Explicitly includes short-term commercial paper and term debt; excludes operating leases pending class convention. |
| Share-count evidence | 14,594,180,000 common shares outstanding as of July 17, 2026; nine-month weighted-average diluted shares of 14.750 billion | Q3 2026 Form 10-Q, cover page; Note 3, p. 6 | The point-in-time count supports market capitalization; diluted weighted-average shares remain relevant for EPS. The valuation must state which convention it uses. |
| Operating-value driver | Nine-month Services net sales: $91,728, up 14% year over year | Q3 2026 Form 10-Q, MD&A, “Products and Services Performance,” p. 15 | Services growth and mix are potentially important to recurring revenue and margin durability. |
| Contextual operating scale | Nine-month total net sales: $364,357, up 16% year over year; Q3 total gross margin: 50.1% | Q3 2026 Form 10-Q, MD&A, pp. 14–16 | Frames current growth and operating leverage, but a full-year forecast must not annualize one quarter without justification. |

## Enterprise-to-equity bridge check

This market-implied Apple bridge uses the September 1, 2026 closing price and the latest share-count and balance-sheet information publicly available by that date. It is a reconciliation check—not a DCF output—and excludes marketable securities and operating leases pending a documented policy decision.

| Bridge item | $ millions | Treatment |
|---|---:|---|
| Market-implied enterprise value | 4,789,806 | `Equity value + debt − cash`; USD millions. |
| Less: commercial paper | (1,997) | Q3 2026 Form 10-Q balance sheet; June 27, 2026. |
| Less: term debt | (82,347) | Q3 2026 Form 10-Q, Note 6; June 27, 2026. |
| Add: cash and cash equivalents | 39,544 | Q3 2026 Form 10-Q balance sheet; June 27, 2026. |
| Equals: implied equity value | 4,745,006 | `4,789,806 − 1,997 − 82,347 + 39,544`; USD millions. |
| Shares outstanding | 14,594.180 | 14.594 billion shares as of July 17, 2026, from the Q3 2026 Form 10-Q cover page. |
| Implied value per share | $325.13 | `4,745,006 ÷ 14,594.180`; matches the September 1, 2026 closing price. |
| Price source / reconciliation variance | $325.13 / $0.00 | Yahoo Finance historical close on September 1, 2026; rounding to whole $ millions creates immaterial differences. |

**Bridge convention:** Debt is commercial paper plus term debt; cash means reported cash and cash equivalents. Marketable securities, operating leases, pension obligations, preferred equity, and noncontrolling interests are excluded from this preliminary reconciliation and must be explicitly evaluated in the final DCF bridge.

## Initial thesis

Apple merits continued research, not an immediate recommendation. Through the first nine months of fiscal 2026, net sales grew 16% year over year and Services net sales grew 14%; the Q3 2026 filing also reported a 50.1% total gross margin for the quarter. This supports a hypothesis of substantial ecosystem-driven earnings durability. However, the filing identifies business exposures that could materially affect normalized growth and margins, including dependence on new-product launches, intense competition, supply-chain concentration, foreign-exchange and tariff effects, and regulatory/legal developments. The current market price, required return and forward operating assumptions have not yet been evaluated; therefore, value relative to price is unknown.

## Consequential assumptions

- Services revenue can continue to grow faster than total company revenue without a material deterioration in economics or regulatory constraints.
- The current product installed base and ecosystem sustain customer retention and premium pricing through future device cycles.
- The selected debt convention—commercial paper plus term debt—matches the course bridge convention. Operating leases and marketable securities are excluded until that convention is confirmed.
- The valuation will use fully diluted shares appropriate to the valuation date; the FY2025 weighted-average diluted share count is evidence, not automatically the final point-in-time share count.
- A valuation completed as of September 1, 2026 will use only information public by that date, including the July 31, 2026 Form 10-Q, rather than treating FY2025 filing data as current by itself.

## Unknowns and decision-critical questions

- What is Apple’s market capitalization and enterprise value on the valuation date?
- What forward growth, operating margin, reinvestment and discount-rate assumptions are required to justify the market price?
- How durable is Services growth under App Store, advertising and platform regulation?
- What are the downside effects of China demand weakness, tariffs and supply-chain disruption?
- Under the course convention, should marketable securities, lease liabilities, restricted cash, preferred interests or noncontrolling interests be included in the enterprise-to-equity bridge?

## Research plan

1. Establish valuation-date market capitalization, debt, cash and diluted-share inputs; reconcile all bridge components to the course convention.
2. Build a three-case operating forecast separating Products and Services, with explicit revenue growth, gross-margin and operating-expense assumptions.
3. Analyze Services economics and regulatory exposure, including the sensitivity of revenue and margin to App Store and advertising changes.
4. Evaluate geographic and supply-chain downside cases, with particular attention to Greater China demand, tariff costs and component concentration.
5. Value Apple using a DCF and a market-based cross-check; compare implied value per diluted share with the valuation-date price and identify the assumptions that drive the recommendation.

---

# Project 1 — Edition B: Research Evolution and Current Position

**Company/security:** Apple Inc. common stock (AAPL)
**Intended user:** Buy-side investment committee; fund has no position
**Decision horizon / valuation date:** Initiation decision as of September 17, 2026
**Currency/share basis:** USD millions except per-share values; 14,594.18M point-in-time shares
**Action:** **Watch/defer; do not initiate at the recorded $337.00 per-share price.**

Edition A remains unchanged in `edition-a/project-1-edition-a.pdf`. This Edition B records the post-checkpoint research, model, validation, and AI-use evolution.

## A-to-B change table

| Changed item | Edition A | Edition B | Primary driver of change | Evidence or test |
|---|---|---|---|---|
| Thesis / recommendation | Watch/defer while valuation relative to price was unknown. | Watch/defer at $337.00; DCF range remains below market. | Own analysis plus course architecture. | Final FCFF range: $87.07–$185.85/share. |
| Data/source choice | Identified Apple FY2025 10-K and Q3 FY2026 10-Q. | Anchored FY2025 opening statements to the 10-K and bridge to Q3 FY2026 cash, debt, and shares. | Own source reconciliation. | Model, source log, and challenge record. |
| Assumption/model design | Planned a valuation framework. | Built five-year articulating FCFF statements with cases, grid, reverse search, and product controls. | Course instruction and own model review. | Articulation, known-answer, monotonicity, bridge, and cold-run tests. |
| Risk/limitation | Product cycle, China, regulation, FX, and capital allocation were open. | Adds terminal-value dependence, WACC judgment, aggregate working-capital forecast, and peer mismatch. | Own analysis; AI-assisted model challenge independently checked. | Challenge record, peer policy, and validation record. |

## Final valuation evidence

The final model forecasts FY2026E–FY2030E revenue, EBIT, operating assets/liabilities, PP&E, cash flow, and FCFF. Base assumptions are 6% annual revenue growth, 47.0% gross margin, 15.0% operating expenses/revenue, 3.0% capex/revenue, 9.0% WACC, and 2.5% terminal growth. The 9.0% model rate is the nearest whole-percent representation of a dated 9.45% risk-free-rate, beta, ERP, debt-cost, tax-rate, and market-value-capital-structure build; its sources and limitations are in `wacc-build.md`. Base enterprise value is $1,858,504M. The bridge adds $146,517M cash plus marketable securities and subtracts $84,344M commercial paper plus term debt, yielding $1,920,677M equity value, or **$131.61/share**.

Causal cases are **$87.07 low / $131.61 base / $185.85 high**. The WACC–terminal-growth grid spans $109.06 to $167.57 per share over 8%–10% WACC and 2.0%–3.0% terminal growth. Terminal value is 74.9% of base enterprise value. The reverse DCF cannot reach $337.00 using constant annual revenue growth from −10% to 30% while holding all other base inputs fixed; this is a bounded market-implied expectation, not proof of mispricing.

The P/E cross-check yields $206.86–$239.69 per Apple share from qualified Microsoft and Alphabet peers. Alphabet’s documented EV/revenue multiple is 10.7747x. These methods are not averaged: Microsoft has greater enterprise/cloud exposure and Alphabet is advertising-led, so they are market checks rather than interchangeable versions of Apple.

## Conditions, monitoring, and reversal

Initiate only if a refreshed, reproducible range supports the price or filed evidence supports a stronger sustainable FCFF path. Monitor Services growth, iPhone demand, Greater China, gross margin, capital spending, regulation, and cash-flow conversion. Reopen the model if the bridge convention, WACC evidence, operating-driver evidence, or statement articulation fails.

## AI-use and validation

Codex assisted with documentation organization, source reconciliation, and code drafting. I checked the accepted model output through the published Week 3 known answer, filing-based bridge input check, statement articulation, DCF monotonicity, peer-definition check, cold run, and changed-input test. The complete named disclosure and locked record are in `validation-and-ai-use.md`.

## What changed from Edition A to Edition B, and why?

The action did not change, but the decision evidence did. Edition A established the research question and facts to investigate. Edition B supplies a reproducible FCFF engine, a valuation range, explicit bridge, documented driver challenges, market cross-checks, and validation results. The evidence supports watch/defer rather than a single-number claim because the base, downside, and upside cases all remain below the $337.00 price while material operating and discount-rate conditions remain monitorable.
