"""Shares outstanding read directly from SEC filing cover pages (XBRL, dei namespace).

Usage: python3 scripts/shares.py ALNT BKNG ...
Prints the latest cover-page count per share class, its date and form, and the total.
Multi-class companies (e.g. Berkshire A/B) print each class; convert to one basis yourself.
SEC asks for a contact in the User-Agent: set SEC_CONTACT in the environment (never hardcode it).
"""
import json, os, sys, urllib.request

UA = {"User-Agent": "research-rep " + os.environ.get("SEC_CONTACT", "anonymous")}


def get(url):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20))


def cik_map():
    return {v["ticker"]: str(v["cik_str"]).zfill(10)
            for v in get("https://www.sec.gov/files/company_tickers.json").values()}


def shares(cik):
    d = get(f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/dei/EntityCommonStockSharesOutstanding.json")
    rows = d["units"]["shares"]
    last = max(r["end"] for r in rows)
    latest = [r for r in rows if r["end"] == last]
    # one row per class on the latest date; keep distinct filings' values once
    seen, out = set(), []
    for r in latest:
        key = (r.get("frame"), r["val"])
        if key not in seen:
            seen.add(key); out.append(r)
    return last, out


if __name__ == "__main__":
    # Args are TICKER=CIK (www.sec.gov's ticker map 403s without SEC_CONTACT; data.sec.gov answers).
    # Known CIKs: ALNT=46129 LASR=1124796 RCAT=748268 BKNG=1075531 JPM=19617 WMT=104169
    # MYRG=700923 HUBB=48898 PWR=1050915 UNH=731766 PEP=77476 ADBE=796343
    # Berkshire (1067983) has not tagged a cover-page count since 2011 — check its 10-Q by hand.
    for arg in sys.argv[1:]:
        t, _, c = arg.partition("=")
        if not c:
            print(f"{t:6s} FAILED: give TICKER=CIK"); continue
        cik = c.zfill(10)
        try:
            last, rows = shares(cik)
            # A company that stopped tagging returns its last-ever count (2009 for Comcast): refuse it.
            if last < "2025-10-01":
                print(f"{t:6s} STALE: latest cover-page count is {last}; company no longer tags it — use the 10-Q cover by hand")
                continue
            vals = [r["val"] for r in rows]
            print(f"{t:6s} {last}  {rows[0]['form']:5s} " + " + ".join(f"{v/1e6:,.2f}M" for v in vals)
                  + (f" = {sum(vals)/1e6:,.2f}M" if len(vals) > 1 else ""))
        except Exception as e:
            print(f"{t:6s} FAILED at cover-page fetch: {e}")
