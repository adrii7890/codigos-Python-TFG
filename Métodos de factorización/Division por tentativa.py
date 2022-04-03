def trialdiv(n):
    L=[]
    m=NRsuelo(n)
    for i in range (2,m):
        while n%i==0 and n!=1:
            L.append(i)
            n=n/i
            m=NRsuelo(n)
    if n==1:
        return L
    else: 
        L.append(n)
        return L
