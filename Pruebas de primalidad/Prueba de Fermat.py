from random import randint

def testFermat(n,k):
    for j in range(0,k):
        a=randint(2,n-1)
        if exprapID(a,n-1,n)!=1:
            return False
    return True
