import algoritmos_complementarios as alg

def trialdiv(n):
    L=[]
    m=alg.NRfloor(n)
    for i in range (2,m+1):
        while n%i==0 and n!=1:
            L.append(i)
            n=n//i
            m=alg.NRfloor(n)
    if n==1:
        return L
    else: 
        L.append(n)
        return L
