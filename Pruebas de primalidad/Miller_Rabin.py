from random import randint
import algoritmos_complementarios as alg

def MR(n,k):
    j, d= 0, n-1
    while d%2==0:       #Descomponemos n-1 de la forma deseada
        j+=1
        d//=2
    for _ in range(1,k):
        a=randint(2,n-1)
        e=alg.binladders(a,d,n)
        if e!=1 and e!=n-1:              #Comprobamos que no es -1, si lo es pasamos a otra base
            i=1
            bool=True
            while i<j and bool==True:
                e=e**2%n
                if e==n-1:
                    bool=False         #Si hay un -1 entonces pasa el test para esa base, seguimos con la siguiente
                i+=1
            if bool==True:              #Si no hay ningún -1 entonces n es compuesto
                return False
            
    return True
