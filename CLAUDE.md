# CLAUDE.md — Investing research

Pointers only. Open a file when the task needs it.

## Where things are
- `reference/method.md` — the four-step valuation method. **Read before any stock valuation.**
- `reference/valuations.md` — Sept 2026 results, Adobe thesis, Intuit notes.
- `reference/titans-framework.md` — titans data, signals, traits, tools, grid watchlist.
- `reference/open-items.md` — open research items.
- `reference/auto-updater.md` — the alerter spec; ALREADY BUILT in `PhiI017/kleague-model` `alerts/`, do not rebuild.
- `session-summary.md` — condensed record of the original claude.ai chat.
- `titan-course.md` — the full course (`.pdf` is the user's printable copy). Live doc: https://claude.ai/code/artifact/99a54428-8c5e-4bdb-93a7-ceacd5b3910d

## About me
- 19, groundman at Eilertson Inc (transmission lines, substations), pursuing IBEW Local 55 lineman apprenticeship.
- Invest on Robinhood. Core: SCHG (growth ETF, moved from VOO on Sept 21, 2026). Also hold Bitcoin, META, CELH, TTWO, and ADBE (bought at $240, Sept 2026).
- Plan: DCA into SCHG each paycheck; deploy margin in stages when S&P 500 closes 10/15/20/25% below its all-time high.

## How I want you to work
- Be precise. Avoid absolute words ("every", "always", "most") unless backed by data; give the actual percentage and source.
- Label every claim: [S] read directly from a primary source by a script (`quote.py`, `shares.py`) · [V] reported as from a filing/release but not read · [C] calculation · [G] approximate · [O] opinion.
- Valuation runs: ONE exit multiple for every stock (16x, the user's market-average rule), always shown with 12x and 20x; share counts from SEC cover pages (`shares.py`), never from summaries. A base case inside the 12x-20x band of another is not a ranking difference.
- Verify numbers with current sources; flag stale prices.
- **Prices must be CURRENT, including after-hours, overnight and weekend trading** (the user trades on Robinhood, which runs 24-hour sessions). Fetch a fresh quote before using a price, state its time and session (regular / after-hours / overnight), and re-run any valuation whose price moved. A last close is not "current".
- Teach from first principles when I ask to learn something; define terms.
- No risk lectures, but be honest when a thesis is weak. You are not a financial advisor.

## Context is a budget, not a buffer (user's rule, 2026-09-27)
Everything added is re-sent every later turn, so early additions cost most.
1. Edit files with the edit tool (old text → new text). No read-replace-write scripts; never rewrite a whole file to change part.
2. Read slices: grep with line numbers, then read only the range needed.
3. Never poll or sleep; use a waiting primitive or a scheduled check-in.
4. Ask every tool for the least output: summaries, small pages, tails, fields.
5. Big one-off reads (transcripts, logs, wide searches) go to a subagent; keep only its conclusion.
6. Don't verify what a tool already confirmed; don't read back an edit.
7. Say a result once; don't restate command output or summarise a summary.
8. Keep this file short and pointer-shaped; detail goes in files opened only when needed.
9. When the job changes, start a new conversation.
10. Before adding more than a few thousand characters in one call, say in one line why it can't live in a file or subagent.

## This repo is the working base (set 2026-09-27)
- All research, theory tests and paper-trade tracking live HERE, not in kleague-model.
- `titan-class-notes.md` — the condensed class notes, the Tier A/B watchlist, and the six questions every AI theory goes through. **Start here for titan work.**
- `theses/REGISTER.md` — every thesis, its status, its test, and its break condition. Robotics is PINNED there. `theses/thoughts-*.md` are the user's raw notes, word for word.
- `findings/YYYY-MM-DD.md` — dated results. Each ends with a paper-trade ledger of dated calls to score later.
- `scripts/` — `dcf.py` (10-yr low/mid/high return and 9%/12% values), `margin_test.py` (staged-margin plan vs S&P history), `quote.py` (latest price incl. after-hours — run before citing any price), `shares.py` (share counts from SEC cover pages; args TICKER=CIK).
- `data/spx_daily.csv` — S&P 500 daily closes 1960-01-04 to 2026-09-11, price only (no dividends). Copied from kleague-model's store.
- Page fetching was blocked in the first session; figures came from search summaries. Re-verify before acting.
- Research only. Do not build apps or tools here unless asked.
