def TestLucas(n,L): #L es una lista con los divisores de n-1
    a=2
    i=0
    while a<n:     
        bool=True
        if exprapID(2, n-1,n)!=1:
            return False
        else:
            while i<len(L) and bool=True:
                if exprapID(2,int((n-1)/L[i]),n)==1:
                    bool=False
                i+=1
        if bool==True:
            return True
    return False

