# Thesis register

Every thesis gets one entry, and none counts as tested until all six questions are answered
with data: what changes · who pays / who gets paid · second-order bottleneck · timeline ·
priced in? · how to test. Each entry also needs a **break condition** written BEFORE money
goes in. "Invest no matter what as long as the thesis isn't broken" only works if "broken" is
defined in advance (the Adobe disprove list is the model).

Status: `raw` (stated, not tested) · `testing` · `holds` · `broken` · `parked`.

## PINNED

- **Robotics** — "robotics is inevitable", pinned 2026-09-27 for deep research. Questions to
  start with: who makes the parts every robot needs (actuators, reducers, sensors, motors),
  who is deploying at scale today, and which listed names sit in the $500M-$5B titan range.

## Theses

### T1 — AI makes most industry more productive over 20-40 years; the capex cycle is a bump · `raw`
- Source: user, 2026-09-27.
- Sharpest version (from the same notes): once intelligence is cheap, the gains go to whoever
  owns **distribution, manufacturing, logistics and moats that don't depend on intelligence**.
- Tension to resolve [O]: "productivity rises" does not by itself mean "margins rise". Where
  competitors all get the same tool, the saving often passes to customers as lower prices.
  The distribution version predicts WHO keeps the gain; the "most companies" version does not.
- Test idea: count S&P 500 earnings calls citing measurable cost reductions from internal AI
  (Booking.com's customer-service costs is the model signal), quarter by quarter. Rising
  breadth supports T1; staying at ~20 companies does not.

### T2 — Amazon: robotics and automation expand retail margins · `raw`
- Source: user, 2026-09-27. Holds conviction.
- Tension with our own valuation [C, Sept 2026]: ~8%/yr mid case at $248, 2/8 pillars,
  trailing FCF negative (capex). The thesis is a MARGIN thesis, so it must show up in margins.
- Test: North America segment operating margin, quarter by quarter; units shipped per
  employee (or headcount vs. volume); robot count disclosures. Break condition: not yet written.

### T3 — Robinhood captures the generational wealth transfer · `raw`
- Source: user, 2026-09-27. Separate from AI.
- Test: net deposits, funded customers, assets under custody and its growth rate, retirement
  and advisory assets, age mix of customers. Break condition: not yet written.

### T4 — US government will not let China lead in AI · `raw`
- Source: user, 2026-09-27. Supports T1.
- Test: federal AI/chip/power spending and policy (export controls, permitting, grid funding);
  who receives it.

### T5 — AI fear cycles with forced liquidation are buying chances, not thesis breaks · `raw`
- Source: the interview notes, 2026-09-27. Example given: Bloom Energy.
- Key distinction: selling from fundamental deterioration vs. selling from forced
  liquidation. Test: after a sector sell-off, did estimates/backlog fall, or only price?
- Existing evidence against the simple version [measured in kleague-model, `overreaction.py`]:
  2,547 single-stock drops of 15%+ versus the market over 20 days (489 names) showed **no
  reliable bounce** — +0.8% at 60 days, +1.1% at 120, all within noise. So a drop alone is not
  a buy signal; the forced-vs-fundamental distinction has to do the work.
- Claim to check: "another AI fear cycle within 30-90 days" (dated 2026-09-27, so it can be
  scored by 2026-12-26).

### T6 — Fragility window: capital is spent before returns arrive · `raw`
- Source: the interview notes. This is the bear case to T1 and should be tracked alongside it.
- Test: AI capex vs. AI revenue at the hyperscalers, and whether the gap narrows.

## Methods (not theses, but rules to test)

- **Asymmetric bets:** "priced at X%, true odds about 2X%". Worth taking only if the odds
  estimate is actually right, and sized so a long losing streak can't hurt. Can be tested with
  a sizing calculation when there is a real example.
- **Ground truth away from finance:** developers on Reddit/X/YouTube, job sites, crews on the
  grid. Public observation only.
- **The attention trade:** narrative spread moves prices short term. The kleague-model repo
  already tested whether commentary attention LEADS price (`stocks_model/attention.py`); its
  verdict is **cannot-answer** — not enough data yet, which is different from "no".
- **Price still matters, even with conviction:** the SpaceX note says it — stop adding when
  the edge is no longer something others don't see.
