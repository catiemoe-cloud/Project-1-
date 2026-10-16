# Comparable-Company Policy and Evidence — Apple

**Policy fixed before interpreting the outputs.** The target is Apple and the valuation date is September 17, 2026. A company qualifies only if it is a listed, profitable technology platform with (1) a material consumer ecosystem or device/software/services combination, (2) annual financial statements public by the valuation date, and (3) a scale large enough that its enterprise-value multiple is meaningful. Exclude the target, unprofitable companies, private companies, and issuers for which a matching-date price or an annual GAAP denominator cannot be documented.

## Candidate decisions

| Candidate | Decision | Evidence and judgment |
|---|---|---|
| Apple | Exclude | Target; cannot be its own comparable. |
| Microsoft | Include, qualified | Listed, profitable technology platform with cloud, software, consumer and device activity. Its enterprise/cloud exposure is materially higher than Apple’s, so it is a cross-check rather than a close operational match. See its FY2026 10-K cited in `AAPL_peer_comparison_2026-09-10.md`. |
| Alphabet | Include, qualified | Listed, profitable platform with subscriptions, devices, cloud, and services. Advertising is its dominant revenue source, so its multiple is not directly transferable to Apple. Alphabet’s FY2025 10-K reports $402,836M revenue, $126,843M cash/cash equivalents/marketable securities, and $46,547M long-term debt (plus a $1,996M current portion). |
| Meta, Amazon, hardware-only issuers | Exclude | They fail the pre-set comparability screen: advertising-led economics, retail/logistics-led economics, or insufficiently similar ecosystem mix. They were not added or removed after viewing results. |

## Consistent multiple evidence

The equity-value multiple is P/E using matching-date price divided by the latest annual GAAP diluted EPS public by the valuation date. `peer_valuation.py` calculates Microsoft at 27.729805x and Alphabet at 32.130435x; the $206.86–$239.69 Apple implied range is retained only as a qualified cross-check.

The EV multiple is **EV/revenue**, not EV/EBITDA, because both Apple and Alphabet report revenue on a consistent annual GAAP basis and this avoids an unsupported EBITDA add-back. For Alphabet, the transparent, documented approximation is:

| Item | Amount |
|---|---:|
| GOOGL price, Sep. 17, 2026 | $347.33/share |
| FY2025 diluted shares used as market-cap proxy | 12,722M |
| Equity value proxy | $4,418,732M |
| Less cash, equivalents, and marketable securities | $(126,843)M |
| Add debt, including current portion | $48,543M |
| Enterprise value proxy | $4,340,432M |
| FY2025 revenue | $402,836M |
| EV / revenue | 10.7747x |

The displayed EV is $347.33 × 12,722M − $126,843M + $48,543M. This file supplies policy and source evidence, but **does not convert Alphabet’s EV/revenue into an Apple price target** because Apple’s revenue mix and capital return differ materially. The decision therefore continues to rest on the Apple FCFF model, with P/E and EV/revenue as non-averaged market checks.

## Source links

- [Apple Q3 FY2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/320193/000032019326000020/aapl-20260627.htm)
- [Apple FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm)
- [Alphabet FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm)
- [Microsoft FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm)
