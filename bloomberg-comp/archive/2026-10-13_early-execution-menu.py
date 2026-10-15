# Week-1 execution menu math. Reference prices from web sources (see doc), FX approximate.
KRW, TWD = 1450.0, 31.6  # per USD, approximate

rows = [
 # name, ccy, ref, tranches_usd, stop, tp1, tp2
 ("TSMC",     "TWD", 2540.0,   [99000, 99000], 2360,    2745,    2920),
 ("Nvidia",   "USD", 226.32,   [99000, 99000], 208,     249,     267),
 ("Alphabet", "USD", 352.72,   [99000, 99000], 331,     381,     400),
 ("Lam",      "USD", 309.56,   [150000],       282,     340,     371),
 ("SK hynix", "KRW", 1457000., [75000, 75000], 1280000, 1680000, 1900000),
 ("Micron",   "USD", 989.04,   [50000, 50000], 900,     1100,    1200),
]
fx = {"USD": 1.0, "KRW": KRW, "TWD": TWD}
tot = risk_tot = 0
for n, c, ref, tr, st, t1, t2 in rows:
    usd = sum(tr)
    sh = [int(t * fx[c] // ref) for t in tr]
    risk = usd * (ref - st) / ref
    tot += usd; risk_tot += risk
    print(f"{n:9s} ${usd:>8,.0f} shares/tranche {sh} total {sum(sh)}  "
          f"stop {100*(st/ref-1):+.1f}%  tp1 {100*(t1/ref-1):+.1f}%  tp2 {100*(t2/ref-1):+.1f}%  "
          f"risk@stop ${risk:,.0f}  gain@tp1 ${usd*(t1/ref-1):,.0f}")
print(f"TOTAL invested ${tot:,.0f}  cash ${1_000_000-tot:,.0f}  risk if all stops hit ${risk_tot:,.0f} ({100*risk_tot/1e6:.1f}%)")
print("half-size check: SK hynix tranche KRW", 75000*KRW, " TSMC tranche TWD", 99000*TWD)
