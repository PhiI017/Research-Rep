import csv, bisect, statistics as st
import os
SRC=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','data','spx_daily.csv')
rows=[(r['date'],float(r['close'])) for r in csv.DictReader(open(SRC))]
rows.sort(); d=[r[0] for r in rows]; p=[r[1] for r in rows]
LEVELS=[10,15,20,25]
# find trigger dates: first close at or below each level within each episode (ATH -> next ATH)
trig={L:[] for L in LEVELS}; ath=p[0]; armed={L:True for L in LEVELS}
for i,x in enumerate(p):
    if x>ath:
        ath=x; armed={L:True for L in LEVELS}
    dd=(1-x/ath)*100
    for L in LEVELS:
        if armed[L] and dd>=L: trig[L].append(i); armed[L]=False
def fwd(i,yrs):
    j=i+round(252*yrs)
    return None if j>=len(p) else (p[j]/p[i])**(1/yrs)-1
def worse(i):  # further fall from trigger to the episode bottom (before recovering to trigger's ATH)
    peak=max(p[:i+1]); lo=p[i]
    for x in p[i:]:
        if x>=peak: break
        lo=min(lo,x)
    return lo/p[i]-1
print("S&P 500 price only (no dividends, ~2%/yr), 1960-01 to", d[-1])
for L in LEVELS:
    ts=trig[L]
    print(f"\n-{L}%: {len(ts)} episodes. dates: "+", ".join(d[i][:7] for i in ts))
    for y in (1,3,5):
        r=[fwd(i,y) for i in ts]; r=[v for v in r if v is not None]
        if r:
            print(f"  {y}y fwd annualised: n={len(r)} median {st.median(r):.1%}  worst {min(r):.1%}  "
                  f"beat 5%: {sum(v>0.05 for v in r)}/{len(r)}  beat 8%: {sum(v>0.08 for v in r)}/{len(r)}")
    w=[worse(i) for i in ts]
    print(f"  further fall after trigger: median {st.median(w):.1%}, worst {min(w):.1%}; fell another 20%+: {sum(v<=-0.20 for v in w)}/{len(w)}")
# baseline: all days
for y in (1,3,5):
    r=[fwd(i,y) for i in range(0,len(p),5)]; r=[v for v in r if v is not None]
    print(f"\nbaseline any-day {y}y: median {st.median(r):.1%}, beat 5%: {sum(v>0.05 for v in r)/len(r):.0%}, beat 8%: {sum(v>0.08 for v in r)/len(r):.0%}")
x=p[-1]; print("\nlatest close",d[-1],x," ATH",max(p)," drawdown",f"{x/max(p)-1:.1%}")
