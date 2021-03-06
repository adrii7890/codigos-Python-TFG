from random import randint
import algoritmos_complementarios as alg

def pruebaFermat(n,k): #número al que se le pasa el test y número de bases aleatorias para las que queremos aplicar el test
    for j in range(0,k):
        a=randint(2,n-1) #genera un entero aleatorio entre 2 y n-1, ambos incluidos
        if alg.binladders(a,n-1,n)!=1: #vemos si pasa el test usando el algoritmo de cuadrados iterados, cuyo código se puede ver también en el repositorio
            return False
    return True
