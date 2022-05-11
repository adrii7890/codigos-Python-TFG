from math import gcd

def PollardpB (n,x0,M): #número a factorizar, valor inicial (en este caso 2 sería un buen valor) y número máximo de iteraciones
    a=x0
    b=x0
    i=1
    d=1
    k=2
    while i<=M and d==1:
        if i>k:
            k=2*k
            b=a
        a=(a**2-1)%n
        d=gcd(a-b,n)
        i+=1
       
    if d!=1 and d!=n:
        return [d,n//d]
    else:
        return 0    #devuelve 0 si no encuentra ningún factor
