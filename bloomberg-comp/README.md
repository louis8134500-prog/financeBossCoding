# Bloomberg Global Trading Challenge 2026

Our team's files for the challenge: $1M notional, long only, single stocks in the WLS index, Oct 12 to Nov 13, 2026.

## What's here

| File | What it is | Status |
| --- | --- | --- |
| [plans/2026-10-13_week1-trading-plan.md](plans/2026-10-13_week1-trading-plan.md) | Week 1 orders, stops and targets (Oct 13–16), with branches A / M / B set by TSMC's results | Current |
| [daily-desk/2026-10-15_desk-review.pdf](daily-desk/2026-10-15_desk-review.pdf) | Desk review for Thu Oct 15: the market, TSMC's results, the branch M call, positions and P&L, stop-loss and take-profit levels, and the day's orders | Current |
| [tools/week1_levels_and_sizing.py](tools/week1_levels_and_sizing.py) | Computes the plan's stop and target prices, branch sizes and loss if every stop hits | Current |
| [archive/2026-10-13_initial-strategy-memo.md](archive/2026-10-13_initial-strategy-memo.md) | First-draft strategy memo (memory and AI-hardware book) | Superseded |
| [archive/2026-10-13_early-execution-menu.py](archive/2026-10-13_early-execution-menu.py) | Sizing math for the first execution menu (TSMC, Nvidia, Alphabet, Lam, SK hynix, Micron) | Superseded |

Run the sizing script with `python3 tools/week1_levels_and_sizing.py`; it needs only Python 3.

## Rules that bind us

Verify each on the terminal; the 2026 terms page could not be opened, so these come from the 2026 FAQ and the 2025 terms.

- $1M notional; long only; single stocks in the WLS index; no ETFs or leverage; no position above 20% ($200k).
- Initial positions by Fri Oct 16, 11:59 PM ET.
- Scored on time-weighted return relative to WLS, Oct 12 9:00 AM to Nov 13 5:00 PM ET. Cash earns 0%.

## How the folder is kept

- Name files `YYYY-MM-DD_short-name.ext` by the date written.
- `plans/` holds trading plans, `daily-desk/` daily desk reviews as PDFs, `tools/` scripts, `research/` notes and data, `archive/` anything replaced.
- When a plan is replaced, move it to `archive/` and add a "Superseded" line at the top that links to its replacement.
- The editable version of each plan is the team's Claude doc, "Bloomberg Trading Challenge Strategy". The files here are snapshots: the Week 1 plan is at doc revision 16, as of Oct 13, and the Oct 15 desk review is at revision 29.

## Not yet here

Earlier materials were not recovered: the rulebook, data pack, session notes, price analysis, earnings calendars, JMC reference materials and the trader brief. Add copies under `research/`.
