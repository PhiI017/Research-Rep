# How the picks were made — full report, 2026-09-27

Companion to `2026-09-27-claude-picks.md` (the short version). This file explains the
process step by step, lists every number used and where it came from, and gives the full
thesis, bull case and bear case for each of the twelve stocks.

**Price note:** prices below are as the research helpers found them (9/20-9/26). Refreshed
latest trades and re-run base cases are in the ledger of `2026-09-27-claude-picks.md`; the
biggest moves were ALNT $109.35 → $116.01 and MYRG $279.28 → $292.58. No verdict changed.

**Labels:** [V] verified from a filing or company release · [C] my calculation ·
[G] general knowledge or an approximate figure from an aggregator · [O] opinion.
**Nothing here is financial advice.**

---

## Part 1 — The process

### Step 1: Split the search into four categories
You asked for four kinds of ideas, and each needs a different test:
1. **Emerging titans** — small companies ($500M-$5B) that could become large.
2. **Big AI implementers** — large companies that win by *using* AI, not selling it.
3. **Picks and shovels** — suppliers to the AI and electrification buildout.
4. **Outside AI** — ideas that do not depend on AI, because your portfolio already does.

### Step 2: One research helper per category
Each category went to a separate research helper (another instance of Claude working in this
session) so the wide web searches did not fill this conversation — your context rule 5. Each
helper got the same instructions: search only, pick the best 3, name 2 near-misses, label every
number, and return a compact report with sources. **I did not independently re-check each
number the helpers returned**; I kept their labels, and where something looked wrong I fixed or
flagged it (see Step 6).

### Step 3: Candidate lists and exclusions
- Titans: second-order bottlenecks behind AI and robotics (grid, cooling, optics, nuclear fuel,
  robot components, defense autonomy). Excluded names already screened: PLPC, Hammond, Powell,
  AMSC, AbCellera, AST SpaceMobile, Rocket Lab, Navitas, Applied Optoelectronics, Credo.
- Big AI users: market cap over $20B, excluding Amazon, Spotify, Duolingo, Meta and Adobe
  (already covered) and excluding chip sellers — the test is who *uses* AI.
- Picks and shovels: favoured names where **you** can see ground truth on the job
  (contractors, utility hardware), per your notes' "edge in small places".
- Outside AI: chosen for how they behaved in 2022 and past tech drawdowns, because of the
  fragility-window risk in your notes.

### Step 4: Your philosophies, turned into lenses
Every pick was judged through the lenses from your notes, one line each, with "no evidence
found" allowed:

| Lens | From your notes |
|---|---|
| Second-order bottleneck | "the early money goes to whoever supplies what the obvious story can't live without" |
| Distribution moat | "Distribution wins… whoever already owns distribution, manufacturing, logistics" |
| Measured AI savings | "earnings language showing costs falling because of internal AI" (Booking.com) — judged by numbers, not words |
| Keep vs. pass on | added after our airline discussion: do savings stay as margin? |
| Ground truth outside finance | "go to the people who actually work at these companies" |
| Asymmetry | "a 2x better chance than what it's priced" — upside vs. downside |
| Forced vs. fundamental | "selling caused by fundamental deterioration vs. forced liquidation" |
| Priced in / edge | the SpaceX note: stop when the edge is no longer something others don't see |
| Policy | "the US government won't let China overtake the US" |
| Cycle vs. structure | course Unit 4: check 10+ years of revenue |
| Fragility | "capital committed while returns are uncertain" |

### Step 5: The ten-year model (one lens among several)
Script: `scripts/dcf.py`. For each stock:
1. Start from base revenue (current-year guidance or trailing twelve months).
2. Grow it at rate *g* for 10 years.
3. Free cash flow each year = revenue × FCF margin.
4. After year 10, sell the business at an exit multiple × year-10 FCF.
5. Add net cash (or subtract net debt).
6. Solve for the yearly return that makes all of that equal to today's market cap.

Three sets of inputs per stock — bear, base, bull (growth, FCF margin, exit multiple) — came
from the helpers, anchored on each company's own history. **The bar is your 12%: a stock
"passes" if its base case beats 12% a year.** I also used your 9% fair-value and 12%
margin-of-safety prices where useful.

**Two different numbers appear below, and they are not the same thing:**
- **10-year return** — my calculation from `dcf.py`.
- **2030 price** — the helper's four-year estimate of where the price could be in the bull or
  bear case.

