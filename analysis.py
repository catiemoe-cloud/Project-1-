"""Export the Apple FCFF DCF's frozen visible-output artifact."""

import json
from pathlib import Path

import dcf


AS_OF_DATE = "2026-09-17"
OUTPUT_PATH = Path("visible_output.json")


def calculate_base_case():
    fcff = dcf.STARTING_FCFF
    pv_explicit = 0.0
    for year, growth in enumerate(dcf.GROWTH_RATES, start=1):
        fcff *= 1 + growth
        pv_explicit += fcff / (1 + dcf.WACC) ** year
    terminal_value = fcff * (1 + dcf.TERMINAL_GROWTH) / (dcf.WACC - dcf.TERMINAL_GROWTH)
    pv_terminal = terminal_value / (1 + dcf.WACC) ** len(dcf.GROWTH_RATES)
    enterprise_value = pv_explicit + pv_terminal
    equity_value = enterprise_value + dcf.NON_OPERATING_CASH - dcf.DEBT
    return {
        "fcff_year_5_millions": round(fcff, 2),
        "enterprise_value_millions": round(enterprise_value, 2),
        "equity_value_millions": round(equity_value, 2),
        "value_per_share": round(equity_value / dcf.DILUTED_SHARES, 2),
        "terminal_value_share_of_ev": round(pv_terminal / enterprise_value, 4),
    }


def main():
    result = calculate_base_case()
    payload = {
        "company": "Apple Inc. (AAPL)",
        "as_of_date": AS_OF_DATE,
        "decision": "Watch / defer; do not initiate at the recorded $337.00 market price.",
        "units": "USD millions except per-share values and rates",
        "material_inputs": {
            "starting_fcff_millions": dcf.STARTING_FCFF,
            "fcff_growth_rates": dcf.GROWTH_RATES,
            "wacc": dcf.WACC,
            "terminal_growth": dcf.TERMINAL_GROWTH,
            "non_operating_cash_millions": dcf.NON_OPERATING_CASH,
            "debt_millions": dcf.DEBT,
            "shares_millions": dcf.DILUTED_SHARES,
            "market_price": dcf.TARGET_SHARE_PRICE,
        },
        "base_case": result,
        "limitations": [
            "Starting FCFF and WACC require final filing-based reconciliation.",
            "This is an interim FCFF DCF; the final project requires an articulating three-statement forecast and documented bridge policy.",
        ],
    }
    OUTPUT_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")
    print(f"Base value per share: ${result['value_per_share']:.2f}")


if __name__ == "__main__":
    main()

