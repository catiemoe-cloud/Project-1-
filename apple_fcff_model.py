"""Apple five-year three-statement FCFF model (USD millions except per-share data).

The model starts with Apple FY2025 audited balances.  It treats cash and
marketable securities as non-operating in the valuation bridge, holds gross
debt constant, and forecasts the operating balance-sheet accounts as a share
of revenue.  The cash-flow statement ties the change in cash to the balance
sheet every forecast year; a financing line represents Apple's residual cash
return to common shareholders rather than an unsupported debt plug.
"""

from dataclasses import dataclass, replace
from typing import Optional


YEARS = (2026, 2027, 2028, 2029, 2030)
MARKET_PRICE = 337.00
SHARES = 14_594.18  # Q3 FY2026 cover page, millions, July 17, 2026.
# Q3 FY2026 Form 10-Q / June 27, 2026, valuation-date bridge.
BRIDGE_CASH_AND_SECURITIES = 146_517.0
BRIDGE_DEBT = 84_344.0

# FY2025 Form 10-K / September 27, 2025, USD millions.  Aggregated operating
# assets and liabilities reconcile exactly to the reported balance sheet.
OPENING = {
    "revenue": 416_161.0,
    "cash": 35_934.0,
    "marketable_securities": 96_486.0,
    "ppe": 49_834.0,
    # AR + vendor receivables + inventory + other current assets + total
    # intangible assets + other non-current assets.  Total intangibles (13,301)
    # are used here, so the current portion is not double counted.
    "operating_assets": 176_987.0,
    "debt": 98_657.0,
    "operating_liabilities": 186_851.0,
    "equity": 73_733.0,
}


@dataclass(frozen=True)
class Assumptions:
    """All rates are annual; ranges are enforced in the product UI."""

    revenue_growth: float = 0.06
    gross_margin: float = 0.470
    operating_expense_rate: float = 0.150
    tax_rate: float = 0.160
    da_rate_on_opening_ppe: float = 0.200
    capex_rate: float = 0.030
    operating_assets_rate: float = OPENING["operating_assets"] / OPENING["revenue"]
    operating_liabilities_rate: float = OPENING["operating_liabilities"] / OPENING["revenue"]
    wacc: float = 0.090
    terminal_growth: float = 0.025
    annual_dividend: float = 16_000.0


def validate(assumptions: Assumptions) -> list[str]:
    """Return user-visible errors rather than producing incoherent output."""
    errors = []
    if not -0.10 <= assumptions.revenue_growth <= 0.30:
        errors.append("Revenue growth must be between -10% and 30%.")
    if not 0.35 <= assumptions.gross_margin <= 0.60:
        errors.append("Gross margin must be between 35% and 60%.")
    if not 0.08 <= assumptions.operating_expense_rate <= 0.25:
        errors.append("Operating-expense rate must be between 8% and 25%.")
    if not 0.10 <= assumptions.tax_rate <= 0.30:
        errors.append("Tax rate must be between 10% and 30%.")
    if not 0.01 <= assumptions.capex_rate <= 0.08:
        errors.append("Capex rate must be between 1% and 8%.")
    if not 0.06 <= assumptions.wacc <= 0.12:
        errors.append("WACC must be between 6% and 12%.")
    if not 0.01 <= assumptions.terminal_growth <= 0.04:
        errors.append("Terminal growth must be between 1% and 4%.")
    if assumptions.terminal_growth >= assumptions.wacc:
        errors.append("Terminal growth must be lower than WACC.")
    return errors