### Step 6: Corrections I made
- **Red Cat:** the helper's growth rates (60-85% a year) were four-year rates. Compounded for
  ten years they imply $8B+ revenue from $72M, which is not credible. I re-ran it with ten-year
  rates (15/32/45%) and added 30% more shares for continued dilution.
- **Booking:** the $163.95 price and 751M shares imply a stock split I could not confirm.
  Market cap (~$123B) is consistent, so the return math holds, but verify the per-share price.
- **Duolingo, from earlier:** counted stock-based pay as a cost, which moved the base case from
  22.5% to 13.6%. The same principle is why I did not use "adjusted" figures as the main case.

### Step 7: Verdict rules
- **Short list:** base case near or above 12%, plus at least one lens that gives you an edge
  others don't have (measured savings, forced selling, your job, or portfolio hedge).
- **Watchlist:** right thesis, price already reflects it — buy on a drop.
- **Priced in / fails:** thesis working but base case well under 12%.

### Limits you should know
- Page fetching was blocked in this environment; all figures came through search-result
  summaries. [G] figures in particular should be checked against a filing before buying.
- Prices are from 9/20-9/27/2026 and go stale.
- The scenarios are judgement calls. Changing an exit multiple from 20x to 25x moves a result
  by several points a year.

---

## Part 2 — The stocks

### Category 1: Emerging titans

#### ALNT — Allient · watchlist (Tier B)
**Data:** price $109.35 on 9/21/2026 [G]; 17.0M shares [G]; market cap ~$1.86B [G]; net debt
$131M [V]. Revenue $554.5M FY2025 [V], ~$582M trailing [C]. Growth accelerated from +4.6%
(FY25) to +10% (Q2 2026) [V]; bookings +49%; backlog $298M, +26% [V]. Gross margin 34.9% vs
33.2% [V]. FCF ~$48M FY25 (operating cash flow $56.7M minus capex) [C]. CEO Dick Warzala owns
~9.9% [G] and sold 70,000 shares in August [V]. Revenue ~$246M in 2016 [G], grown partly
through acquisitions, with dips in 2020 and 2024 [G].

**Lenses:** bottleneck — humanoid and industrial robots need compact, high-torque motors and
actuators; data-center power quality is a second leg. Ground truth — record bookings [V], humanoid
motor white paper and Robotics Summit demos (trade press); no lead-time evidence found. Priced in
— re-rated to ~38x FCF [C]. Policy — tariffs cut both ways; defense demand helps. Cycle —
cyclical history.

**Thesis:** Robots are the pinned research theme, and every robot is built from motors, drives
and actuators. Allient already sells them, its order book is accelerating, margins are rising,
and the CEO owns a real stake. If robotics scales, Allient is re-rated from a cyclical industrial
into a robotics bottleneck.

