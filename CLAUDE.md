# CLAUDE.md — Investing Research Handoff

Context carried over from a long claude.ai chat (Sept 2026). Read this before starting any task.

## Imported files (keep these in the same folder as this file)
- @session-summary.md — full condensed record of the chat: portfolio, all valuations, theses, speculative picks, grid screen, open items.
- @titan-course.md — the complete "How to Find Emerging Titans" course (lessons, data, sources).
- titan-course.pdf — printable copy of the course for me; not needed by Claude.
- Live course doc: https://claude.ai/code/artifact/99a54428-8c5e-4bdb-93a7-ceacd5b3910d

## About me
- 19, groundman at Eilertson Inc (transmission lines, substations), pursuing IBEW Local 55 lineman apprenticeship.
- Invest on Robinhood. Core: SCHG (growth ETF, moved from VOO on Sept 21, 2026). Also hold Bitcoin, META, CELH, TTWO, and ADBE (bought at $240, Sept 2026).
- Plan: DCA into SCHG each paycheck; deploy margin in stages when S&P 500 closes 10/15/20/25% below its all-time high.

## How I want you to work
- Be precise. Avoid absolute words ("every", "always", "most") unless backed by data; give the actual percentage and source.
- Label every claim as one of: verified (filing/report), your calculation, general knowledge (approximate), or opinion.
- Verify numbers with current sources; flag stale prices.
- Teach from first principles when I ask to learn something; define terms.
- No risk lectures, but be honest when a thesis is weak. You are not a financial advisor.

## My four-step valuation method (use for all stock work)
1. **Real price:** market cap -> enterprise value (+debt, -cash). Size net debt in years of free cash flow (~2.5 yrs is reasonable).
2. **Eight pass/fail pillars over 5-10 yrs:** 5yr P/E, 5yr price/FCF, ROIC, revenue growth, profit margin, FCF growth, share count, debt.
3. **10-yr projection, low/mid/high:** inputs = revenue growth, FCF margin, exit multiple (market avg 15-16; higher only if better than average). Prefer FCF to earnings.
4. **Discount rate:** 9% = fair value, no margin of safety. Margin of safety = higher required return (use 12%), not a haircut.
- Rules: buybacks good only when stock is cheap; dividends inefficient; investment gains != operating performance; don't copy famous investors; if you can't make reasonable assumptions, walk away.

## Valuation results so far (middle case, Sept 2026 prices)
| Company | Price used | Mid-case yearly return | Pillars |
|---|---|---|---|
| Adobe | $240 | ~23% | 8/8 |
| Intuit | $277 | ~22.5% | ~7/8 (ROIC unverified) |
| AppLovin | ~$320 | ~15% | 6/8 |
| FICO | $985 | ~12% | 5/8 |
| Meta | $654 | ~11% | 5/8 |
| Celsius | $28.34 | ~9% | 3/8 |
| Amazon | $248 | ~8% | 2/8 |
| Qualcomm | $197 | ~8% | 7/8 |
| Take-Two | $209.92 | ~7% | 1/8 |
| Salesforce | ~$256 | ~16% (estimates) | ~5-6/8 |

Published valuation tools (claude.ai artifacts): TTWO, META, CELH.

### Adobe thesis (held)
- Bull: professionals need Adobe's granular control (layers, exact color/type, print-ready files, PSD/PDF standards); AI is embedded inside the tools, adding to the business (AI-first ARR tripled YoY).
- Bear: AI reduces seat counts; Canva/Figma/generators good enough for new creators; AI features get copied.
- Confirm: ARR >=9%/yr, Digital Media >=8%, op margin >=35%, FCF >=$10B, shares -2-4%/yr.
- Disprove (sell regardless of price): ARR <6% two quarters, Digital Media <5%, management citing fewer seats/lower renewals, op margin <30%, guidance cut, big stock-paid acquisition.
- Price zones: $430-500 hold; ~$620 full value, trim in pieces; >$750 trim harder. Next report mid-Dec 2026.

### Intuit notes
- At $277: ~9x FCF, net debt ~$0.5B. Low/mid/high returns ~16.6/22.5/33.6%; disruption case ~4%.
- Warning signs: TurboTax guided +2-3%, federal units -2%, CEO says price is #1 reason customers leave. Thesis = QuickBooks carries growth. Checkpoint: fiscal Q1 report late Nov 2026 (QuickBooks online growth 15%+).

