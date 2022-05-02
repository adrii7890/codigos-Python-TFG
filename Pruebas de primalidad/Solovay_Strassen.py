from random import randint
import algoritmos_complementarios as alg

def PruebSS(n,k):
    for j in range(1,k):
        a=randint(2,n-1)
        x=alg.jacobi(a,n)
        print(a,x)
        if x==-1:
            x=n-1
        if (x!=alg.binladders(a,(n-1)//2,n)):
            return False
    return True
