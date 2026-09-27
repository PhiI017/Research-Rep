"""Latest quote per ticker from Yahoo, including pre-market and after-hours.

Usage: python3 scripts/quote.py ALNT BKNG ...
Prints: ticker, latest price, its UTC time, session, and the regular-session close.
Yahoo does NOT carry Robinhood's overnight/weekend (24-hour market) trades; for those, the
Robinhood app is the only current source.
"""
import json, sys, urllib.request, datetime as dt

URL = "https://query1.finance.yahoo.com/v8/finance/chart/{}?range=5d&interval=5m&includePrePost=true"


def quote(sym):
    req = urllib.request.Request(URL.format(sym), headers={"User-Agent": "Mozilla/5.0"})
    r = json.load(urllib.request.urlopen(req, timeout=15))["chart"]["result"][0]
    m = r["meta"]
    bars = [(t, c) for t, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]) if c]
    t, last = bars[-1]
    reg_t = m["regularMarketTime"]
    session = "regular" if t <= reg_t else "after-hours"
    when = dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return sym, round(last, 2), when, session, m["regularMarketPrice"]


if __name__ == "__main__":
    for s in sys.argv[1:]:
        try:
            print("%-6s %9.2f  %s  %-11s close %.2f" % quote(s))
        except Exception as e:  # say where it stopped, never a bare blank
            print("%-6s FAILED: %s" % (s, e))
