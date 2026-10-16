# WACC Component Build — Apple (AAPL)

**Valuation date:** September 17, 2026. **Currency:** USD. **Capital values:** USD millions.  This is the documented anchor for the DCF WACC; it does not turn a forecast discount rate into a reported fact.

## Components and calculation

| Component | Input | Definition / calculation | Source and as-of | Treatment / limitation |
|---|---:|---|---|---|
| Risk-free rate | 4.94% | U.S. Treasury 10-year constant-maturity par yield. | [U.S. Treasury daily yield curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=202609&type=daily_treasury_yield_curve), September 17, 2026. | Same-date USD nominal proxy. |
| Levered beta | 1.09 | Yahoo Finance “Beta (5Y Monthly)” for AAPL, retrieved September 16, 2026, the last available screen before the valuation date. | [Yahoo Finance AAPL quote](https://finance.yahoo.com/quote/AAPL/). | Provider-calculated trailing beta; it can change with the lookback period and is not a filing fact. |
| Equity-risk premium | 4.23% | Implied U.S. ERP. | [Aswath Damodaran, January 2026 data update](https://aswathdamodaran.blogspot.com/2026/01/), January 1, 2026. | Annual market-implied estimate; retained because a September daily ERP was not available in the project evidence set. |
| Cost of equity | 9.55% | 4.94% + (1.09 × 4.23%). | Calculated from the three inputs above. | CAPM output, not a price target. |
| Pre-tax cost of debt | 4.00% | Coupon proxy for Apple fixed-rate debt. | [Apple FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm), debt securities; the filing identifies Apple fixed-rate notes, including 4.000% notes issued in FY2025. | A disclosed coupon proxy, not an observed yield-to-maturity. Apple does not separately report interest expense in the Q3 income statement, so a precise current yield is not claimed. |
| Tax rate for debt shield | 17.6% | Apple’s effective rate for the first nine months of FY2026. | [Apple Q3 FY2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/320193/000032019326000020/aapl-20260627.htm), filed July 31, 2026. | Used only in the WACC tax shield. The operating forecast separately uses a conservative 16.0% NOPAT tax assumption. |
| Market value of equity | $4,918,239M | $337.00 recorded market price × 14,594.18M point-in-time shares. | Price is the project’s September 17, 2026 recorded market price; shares are from Apple Q3 FY2026 Form 10-Q cover page (July 17, 2026). | Price is a dated market input, not valuation evidence. |
| Market value of debt | $84,344M | $1,997M commercial paper + $11,007M current term debt + $71,340M non-current term debt. | Apple Q3 FY2026 Form 10-Q, June 27, 2026 balance sheet. | Book debt is used as the practical market-value proxy. |
| Capital weights | 98.31% equity / 1.69% debt | Equity or debt divided by $5,002,583M total capital. | Calculated from the preceding two rows. | The very small debt weight limits debt-cost sensitivity. |

**Calculated component WACC:**

`98.31% × 9.55% + 1.69% × 4.00% × (1 − 17.6%) = 9.45%`.

## Model convention and challenge

The executable model uses a **9.0% whole-percent base input**, which is the nearest whole-percent representation of the 9.45% component calculation. It does not present 9.0% as a directly observed fact. The 8%–10% sensitivity grid brackets the 9.45% component result, and `apple_fcff_model.py` tests that the selected base remains within the half-percentage-point rounding band.

The recommended next refinement is to replace the 4.00% coupon proxy with a valuation-date Apple bond yield and to refresh beta and ERP on the exact valuation date. A committee that does not accept whole-percent rounding should run the same model at 9.45%; this would lower the base value and would not weaken the current watch/defer action.
