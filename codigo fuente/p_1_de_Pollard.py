from math import gcd

def Pollardp1 (n,H):
    a=2
    M=1
    d=1
    while M<H and d==1:
        a=(a**M)%n
        d=gcd(a-1,n)
        M+=1
    if d!=1 and d!=n:
        return [d, n//d]
    else:
        return 0    #devuelve 0 si no encontramos un factor al terminar las H iteraciones
