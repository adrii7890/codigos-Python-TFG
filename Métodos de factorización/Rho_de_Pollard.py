from math import gcd

def Pollardp (n,x0,M):
    a=x0
    b=x0
    i=1
    d=1
    while i<=M and d==1:
        a=(a**2-1)%n
        b=(b**2-1)%n
        b=(b**2-1)%n
        d=gcd(a-b,n)
        i+=1
    if d!=1 and d!=n:
        return [d,n/d]
    else:
        return 0    #devuelve 0 si el método falla
