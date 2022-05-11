from math import gcd
import Algoritmos_complementarios as alg

def Pollardp1M (n,H):
    a=2
    M=2
    d=1
    lcm=1
    while M<H and d==1:
        g=gcd(lcm,M) 
        if g!=M:
            lcm*=(M//g)
            a=alg.binladders(a,M//g,n)
            d=gcd(int(a)-1,n)
        M+=1
    if d!=1 and d!=n:
        return [d,int(n/d)]
    else:
        return 0