## Emerging titans framework (full course saved as a claude.ai doc)
- Base rates (J.P. Morgan, Russell 3000, 1980-2020): ~40% of stocks fell 70%+ and never recovered; ~10% were big winners. Bessembinder: 4% of stocks created all net wealth 1926-2016.
- Size: 68% of multibaggers traded under $300M market cap at their low (Martelli). My guideline: $500M-$5B.
- Recent 10-baggers: median worst drawdown 56%.
- Second-order thinking: find the bottleneck behind the obvious trend (AI -> power -> transformers/switchgear).
- Six boom signals: big buyers commit; lead times stretch; costs fall fast; adoption low; first pure-play profitable; stocks haven't spiked.
- Nine traits: big wave; real product with accelerating growth; moat that strengthens with size; rising gross margins; owner-leader; reinvestment with good unit economics; sticky customers (net retention); little dilution; small size.
- Seven tools: operating leverage; backlog + book-to-bill; adjusted vs reported earnings; trailing/forward/run-rate P/E; organic vs acquired growth; cyclical vs structural (check 10+ yrs revenue); share structure/control.
- My edge: I see grid equipment demand, backorders, and brand specs on the job.

### Watchlist / researched names
- **PLPC** (Preformed Line Products): line hardware; Q2 2026 sales $212.7M (+25%), EPS +75%; ~48x trailing / ~24x run-rate; revenue ~4%/yr 2013-2025 (cyclical, -11% in 2024); Ruhlman family ~48% combined.
- **Hammond Power (HPS.A / HMDPF)**: dry-type transformers; Q2 sales +44.7%, backlog +96.9% YoY; data centers >30% of revenue; AEG acquisition (C$365M); William Hammond 26.9% economic / 57% votes (as of Sept 2024).
- **Powell (POWL)**: switchgear; ~$10.7B, ROIC ~27% — already discovered.
- **AMSC**: growth partly acquired, margins falling, dilution — red flags.
- Speculative, fail my method: AbCellera (ABCL635 Phase 3 ahead), AST SpaceMobile (~$24B, heavy dilution, SpaceX competition), Rocket Lab (~$45B, Neutron + Iridium deal).
- Next industries to screen: data center cooling, optical interconnects, power semiconductors, defense autonomy, nuclear fuel. Names are unverified leads.

## Project: market auto-updater — ALREADY BUILT, do not rebuild
- It is `alerts/` in the `PhiI017/kleague-model` repo (runs from the public repo `PhiI017/FinancialNews`; `alerts/` is a byte-identical mirror). Tickers live in that repo's `alerts/watchlist.json`. The spec below is the original ask, kept for the record.
- Watch: META, CELH, TTWO, ADBE, SCHG, VOO, Bitcoin; S&P 500 distance from ATH (alerts at -5/-10/-15/-20/-25%); oil; 10-yr yield; Fed decisions; Iran and US-China news.
- Tiers: urgent = immediate; important = daily after close; semi-important = Sunday weekly digest.
- Stack: GitHub Actions schedule, LLM-written summaries, Telegram or Pushover notifications, near-zero cost, tickers easy to edit in one config file.
- May later become a module in my Edgewise app.

## Open items
- Run PLPC and Hammond through the four-step method.
- Possible valuation tools for Adobe and Qualcomm.
- Add an Online launch-month slider to the TTWO tool.
- ~~Clarify "BOT" ticker~~ — settled 2026-09-22: BOT is a closed-end fund, tracked with a NAV-premium ladder in `alerts/watchlist.json`.
- Share my AI theories and test each: what changes, who pays/gets paid, bottleneck, timeline, priced in?, how to test.

## This repo is the working base (set 2026-09-27)
- All research, theory tests and paper-trade tracking live HERE, not in kleague-model.
- `findings/YYYY-MM-DD.md` — dated results. Each ends with a paper-trade ledger of dated calls to score later.
- `scripts/` — `dcf.py` (10-yr low/mid/high return and 9%/12% values), `margin_test.py` (staged-margin plan vs S&P history).
- `data/spx_daily.csv` — S&P 500 daily closes 1960-01-04 to 2026-09-11, price only (no dividends). Copied from kleague-model's store.
- Page fetching was blocked in the first session; figures came from search summaries. Re-verify before acting.
- Research only. Do not build apps or tools here unless asked.