def forecast(assumptions: Assumptions = Assumptions()) -> dict:
    """Build the income statement, balance sheet, cash flow, and FCFF."""
    errors = validate(assumptions)
    if errors:
        raise ValueError("; ".join(errors))

    rows = []
    prior = dict(OPENING)
    for year in YEARS:
        revenue = prior["revenue"] * (1 + assumptions.revenue_growth)
        gross_profit = revenue * assumptions.gross_margin
        operating_expenses = revenue * assumptions.operating_expense_rate
        depreciation = prior["ppe"] * assumptions.da_rate_on_opening_ppe
        ebit = gross_profit - operating_expenses - depreciation
        # The model is an unlevered valuation. Interest is shown only to link
        # reported debt to net income/cash; FCFF begins with EBIT after tax.
        interest = prior["debt"] * 0.040
        pretax_income = ebit - interest
        taxes = max(0.0, pretax_income * assumptions.tax_rate)
        net_income = pretax_income - taxes
        nopat = ebit * (1 - assumptions.tax_rate)

        operating_assets = revenue * assumptions.operating_assets_rate
        operating_liabilities = revenue * assumptions.operating_liabilities_rate
        nwc = operating_assets - operating_liabilities
        prior_nwc = prior["operating_assets"] - prior["operating_liabilities"]
        change_nwc = nwc - prior_nwc
        capex = revenue * assumptions.capex_rate
        ppe = prior["ppe"] + capex - depreciation
        fcff = nopat + depreciation - capex - change_nwc

        # Cash flow statement: capital return is held at Apple-specific policy
        # level (dividend plus residual repurchases) and is not used in FCFF.
        cash_from_operations = net_income + depreciation - change_nwc
        cash_before_financing = prior["cash"] + cash_from_operations - capex
        residual_repurchase = max(0.0, cash_before_financing - 30_000.0 - assumptions.annual_dividend)
        capital_return = assumptions.annual_dividend + residual_repurchase
        cash = cash_before_financing - capital_return
        equity = prior["equity"] + net_income - capital_return
        debt = prior["debt"]
        marketable_securities = prior["marketable_securities"]

        assets = cash + marketable_securities + ppe + operating_assets
        liabilities_and_equity = debt + operating_liabilities + equity
        balance_gap = assets - liabilities_and_equity
        cash_flow_change = cash - prior["cash"]
        cash_flow_change_from_statement = cash_from_operations - capex - capital_return
        if abs(balance_gap) > 0.05:
            raise AssertionError(f"FY{year} balance sheet does not balance: {balance_gap:.2f}")
        if abs(cash_flow_change - cash_flow_change_from_statement) > 0.05:
            raise AssertionError(f"FY{year} cash flow does not tie to cash: {cash_flow_change:.2f}")

        row = locals().copy()
        rows.append({key: row[key] for key in (
            "year", "revenue", "gross_profit", "operating_expenses", "depreciation", "ebit",
            "interest", "pretax_income", "taxes", "net_income", "nopat", "operating_assets",
            "operating_liabilities", "nwc", "change_nwc", "capex", "ppe", "fcff",
            "cash_from_operations", "capital_return", "cash", "marketable_securities", "debt",
            "equity", "assets", "liabilities_and_equity", "balance_gap", "cash_flow_change",
            "cash_flow_change_from_statement")})
        prior = {
            "revenue": revenue, "cash": cash, "marketable_securities": marketable_securities,
            "ppe": ppe, "operating_assets": operating_assets, "debt": debt,
            "operating_liabilities": operating_liabilities, "equity": equity,
        }
    return {"assumptions": assumptions, "rows": rows}


def valuation(assumptions: Assumptions = Assumptions()) -> dict:
    model = forecast(assumptions)
    rows = model["rows"]
    pv_explicit = sum(row["fcff"] / (1 + assumptions.wacc) ** index
                      for index, row in enumerate(rows, start=1))
    terminal_fcff = rows[-1]["fcff"] * (1 + assumptions.terminal_growth)
    terminal_value = terminal_fcff / (assumptions.wacc - assumptions.terminal_growth)
    pv_terminal = terminal_value / (1 + assumptions.wacc) ** len(rows)
    enterprise_value = pv_explicit + pv_terminal
    # Bridge policy: include cash and marketable securities, subtract commercial
    # paper and term debt; operating leases are retained in operating liabilities
    # and not double counted as debt in this simplified model.
    equity_value = enterprise_value + BRIDGE_CASH_AND_SECURITIES - BRIDGE_DEBT
    return {
        **model,
        "pv_explicit": pv_explicit,
        "terminal_value": terminal_value,
        "pv_terminal": pv_terminal,
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "value_per_share": equity_value / SHARES,
        "tv_share_of_ev": pv_terminal / enterprise_value,
    }


def case_results() -> dict:
    """Causal cases change operating drivers, not just WACC."""
    cases = {
        "low": Assumptions(revenue_growth=0.02, gross_margin=0.450, operating_expense_rate=0.160, capex_rate=0.035, wacc=0.095, terminal_growth=0.020),
        "base": Assumptions(),
        "high": Assumptions(revenue_growth=0.09, gross_margin=0.485, operating_expense_rate=0.145, capex_rate=0.028, wacc=0.085, terminal_growth=0.030),
    }
    return {name: valuation(case) for name, case in cases.items()}


def sensitivity_grid() -> dict:
    """Return the required WACC-terminal-growth sensitivity grid."""
    waccs = (0.08, 0.09, 0.10)
    growths = (0.020, 0.025, 0.030)
    grid = {}
    for wacc in waccs:
        for terminal_growth in growths:
            grid[(wacc, terminal_growth)] = valuation(
                replace(Assumptions(), wacc=wacc, terminal_growth=terminal_growth)
            )["value_per_share"]
    return grid


def reverse_revenue_growth(target_price: float = MARKET_PRICE) -> Optional[float]:
    """Solve the constant annual revenue-growth assumption that reaches price."""
    lower, upper = -0.10, 0.30
    def difference(growth: float) -> float:
        return valuation(replace(Assumptions(), revenue_growth=growth))["value_per_share"] - target_price
    lower_difference, upper_difference = difference(lower), difference(upper)
    if lower_difference * upper_difference > 0:
        return None
    for _ in range(100):
        midpoint = (lower + upper) / 2
        midpoint_difference = difference(midpoint)
        if abs(midpoint_difference) < 1e-8:
            return midpoint
        if lower_difference * midpoint_difference < 0:
            upper = midpoint
        else:
            lower, lower_difference = midpoint, midpoint_difference
    return (lower + upper) / 2


