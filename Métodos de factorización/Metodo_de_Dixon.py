import algoritmos_complementarios as alg
from random import randint
    
def  trialdiv(n):
    L=[]
    if n<0:
        n=-n
        L.append(-1)
    m=alg.NRfloor(n)
    for i in  range (2,m+1):
        while n%i==0  and n!=1:
            L.append(i)
            n=n/i
    if n==1:
        return L
    else:
        L.append(int(n))
        return L 
    
def basef (M): #genera la base de factores 
    B=[2]
    i=3
    while i<=M:
        if alg.MR(i,4)==True:   #utilizamos el test de Miller-Rabin para verificar que si i es primo (la probabilidad de falso positivo es muy pequeña)
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

#primera parte del método de Dixon, la "recolección de datos". 

def Dixon(n,N,M):  #número a factorizar, M es la cota para la base de factores y N es el número de valores aleatorios que se generarán
    z=0                         #Se piden como entrada el número a factorizar, el número de elementos aleatorios con los que trabajaremos y la cota para la base de factores.
    w=0
    # Base de factores 
    base = basef(M)
    print("B=",base) #sacamos por pantalla la base de factores
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
            print(z,"^2=",w,"(mod", n,")")   #sacamos por pantalla los que son B-lisos
            Z.append(z)
            W.append(w)
            B.append(exp(w,base))
        i+=1
    print("A=",B) #imprimimos la matriz de exponentes
#tendríamos almacenada en B la matriz con los exponentes
