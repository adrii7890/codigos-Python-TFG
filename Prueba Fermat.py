import random

def pruebaFermat(n,k):
    for j in range(0,k):
        a=random.randint(2,n-1) #genera un entero aleatorio entre 2 y n-1, ambos incluidos
        print(a)
        if exprapID(a,n-1,n)!=1: #vemos si pasa el test usando el algoritmo de la exponenciación rápida, cuyo código se puede ver también en el repositorio
            return False
    return True
