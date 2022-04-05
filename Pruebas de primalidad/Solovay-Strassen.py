def PruebSS(n,k):
    for j in range(1,k):
        a=random.randint(2,n-1)
        x=jacobi(a,n)
        print(a,x)
        if x==-1:
            x=n-1
        if (x!=binladders(a,(n-1)//2,n)):
            return False
    return True
