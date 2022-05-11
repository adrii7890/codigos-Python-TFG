import algoritmos_complementarios as alg

def TestLucas(n,L): #L es una lista con los divisores de n-1 y n es el número que se pretende testear
    a=2
    while a<n:     
        i=0
        bool=True
        if alg.binladders(2, n-1,n)!=1:     #usamos el algoritmo de los cuadrados iterados, cuyo código se puede ver también en este repositorio
            return False
        else:
            while i<len(L) and bool==True:
                if alg.binladders(2,(n-1)//L[i],n)==1: 
                    bool=False
                i+=1
        if bool==True:      #si todos son dsitintos de 1, entonces n es primo
            return True
        a+=1
    return False

