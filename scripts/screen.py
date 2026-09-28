"""Run every name in an inputs CSV through dcf.py with ONE exit multiple (16x) plus 12x/20x.

Usage: python3 scripts/screen.py data/screen-inputs-YYYY-MM-DD.csv
A name PASSES only if its base case clears 12%/yr at 12x, 16x AND 20x (robust to the one
input that moves results most). CLEAR FAIL: base below 12% even at 20x. Anything else: UNRESOLVED.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from dcf import irr

BAR = 0.12
rows = list(csv.DictReader(open(sys.argv[1])))
out = []
for r in rows:
    f = lambda k: float(r[k])
    cap = f("shares_m") * f("price")
    run = lambda g, m, x: irr(f("rev0_musd"), g, m, x, f("net_cash_musd"), cap)
    base = {x: run(f("base_g"), f("base_m"), x) for x in (12, 16, 20)}
    bear, bull = run(f("bear_g"), f("bear_m"), 16), run(f("bull_g"), f("bull_m"), 16)
    verdict = "PASS" if base[12] > BAR else ("CLEAR FAIL" if base[20] < BAR else "UNRESOLVED")
    out.append((base[16], r["ticker"], r["category"], base[12], base[20], bear, bull, verdict))
for b16, t, c, b12, b20, be, bu, v in sorted(out, reverse=True):
    print(f"{t:6s} {c:11s} base@16x {100*b16:5.1f}%  (12x {100*b12:5.1f} / 20x {100*b20:5.1f})"
          f"  bear {100*be:6.1f}  bull {100*bu:5.1f}  {v}")
