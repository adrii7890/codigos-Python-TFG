import algoritmos_complementarios as alg

def isPerfectSquare(num): #determina si num es un cuadrado perfecto
        return alg.NRsuelo(num)**2 == num


def FermatFact1(n,M):
    x=alg.NRsuelo(n)
    j=1
    while j<=M and isPerfectSquare(x**2-n)==False:
        x+=1
        j+=1
    if isPerfectSquare(x**2-n)==True:
        y=alg.NRsuelo(x**2-n)
        return [(x-y),(y+x)]
    else:
        return 0 #Devuelve 0 si el método falla
