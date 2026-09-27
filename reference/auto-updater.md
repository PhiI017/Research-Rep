## Project: market auto-updater — ALREADY BUILT, do not rebuild
- It is `alerts/` in the `PhiI017/kleague-model` repo (runs from the public repo `PhiI017/FinancialNews`; `alerts/` is a byte-identical mirror). Tickers live in that repo's `alerts/watchlist.json`. The spec below is the original ask, kept for the record.
- Watch: META, CELH, TTWO, ADBE, SCHG, VOO, Bitcoin; S&P 500 distance from ATH (alerts at -5/-10/-15/-20/-25%); oil; 10-yr yield; Fed decisions; Iran and US-China news.
- Tiers: urgent = immediate; important = daily after close; semi-important = Sunday weekly digest.
- Stack: GitHub Actions schedule, LLM-written summaries, Telegram or Pushover notifications, near-zero cost, tickers easy to edit in one config file.
- May later become a module in my Edgewise app.