def training_case_value(wacc: float = 0.10, terminal_growth: float = 0.03) -> float:
    """Course Week 3 known-answer FCFF DCF; independent of Apple inputs."""
    fcff = 100.0
    growths = (0.08, 0.06, 0.05, 0.04, 0.03)
    pv_explicit = 0.0
    for year, growth in enumerate(growths, start=1):
        fcff *= 1 + growth
        pv_explicit += fcff / (1 + wacc) ** year
    terminal_value = fcff * (1 + terminal_growth) / (wacc - terminal_growth)
    enterprise_value = pv_explicit + terminal_value / (1 + wacc) ** 5
    return (enterprise_value + 50.0 - 300.0) / 50.0


def validation_tests() -> dict:
    """Known-answer, DCF-boundary, and monotonicity tests for the final engine."""
    training_value = training_case_value()
    training_wacc_probe = training_case_value(wacc=0.11)
    grid = sensitivity_grid()
    base = valuation()["value_per_share"]
    lower_wacc = valuation(replace(Assumptions(), wacc=0.08))["value_per_share"]
    higher_wacc = valuation(replace(Assumptions(), wacc=0.10))["value_per_share"]
    lower_growth = valuation(replace(Assumptions(), terminal_growth=0.02))["value_per_share"]
    higher_growth = valuation(replace(Assumptions(), terminal_growth=0.03))["value_per_share"]
    checks = {
        "training_known_answer": abs(training_value - 27.50) < 0.01,
        "training_wacc_probe": abs(training_wacc_probe - 23.41) < 0.02,
        "wacc_monotonicity": lower_wacc > base > higher_wacc,
        "terminal_growth_monotonicity": lower_growth < base < higher_growth,
        "bridge_recomputes": abs((valuation()["enterprise_value"] + BRIDGE_CASH_AND_SECURITIES - BRIDGE_DEBT) / SHARES - base) < 1e-8,
        "grid_valid": all(growth < wacc for wacc, growth in grid),
    }
    if not all(checks.values()):
        raise AssertionError(f"Validation failure: {checks}")
    return {"checks": checks, "training_value": training_value, "training_wacc_probe": training_wacc_probe, "grid": grid}


def _money(value: float) -> str:
    return f"{value:,.1f}"


def main() -> None:
    base = valuation()
    print("Apple FCFF Three-Statement Model — USD millions except per-share values")
    print("Income Statement")
    for label, key in (("Revenue", "revenue"), ("EBIT", "ebit"), ("NOPAT", "nopat"), ("Net income", "net_income")):
        print(f"{label:<22}" + "".join(f"{_money(row[key]):>14}" for row in base["rows"]))
    print("Cash Flow / FCFF")
    for label, key in (("Cash from operations", "cash_from_operations"), ("Capex", "capex"), ("Change NWC", "change_nwc"), ("FCFF", "fcff")):
        print(f"{label:<22}" + "".join(f"{_money(row[key]):>14}" for row in base["rows"]))
    print("Checks")
    for row in base["rows"]:
        print(f"FY{row['year']}E balance gap {row['balance_gap']:.2f}; cash-flow tie {row['cash_flow_change'] - row['cash_flow_change_from_statement']:.2f}")
    print(f"Enterprise value: ${base['enterprise_value']:,.1f}M")
    print(f"Equity value: ${base['equity_value']:,.1f}M")
    print(f"Value per share: ${base['value_per_share']:.2f}")
    print(f"Terminal-value share of EV: {base['tv_share_of_ev']:.1%}")
    for name, result in case_results().items():
        print(f"{name.title()} case value/share: ${result['value_per_share']:.2f}")
    print("WACC / Terminal-Growth Sensitivity: value per share")
    grid = sensitivity_grid()
    for wacc in (0.08, 0.09, 0.10):
        values = " | ".join(f"g {growth:.1%}: ${grid[(wacc, growth)]:.2f}" for growth in (0.020, 0.025, 0.030))
        print(f"WACC {wacc:.1%}: {values}")
    implied_growth = reverse_revenue_growth()
    if implied_growth is None:
        print(f"Reverse DCF: no revenue-growth solution for ${MARKET_PRICE:.2f} in -10% to 30% range.")
    else:
        print(f"Reverse DCF: ${MARKET_PRICE:.2f} implies {implied_growth:.2%} annual revenue growth, holding other base inputs fixed.")
    validation = validation_tests()
    print(f"Training known answer: ${validation['training_value']:.2f}; 11% WACC probe: ${validation['training_wacc_probe']:.2f}; all checks: PASS")


if __name__ == "__main__":
    main()
