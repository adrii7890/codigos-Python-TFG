
def exprapID(base, num, mod): #algoritmo de la exponenciación rápida (variante izquierda a derecha)
    acu=1
    binary=format(num,"b")
    i=0
    while i<len(binary):
        acu=(acu**2)%mod
        if binary[i]=="1":
            acu=(acu*base)%mod
        i+=1
    return acu

def TestLucas(n,L):
    a=2
    i=0
    while a<n:     
        bool=True
        if exprapID(2, n-1,n)!=1:
            return False
        else:
            while i<len(L):
                if exprapID(2,int((n-1)/L[i]),n)==1:
                    bool=False
                i+=1
        if bool==True:
            return True
    return False

