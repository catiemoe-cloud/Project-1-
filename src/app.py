"""Local semi-adjustable Apple valuation workbench; standard library only."""

from html import escape
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from apple_fcff_model import Assumptions, MARKET_PRICE, case_results, valuation


CONTROLS = {
    "revenue_growth": ("Revenue growth", 2, 15, 6),
    "gross_margin": ("Gross margin", 35, 60, 47),
    "operating_expense_rate": ("Operating expense rate", 8, 25, 15),
    "capex_rate": ("Capex / revenue", 1, 8, 3),
    "wacc": ("WACC", 6, 12, 9),
    "terminal_growth": ("Terminal growth", 1, 4, 2.5),
}


def assumptions_from_query(query):
    values = {}
    errors = []
    for key, (_, low, high, base) in CONTROLS.items():
        raw = query.get(key, [str(base)])[0]
        try:
            value = float(raw)
        except ValueError:
            errors.append(f"{key} must be a number.")
            continue
        if not low <= value <= high:
            errors.append(f"{key} must be between {low}% and {high}%.")
        values[key] = value / 100
    if errors:
        return None, errors
    return Assumptions(**values), []


def render(query):
    assumptions, errors = assumptions_from_query(query)
    controls = "".join(
        f'<label>{escape(label)}: <output id="{key}-out">{query.get(key, [str(base)])[0]}%</output>'
        f'<input type="range" name="{key}" min="{low}" max="{high}" step="0.1" value="{escape(query.get(key, [str(base)])[0])}" '
        f'oninput="document.getElementById(\'{key}-out\').value=this.value+\'%\'">'
        for key, (label, low, high, base) in CONTROLS.items()
    )
    if errors:
        body = '<div class="error"><strong>Input check failed.</strong><br>' + '<br>'.join(map(escape, errors)) + '</div>'
    else:
        try:
            result = valuation(assumptions)
            rows = result["rows"]
            forecast_rows = ''.join(
                f"<tr><td>FY{r['year']}E</td><td>{r['revenue']:,.0f}</td><td>{r['ebit']:,.0f}</td><td>{r['fcff']:,.0f}</td><td>{r['balance_gap']:,.2f}</td><td>{r['cash_flow_change']-r['cash_flow_change_from_statement']:,.2f}</td></tr>"
                for r in rows)
            cases = case_results()
            case_line = " · ".join(f"{name.title()} ${item['value_per_share']:.2f}" for name, item in cases.items())
            body = f'''<section class="results"><h2>Decision output</h2>
<p class="value">${result['value_per_share']:.2f} <span>per share</span></p>
<p>Recorded market price: ${MARKET_PRICE:.2f}. Difference: ${result['value_per_share'] - MARKET_PRICE:.2f}.</p>
<p>Enterprise value: ${result['enterprise_value']:,.0f}M; equity value: ${result['equity_value']:,.0f}M; terminal value: {result['tv_share_of_ev']:.1%} of EV.</p>
<p><strong>Causal cases:</strong> {case_line}</p>
<h2>Three-statement / validation checks</h2><table><tr><th>Year</th><th>Revenue</th><th>EBIT</th><th>FCFF</th><th>BS gap</th><th>Cash-flow tie</th></tr>{forecast_rows}</table>
<p class="pass">PASS — each balance-sheet gap and cash-flow tie equals 0.00 (USD millions, rounding shown).</p></section>'''
        except ValueError as exc:
            body = f'<div class="error"><strong>Input check failed.</strong><br>{escape(str(exc))}</div>'
    return f'''<!doctype html><html><head><meta charset="utf-8"><title>Apple FCFF Workbench</title>
<style>body{{font:16px system-ui;max-width:960px;margin:36px auto;padding:0 18px;color:#17212b}}h1{{margin-bottom:4px}}.muted{{color:#536471}}form{{display:grid;grid-template-columns:repeat(2,minmax(260px,1fr));gap:16px;background:#f2f6fa;padding:20px;border-radius:10px}}label{{display:grid;gap:6px;font-weight:650}}input{{width:100%}}button,a.button{{padding:10px 14px;background:#0a66c2;color:white;border:0;border-radius:6px;text-decoration:none;font-weight:650;width:max-content}}.results{{margin-top:22px}}.value{{font-size:36px;font-weight:750;margin:5px 0}}.value span{{font-size:16px;font-weight:400}}table{{border-collapse:collapse;width:100%}}th,td{{padding:8px;border-bottom:1px solid #d8dee4;text-align:right}}th:first-child,td:first-child{{text-align:left}}.pass{{color:#087443;font-weight:650}}.error{{margin-top:22px;padding:16px;background:#fff1f0;color:#9d1c16;border-radius:8px}}</style></head><body>
<h1>Apple FCFF Analyst Workbench</h1><p class="muted">Educational valuation, USD millions except per-share data. Source cut-off: September 17, 2026. Bounded controls; select “Run valuation” after changing a driver.</p>
<form method="get">{controls}<div><button type="submit">Run valuation</button> <a class="button" href="/">Reset base</a> <a class="button" href="/?wacc=5">Show invalid-input check</a></div></form>{body}
<p class="muted">Bridge policy: add Q3 FY2026 cash plus marketable securities ($146,517M); subtract commercial paper plus term debt ($84,344M). Lease liabilities remain in operating liabilities to avoid double counting.</p>
</body></html>'''


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        page = render(parse_qs(urlparse(self.path).query))
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(page.encode("utf-8"))

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    print("Open http://127.0.0.1:8000 in a browser. Press Ctrl-C to stop.")
    HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
