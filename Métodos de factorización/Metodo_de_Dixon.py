import math
from random import randint
    
def basef (M): #genera la base de factores 
    B=[2]
    i=3
    while i<=M:
        if MR(i,6)==True:   #utilizamos el test de Miller-Rabin para verificar que si i es primo (la probabilidad de falso positivo es muy pequeña)
            B.append(i)
        i+=1
    return B

def Bsmooth(n,B): #función que devuelve si un número es B-liso
    smooth=True
    L=trialdiv(n)
    i=0
    while smooth==True and i<len(L):
        if L[i]>B:
            smooth=False
        i+=1
    return smooth


def exp(n,B): #función que devuelve el exponente módulo dos de un número con respecto a una cierta base de factores
    L=trialdiv(n)
    E = []
    i=0
    while len(L)>0 and i<len(B):
        a=L[0]
        if a==B[i]:
            j=0
            count=0
            while j<len(L):
                if L[j]==a:
                    count+=1
                    L.pop(j)
                    j=0
                else:
                    j+=1
            E.append(count%2)
            i+=1
        else:
            i+=1
            E.append(0)
    while len(E)<len(B):
        E.append(0)
    return E        


def Dixon(n,N,M): #primera parte del método de Dixon, la "recolección de datos". 
    z=0                         #Se piden como entrada el número a factorizar, el número de elementos aleatorios con los que trabajaremos y la cota para la base de factores.
    w=0
    # Base de factores 
    base = basef(M)
    L=[]
    #Generación de la lista aleatoria
    while len(L)<N:
        L.append(randint(1,n)) #aleatorios en el intervalo [1,n]

    B = []
    Z = []
    W=[]
    i=0
    #Búsqueda de números lisos para nuestra base de factores
    while i<N and len(Z)<=len(base):
        z=L[i]
        w=z**2%n 
        if Bsmooth(w,M)==True:
            Z.append(z)
            W.append(w)
            B.append(exp(w,base))
        i+=1
#tendríamos almacenada en B la matriz con los exponentes