**Bull case:** growth 16% a year, FCF margin 12%, exit 28x → **~20% a year** [C]; 2030 price
~$216 [helper]. Requires robotics orders to become a large share of sales.
**Bear case:** growth 4%, FCF margin 8%, exit 16x → **about -2% a year** [C]; 2030 price ~$45
[helper]. The industrial cycle turns and robotics stays a small niche.
**Base case:** 10% / 10% / 22x → **9.2% a year** [C]. Fair value at 12% ≈ $86 [C].
**Break condition:** bookings below sales for two straight quarters.
**Sources:** [Q2 2026 call highlights](https://www.gurufocus.com/news/9014207/allient-inc-alnt-q2-2026-earnings-call-highlights-record-bookings-and-gross-margin-fuel-strong-growth-outlook) · [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0000046129/000110465926091098/alnt-20260630x10q.htm)

#### LASR — nLIGHT · watchlist (Tier B), asymmetric
**Data:** $40.00 on 9/26/2026 [G]; ~58M shares [G]; ~$2.33B [G]; net cash $331M, no debt [V].
Revenue $261.3M FY25, +32% [V]; ~$310M trailing [C]; Q2 +34%, defense +72% [V]. Q3 guide cut to
$63-73M because China-sourced parts delayed $17M of shipments [V]. Gross margin 31.1% vs 29.9%;
product gross margin 41.2% [V]. Record operating cash flow $20.7M in Q2 [V]. Founder-CEO Scott
Keeney ~3.8% [V/C], sold $16.5M in August [V]. Laser-weapon (JLWS) contract ceiling $600M+ [V].
Commercial revenue ~$270M (2021) → ~$198M (2024) [G].

**Lenses:** bottleneck — shooting down cheap drones with missiles is too expensive; lasers are
the answer, and nLIGHT makes the laser source. Policy — counter-drone and missile-defense budgets
rising. Cycle — commercial side cyclical, defense side looks structural. Forced/fundamental — fell
on a real guide cut.

**Thesis:** Defense is turning a cyclical industrial-laser maker into the supplier of the core
component of directed-energy weapons, with a debt-free balance sheet.
**Bull:** 28% growth, 18% FCF margin, 30x → **~30% a year** [C]; 2030 ~$83 [helper].
**Bear:** 5%, 5%, 15x → **about -13% a year** [C]; 2030 ~$10 [helper] — commercial slump plus
program delays.
**Base:** 18% / 12% / 25x → **12.5% a year** [C], just over your bar.
**Break:** defense growth below 15%, or the China-parts delay repeats.
**Sources:** [Q2 2026 release](https://s23.q4cdn.com/868502988/files/doc_financials/2026/q2/v2/nLIGHT-Q2-Earnings-Release_FINAL.pdf) · [Q2 slides](https://www.investing.com/news/company-news/nlight-q2-2026-slides-defense-drives-record-despite-outlook-cut-93CH-4844767) · [CEO sale](https://www.fool.com/coverage/filings/2026/08/25/nlight-s-ceo-sells-over-360-000-shares-for-usd16-5-million-as-the-stock-drops-post-earnings/)

#### RCAT — Red Cat · lottery ticket only
**Data:** $6.70 on 9/27/2026 [G]; 152.7M shares [G]; ~$1.02B [G]; cash $325.6M [V], debt not
confirmed. Revenue $40.7M FY25 [V]; ~$72M trailing [C]; Q1 +849%, Q2 +527% [V]; FY26 guide
$150-180M [V], which needs ~$115-145M in the second half [C]. Gross margin 3.1% (FY25) → 16.1%
(Q2) [V]. Operating cash burn $78.7M in H1 [V]. CEO Jeff Thompson ~7.7% [V/C]. Shares +36% in a
year [G].

**Lenses:** policy — the Pentagon needs non-Chinese (non-DJI) drones; strong tailwind. Ground
truth — NATO-ally orders [V]; no backorder evidence. Priced in — heavily followed by retail.
Cycle — no history (pivoted ~2021).

**Thesis:** Red Cat holds the Army's program of record for small reconnaissance drones, and
margins are finally turning. If it executes, it becomes the default US small-drone supplier.
**Bull:** 45% growth for 10 years, 12% FCF margin, 25x (with 30% more shares) → **~27% a
year** [C]; 2030 ~$13 [helper].
**Bear:** 15%, 3%, 12x → **about -18% a year** [C]; 2030 under $1 [helper] — the second-half
guide is missed and dilution continues.
**Base:** 32% / 8% / 20x → **8.6% a year** [C].
**Break:** FY26 revenue under $120M, or another equity raise.
**Sources:** [Q2 2026 release](https://ir.redcatholdings.com/news-events/press-releases/detail/237/red-cat-reports-q2-2026-revenue-growth-of-527-yy-q2-gross-margins-increase-39-vs-q2-2025-gross-margins-increased-27-sequentially-from-q1-2026)

Near-misses: **Centrus (LEU)** ~$3.1B, $4.5B backlog [V] but flat revenue ($448.7M FY25, guide
$425-475M [V]), no owner-leader, $1.2B converts ([Q2 release](https://investors.centrusenergy.com/news-releases/news-release-details/centrus-reports-second-quarter-2026-results)).
**Clearfield (CLFD)** gross margin 35.3% → 31.8% and guidance cut [V] ([Q3 FY26 release](https://ir.seeclearfield.com/news-events/press-releases/detail/364/clearfield-reports-third-quarter-fiscal-2026-results)).

### Category 2: Big companies winning from AI implementation

#### BKNG — Booking Holdings · SHORT LIST #1
**Data:** $163.95 on 9/25/2026, post-split [G — verify]; 751M shares [G]; ~$123B [G]; cash
$17.2B [V], net debt ~$10B [G, debt not confirmed]. Revenue $26.92B FY25 [V], ~$28.5B trailing
[G]. Operating margin ~21% (FY21) → 28% → 30% → 32% → 34.5% (FY25) [G/V]; Q2 2026 34.0%, +91bp
[V]. FCF $9.09B FY25 [V]. Customer-service cost fell year on year while volume grew 10% [V];
voice AI takes most inbound calls; cost per booking falling at a double-digit rate [V]; savings
target raised $550M → $650M [V]; operating costs +7%, slower than revenue [V]. P/E 17.2 vs
10-year median 31.6 [V]. AI-assistant referrals under 1% of room nights [V].

**Lenses:** distribution — millions of hotels, repeat direct traffic, loyalty and payments data.
Measured savings — the strongest found; low AI-washing risk. Keep vs. pass on — margin up five
years running, so it has kept them. Ground truth — call-center outsourcers (Teleperformance,
Concentrix) losing volume to clients' in-house AI [G]. Priced in — no; below its own history.
Fragility — low on AI capex; the real risk is AI assistants owning trip search.

**Thesis:** Booking is the textbook case of your AI-implementation signal: a named cost line
visibly bent by its own AI, a distribution moat AI does not copy, savings kept as margin, and a
price below its own history. It is a cash machine that buys back ~4% of its shares a year.
**Bull:** 11% growth, 36% FCF margin, 22x → **~24% a year** [C]; 2030 ~$515 [helper] — savings
plus buybacks.
**Bear:** 3%, 26%, 12x → **~5.7% a year** [C]; 2030 ~$143 [helper] — AI assistants win the
search step and push the commission rate down.
**Base:** 8% / 33% / 18x → **17.6% a year** [C]. Fair value at 12% ≈ $246/share [C].
**Break:** commission (take) rate falls two years running, or AI referrals pass 10% of room nights.
**Sources:** [Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0001075531/000107553126000036/q2-26bkngearningsrelease.htm) · [AI cuts customer-service costs](https://www.pymnts.com/earnings/2026/ai-cuts-booking-holdings-customer-service-costs-10-as-volumes-rise/) · [P/E history](https://www.gurufocus.com/term/pettm/BKNG)

#### JPM — JPMorgan Chase · thesis right, priced in
**Data:** $343.10 on 9/27/2026 [G]; ~$942B [G]; ~2,745M shares [C]. Price/tangible book 3.27x
vs 10-year median 2.0x [V]. Revenue ~$185B FY25 [G], ~$195B trailing [G]. Overhead ratio ~59%
(FY21) → 52% (FY25) → 47% (Q2 2026) [G/V]. Net income $57B FY25 [V]. Management cites $2B saved
from AI [V]; accounts per operations employee +25%, servicing calls per account -30%, processing
cost -15% [V]; headcount guided -10% over five years while the business grows 25%+ [V]; ~150,000
staff use AI weekly, ~4 hours saved each [V]. 2026 expense guide still rises to $107.5B [V].

**Thesis:** JPMorgan has the best measured AI productivity of any big bank, protected by
deposits, balance sheet and regulatory licenses — but the valuation already assumes it.
**Bull:** 7% growth, 32% net margin, 16x, buybacks to 2,400M shares → 2030 ~$545 [helper].
**Bear:** 1%, 24%, 10x → 2030 ~$187 [helper] — credit cycle plus a lower multiple.
**Base:** 2030 ~$365 [helper] — roughly today's price plus dividends. (A bank isn't modelled on
FCF, so no `dcf.py` run.)
**Break:** headcount rises while revenue is flat, or the overhead ratio returns above 55%.
**Sources:** [Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0000019617/000162828026048078/a2q26erfexhibit991narrative.htm) · [headcount guide](https://www.theglobeandmail.com/investing/markets/stocks/JPM/pressreleases/32477655/ai-efficiency-to-trim-jpmorgan-jpm-headcount-by-10-over-five-years/)

#### WMT — Walmart · thesis working, stock fails
**Data:** ~$107 [C, from $853.6B market cap on 9/24 [G]]; net debt ~$40B ex-leases [G].
Revenue $713B FY26 [V], ~$730B trailing [G]. Operating margin ~4.5%, 3.3%, 4.2%, 4.3%, 4.18%
FY22-26 [G/V]. FCF $14.9B FY26 [V]. Headcount flat at 2.1M for three years while sales grow [V];
60% of stores fed by automated distribution centers [V]; shopping agent (Sparky) live [V].
P/E ~40 vs 5-year average ~28 [G].

**Thesis:** Walmart proves AI and automation let a giant grow without adding people — but its
everyday-low-price model passes savings to shoppers (flat margin for five years), and the stock
already trades at a premium.
**Bull:** 6%, 3.5% FCF margin, 38x → **~9.8% a year** [C]; 2030 ~$156 [helper] — advertising
and membership lift the mix.
**Bear:** 3%, 2.0%, 22x → **about -4.3% a year** [C]; 2030 ~$41 [helper] — the multiple
returns to normal.
**Base:** 4.5% / 2.6% / 30x → **2.6% a year** [C].
**Break:** operating margin still under 4.5% by FY28.
**Sources:** [FY26 Q4 release](https://www.sec.gov/Archives/edgar/data/104169/000010416926000032/earningsreleasefy26q4.htm) · [growing without adding staff](https://finance.yahoo.com/news/walmart-plans-grow-revenue-without-223146661.html)

Rejected: **Uber** — its 2026 AI budget was used up in four months and net margin fell from 27%
to 17.3% ([Fortune](https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/)).

### Category 3: Picks and shovels

#### MYRG — MYR Group · SHORT LIST #2
**Data:** $279.28 on 9/20/2026 [V, Reuters close]; ~15.6M shares [C]; ~$4.35B [G]; net cash
$91M at year-end 2025 [V], then $328M paid for Valley/Comet [V] → net debt ~$200M [G]. Revenue
$3.66B FY25 [V], ~$4.0B trailing [G]. Backlog $3.16B, +19.6% [V]; transmission & distribution
share $1.27B [V]; commercial & industrial ~60% of backlog [C]. C&I operating-margin guide raised
to 5-7.5% [V]. Q4 2025 FCF $85M [V]. P/E ~26x trailing, ~23x forward [G/C]. Down ~45% from a
$503.57 high [G] in a sector-wide selloff with AGX, LGN, ECG [G]. Margin problems in 2024 [G].

**Lenses:** bottleneck — skilled linemen and electricians, the scarcest input in the buildout.
Ground truth — **your job**: watch whether its subsidiaries (Sturgeon Electric, Great
Southwestern, Harlan Electric) are winning bids or hiring journeymen near you. Forced vs.
fundamental — backlog rising while the stock fell 45% points to forced/sector selling, **but
the reason was not confirmed — check before buying.** Cycle — cyclical. Policy — permitting
delays on big transmission lines.

**Thesis:** The purest play on the labor bottleneck behind the grid buildout, possibly bought
after a crowded-trade flush, in the one industry where you have a real information edge.
**Bull:** 13% growth, 5.5% FCF margin, 22x → **~20% a year** [C]; 2030 ~$565 [helper].
**Bear:** 4%, 3.5%, 13x → **~0.6% a year** [C]; 2030 ~$134 [helper] — a data-center pause hits
C&I and margins slip again.
**Base:** 9% / 4.5% / 18x → **11.3% a year** [C]; fair value at 12% ≈ $265 [C].
**Break:** transmission & distribution backlog shrinks, or another project write-down.
**Sources:** [Q2 2026 results](https://www.globenewswire.com/news-release/2026/07/29/3335606/10748/en/myr-group-inc-announces-second-quarter-and-first-half-2026-results.html) · [FY2025 results](https://www.globenewswire.com/news-release/2026/02/25/3245028/10748/en/MYR-Group-Inc-Announces-Fourth-Quarter-and-Full-Year-2025-Results.html) · [sector selloff](https://news.alphastreet.com/myr-group-drops-6-7-amid-sector-wide-selling/amp/)

#### HUBB — Hubbell · fair, not cheap
**Data:** $466.62 on 9/26/2026 [G]; ~52.7M shares [C]; ~$24.6B [G]; long-term debt $4.80B at
6/30 after the $3.0B NSI deal [V], net debt ~$5B [G]. Revenue $5.8B FY25 [V], ~$6.2B trailing
[G]; 2026 guide +16-18% [V]. Utility segment adjusted operating margin 25.5% → 25.6% [V]; Grid
Infrastructure +12% [V]. FCF $874.7M FY25 [V]. P/E ~22.9x 2026 adjusted EPS of $20.40 [C] vs
5-year average ~22-25x [G]; EV/FCF ~30x [C]; 52-week range $404-566 [G].

**Thesis:** A toll on every utility dollar — pole-line and substation hardware (Chance, DMC
connectors) — at a near-average multiple. Low forced-selling risk because it isn't traded as an
AI-power momentum name. Ground truth: is Hubbell/Chance/DMC hardware backordered on your trucks?
**Bull:** 10%, 16%, 28x → **~14.3% a year** [C]; 2030 ~$808 [helper].
**Bear:** 3%, 13%, 18x → **~0.9% a year** [C]; 2030 ~$273 [helper] — steel/copper tariffs and
debt from the acquisition.
**Base:** 7% / 15% / 24x → **9.0% a year** [C].
**Break:** utility organic growth below 3% for two quarters, or leverage not falling by 2027.
**Sources:** [Q2 2026 results](https://hubbell.gcs-web.com/news-releases/news-release-details/hubbell-reports-second-quarter-2026-results) · [Q2 10-Q](https://www.sec.gov/Archives/edgar/data/0000048898/000162828026050405/hubb-20260630.htm)

#### PWR — Quanta Services · best company, priced for it
**Data:** $645.21 on 9/22/2026 [G]; ~150M shares [G]; ~$97B [C]; net debt ~$6.5B, 1.7x
debt/EBITDA [V/G]. Revenue $28.48B FY25 [V], $32.9B trailing [C]; 2026 guide $39.3-39.7B [V].
Backlog $44B → $53B in six months [V]. Adjusted EBITDA margin ~11% [G]. FCF $1.7B FY25 [V];
2026 guide $2.0-2.5B [V]. 38.6x 2026 EPS vs 5-year average ~25-30x [C/G]; EV/FCF ~46x [C];
up 461% in five years [G]; fell 16-18% in one day on DeepSeek (Jan 2025) [G].

**Thesis:** The largest and best-run grid contractor, with its own lineman training — the
widest moat in the labor bottleneck. The price already assumes it; the next AI scare is the
entry. Ground truth: Quanta crews and new training yards in your region.
**Bull:** 16%, 7%, 32x → **~17.5% a year** [C]; 2030 ~$1,070 [helper].
**Bear:** 5%, 5%, 20x → **about -1.5% a year** [C]; 2030 ~$287 [helper].
**Base:** 11% / 6% / 28x → **9.3% a year** [C].
**Break:** backlog falls quarter on quarter, or FCF below 50% of net income.
**Sources:** [Q2 2026 results](https://investors.quantaservices.com/news-events/press-releases/detail/402/quanta-services-reports-second-quarter-2026-results) · [FY2025 results](https://investors.quantaservices.com/news-events/press-releases/detail/390/quanta-services-reports-fourth-quarter-and-full-year-2025-results)

Near-misses: **GE Vernova** (turbines and transformers, 50x+ P/E [G]); **Vertiv** (most
data-center-concentrated and crowded, fell 25%+ on DeepSeek [G], [source](https://finance.yahoo.com/news/vertiv-holdings-co-vrt-stock-015637247.html)).

### Category 4: Outside AI

#### BRK.B — Berkshire Hathaway · SHORT LIST #4, the hedge
**Data:** $505.48 on 9/27/2026 [V]; ~2.16B B-equivalent shares [G]; ~$1.09T [C]. Cash and
T-bills $365.5B at 6/30 [V]; book value $349.32/share [V]; price/book 1.45 vs 5-year average
~1.5 [V/G]. Operating earnings Q2 $12.98B, +16% [V]; manufacturing/retail +24%, energy +27% [V].
Buybacks $4.5B in Q2 and $3.3B in July; $20B net stock purchases [V]. Rose ~4% in 2022 while
the Nasdaq fell 33% [G].

**Thesis:** Your portfolio's biggest risk is the fragility window — AI, SCHG, Meta, Adobe and
your margin collateral all falling together. Berkshire moved the other way in 2022, and an AI
bust would hand its $365B of cash cheap assets. It is insurance you get paid to hold.
**Bull:** book value compounds 10% a year to ~$545, at 1.6x book → 2030 ~$870 [helper].
**Bear:** book value +4% a year to ~$410, at 1.2x → 2030 ~$490 [helper].
Upside roughly 1.5x the downside [O] — the point is the cushion, not the upside. (Earnings-based;
FCF doesn't fit an insurer.)
**Break:** buybacks above 1.6x book, or a large acquisition at a premium price.
**Sources:** [Q2 2026 earnings](https://www.cnbc.com/2026/08/08/berkshire-hathaway-earnings-q2-2026.html) · [cash and buybacks](https://www.thestreet.com/investing/berkshire-hathaway-greg-abel-365-billion-cash-buybacks-dividend)

#### UNH — UnitedHealth · recovery, not asymmetric
**Data:** $376.59 on 9/25/2026 [V]; ~905M shares [G]; ~$341B [C]; net debt ~$49B (debt $73.3B
less $24.4B cash) [V/C]. Revenue $447.6B FY25 [V]. Medical care ratio 86.7% vs 89.4% a year
earlier [V]; medical costs $75.4B vs $78.6B [V]. 2026 guide adjusted EPS $19.50-20.00, operating
cash flow ~$24B [V]; ~19x vs 5-year average ~21x [C/G]. 2027 Medicare Advantage rate +3% [V]; a
special master rejected the DOJ's $2B overpayment claim (April 2026) [V]; criminal probe open.

**Thesis:** Health spending doesn't depend on AI capex, and the margin repair is only half in
the price.
**Bull:** EPS $30 at 18x → 2030 ~$540 [helper]. **Bear:** EPS $20 at 12x after a Medicare
Advantage clawback → 2030 ~$240 [helper]. Upside ~1.4x downside [C/O].
**Break:** medical care ratio back above 89%, or DOJ criminal charges.
**Sources:** [2025 results and 2026 outlook](https://www.morningstar.com/news/business-wire/20260126830491/unitedhealth-group-reports-2025-results-and-issues-2026-outlook) · [special master ruling](https://kffhealthnews.org/courts/unitedhealth-special-master-ruling-medicare-advantage-overpayments/) · [2026 recap](https://www.tikr.com/blog/unitedhealth-stock-is-up-14-in-2026-time-to-sell-or-load-up)

#### PEP — PepsiCo · cheap on earnings, not on cash
**Data:** $130.78 on 9/24/2026 [V]; 52-week low $127.98, down 24% from ~$171 [V]; 1.37B shares
[C]; ~$179B; debt $49.2B, net debt ~$40B [V/G]. Revenue $93.9B FY25 [V]. Core operating margin
16.8% vs 17.2% [V]; Q2 core operating profit -8%, volume flat despite price cuts [V]. FY25 FCF
$7.67B [V]; GAAP EPS $6.00 [V]. 2026 guide held: organic +2-4%, core EPS +4-6% [V]. ~15.6x core
earnings vs 5-year average P/E ~26 [C/V]; staples at an all-time low vs the S&P 500 [V].
EV/FCF ~28x [C].

**Thesis:** The market prices a permanent decline for brands still growing organically; if AI
money rotates out, staples are where it goes. The honest caveat: it's cheap on earnings only if
heavy capex returns to normal.
**Bull (FCF):** 4.5%, 11%, 22x → **~9.9% a year** [C]; on earnings, 2030 ~$230 (EPS $10.50 ×
22) [helper].
**Bear (FCF):** 1%, 8%, 16x → **about -0.3% a year** [C]; on earnings, 2030 ~$105 (EPS $7.50 ×
14) [helper] — weight-loss drugs and soda/dye policy keep volumes falling.
**Base (FCF):** 3% / 10% / 19x → **5.9% a year** [C].
**Break:** Oct 8 results cut 2026 guidance, or volume still negative in 2027.
**Sources:** [near 52-week low](https://www.investing.com/news/stock-market-news/pepsico-stock-near-52week-low-ahead-of-october-earnings-test-is-it-a-buy-93CH-4914833) · [FY2025 results](https://www.sec.gov/Archives/edgar/data/77476/000007747626000009/q420258-kxexhibit991.htm) · [staples relative low](https://www.thechartreport.com/TheMorningPrint/09-25-26)

Near-misses: **Robinhood / Interactive Brokers** — fit the wealth-transfer theme but fell ~75%
in 2022 [G], so they crash with AI; **General Mills** — ~9x P/E [V] but 22 fresh 52-week lows
in a year points to real volume loss.

---

## Part 3 — Why the short list is what it is [O]
1. **BKNG** — the only big name where AI savings are measured in the numbers AND the price is
   below its own history. Base case 17.6%.
2. **MYRG** — base case near your bar (11.3%), a possible forced selloff, and the one stock where
   your job gives you information before the market.
3. **ALNT** — the right bottleneck for the robotics theme, but already re-rated; watchlist.
4. **BRK.B** — not for return; it fixes the one risk every other holding shares.

What would change my mind: BKNG's commission rate falling; MYRG's selloff turning out to be
company-specific; ALNT's bookings reversing; Berkshire overpaying for a big deal.
