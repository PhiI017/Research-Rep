def pv(rev0, g, m, mult, r, netcash, years=10):
    v, rev = 0, rev0
    for t in range(1, years+1):
        rev *= 1+g
        v += rev*m/(1+r)**t
    return v + rev*m*mult/(1+r)**years + netcash
def irr(rev0,g,m,mult,netcash,cap):
    lo,hi=-0.5,1.0
    for _ in range(100):
        mid=(lo+hi)/2
        if pv(rev0,g,m,mult,mid,netcash)>cap: lo=mid
        else: hi=mid
    return mid
def run(name, rev0, netcash, shares, price, cases):
    cap=shares*price
    print(f"{name}: mcap {cap:.0f}  EV {cap-netcash:.0f}")
    for lab,(g,m,mult) in cases.items():
        print(f"  {lab:5s} g={g:.0%} fcf={m:.0%} x{mult}: return {irr(rev0,g,m,mult,netcash,cap):.1%}  "
              f"value@9% ${pv(rev0,g,m,mult,.09,netcash)/shares:.0f}  @12% ${pv(rev0,g,m,mult,.12,netcash)/shares:.0f}")
import sys
if __name__=="__main__":
    run("PLPC", 740.5, 33.4, 4.90, 421.20,
        {"low":(0.03,0.06,15),"mid":(0.07,0.09,16),"high":(0.11,0.12,20)})
