# Week-1 plan v3: caps $198k (US, dollar-designated), $190k TSMC (TWD/FX buffer).
ref = {"VLO":436.00,"XOM":172.15,"RTX":186.66,"LMT":512.80,"GOOGL":352.72,"NVDA":226.32}
stop = {"VLO":.08,"XOM":.06,"RTX":.06,"LMT":.06,"GOOGL":.06,"NVDA":.08,"TSMC":.07}
tp = {"VLO":(.10,.18),"XOM":(.08,.14),"RTX":(.08,.14),"LMT":(.08,.14),"GOOGL":(.08,None),"NVDA":(.10,.18),"TSMC":(.08,.15)}
for k,p in ref.items():
    s=p*(1-stop[k]); t1=p*(1+tp[k][0]); t2=p*(1+tp[k][1]) if tp[k][1] else 400.0
    print(f"{k:5s} {p:8.2f} stop {s:8.2f} (-{stop[k]*100:.0f}%)  tp1 {t1:8.2f} (+{tp[k][0]*100:.0f}%)  tp2 {t2:8.2f} ({100*(t2/p-1):+.1f}%)")
E=("VLO","XOM","RTX","LMT")
br = {
 "A": {"VLO":100,"XOM":114,"RTX":100,"LMT":100,"GOOGL":198,"NVDA":198,"TSMC":190},
 "M": {"VLO":150,"XOM":150,"RTX":150,"LMT":150,"GOOGL":198,"NVDA":100,"TSMC":100},
 "B": {"VLO":198,"XOM":198,"RTX":198,"LMT":198,"GOOGL":198},
}
for b,pos in br.items():
    inv=sum(pos.values()); risk=sum(v*stop[k] for k,v in pos.items())
    ed=sum(pos.get(k,0) for k in E)
    print(f"{b}: invested {inv}k  E/D {ed/10:.1f}%  AI {(inv-ed)/10:.1f}%  all-stops loss {risk:.2f}k ({risk/10:.1f}%)")
# Thursday/Friday orders per branch = final - Wed holdings
wed = {"VLO":100,"XOM":100,"RTX":100,"LMT":100,"GOOGL":100}
for b,pos in br.items():
    orders = {k: pos.get(k,0)-wed.get(k,0) for k in set(pos)|set(wed)}
    print(b, {k:v for k,v in sorted(orders.items()) if v})
