"""Generate the visible executed-output artifact from the final FCFF model."""

import json
from pathlib import Path

from apple_fcff_model import (
    BRIDGE_CASH_AND_SECURITIES,
    BRIDGE_DEBT,
    MARKET_PRICE,
    SHARES,
    WACC_COMPONENTS,
    Assumptions,
    case_results,
    component_wacc,
    reverse_revenue_growth,
    sensitivity_grid,
    validation_tests,
    valuation,
)


OUTPUT_PATH = Path("visible_output.json")
AS_OF_DATE = "2026-09-17"


def main() -> None:
    base = valuation()
    cases = case_results()
    sensitivity = sensitivity_grid()
    validation = validation_tests()
    inputs = Assumptions()
    payload = {
        "company": "Apple Inc. (AAPL)",
        "as_of_date": AS_OF_DATE,
        "decision": "Watch / defer; base value is below the recorded market price.",
        "units": "USD millions except per-share values and rates",
        "material_inputs": {
            "revenue_growth": inputs.revenue_growth,
            "gross_margin": inputs.gross_margin,
            "operating_expense_rate": inputs.operating_expense_rate,
            "capex_rate": inputs.capex_rate,
            "wacc": inputs.wacc,
            "component_wacc": round(component_wacc(), 6),
            "wacc_components": WACC_COMPONENTS,
            "terminal_growth": inputs.terminal_growth,
            "market_price": MARKET_PRICE,
        },
        "enterprise_to_equity_bridge": {
            "enterprise_value_millions": round(base["enterprise_value"], 2),
            "cash_and_marketable_securities_millions": BRIDGE_CASH_AND_SECURITIES,
            "debt_millions": BRIDGE_DEBT,
            "equity_value_millions": round(base["equity_value"], 2),
            "shares_millions": SHARES,
        },
        "base_case": {
            "value_per_share": round(base["value_per_share"], 2),
            "terminal_value_share_of_ev": round(base["tv_share_of_ev"], 4),
            "fcff_by_year_millions": {str(row["year"]): round(row["fcff"], 2) for row in base["rows"]},
            "balance_sheet_gaps_millions": {str(row["year"]): round(row["balance_gap"], 2) for row in base["rows"]},
        },
        "causal_cases_value_per_share": {name: round(item["value_per_share"], 2) for name, item in cases.items()},
        "wacc_terminal_growth_sensitivity": {
            f"wacc_{wacc:.1%}_g_{growth:.1%}": round(value, 2)
            for (wacc, growth), value in sensitivity.items()
        },
        "reverse_dcf": {
            "solved_variable": "constant annual revenue growth, holding all other base inputs fixed",
            "target_price": MARKET_PRICE,
            "search_range": "-10% to 30%",
            "result": None if reverse_revenue_growth() is None else round(reverse_revenue_growth(), 6),
            "interpretation": "No solution in the stated range" if reverse_revenue_growth() is None else "Solved growth rate",
        },
        "validation": {
            "training_known_answer_value_per_share": round(validation["training_value"], 2),
            "training_wacc_probe_value_per_share": round(validation["training_wacc_probe"], 2),
            "all_checks_passed": all(validation["checks"].values()),
        },
        "limitations": [
            "Aggregate operating-asset and operating-liability forecast, not every reported Apple line item.",
            "Comparable-company output is a cross-check and is not averaged with DCF.",
        ],
    }
    OUTPUT_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")
    print(f"Base value per share: ${payload['base_case']['value_per_share']:.2f}")


if __name__ == "__main__":
    main()
