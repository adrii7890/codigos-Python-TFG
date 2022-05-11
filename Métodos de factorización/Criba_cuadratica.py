import algoritmos_complementarios as alg

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
    
def Bsmooth(n,B):
    smooth=True
    L=trialdiv(n)
    i=0
    while smooth==True and i<len(L):
        if L[i] not in B:
            smooth=False
        i+=1
    return smooth

def exp(n,B):
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

def basef (n,M):       #M es la cota para los elementos de la base
    B=[-1,2]
    i=3
    while i<=M:
        if alg.MR(i,6)==True and alg.jacobi(n,i)==1:    #Usamos la función jacobi(n) del módulo algoritmos_complementarios y el algoritmo de Miller-Rabin
            B.append(i)
        i+=1
    return B

#solo la primera parte del algoritmo, la "recolección de datos"

def QS(n,M1,M2): #número a factorizar, M2 es la cota para la base de factores
    z=0
    w=0
    Base=basef(n,M2) #generamos la base de factores
    print("B=",Base) #sacamos por pantalla la base de factores
    S=[alg.NRfloor(n)]
    #Generación de la lista S
    for i in range(1,M1):
        S.append(alg.NRfloor(n)+i)
        S.append(alg.NRfloor(n)-i)
    B = []
    Z = []
    W= []
    i=0
    #Búsqueda de números lisos para nuestra base de factores
    while i<len(S) and len(Base)>=len(Z):
        z=S[i]
        w=z**2-n
        if Bsmooth(w,Base):
            print(z,"^2=",w,"(mod", n,")") #sacamos por pantalla los que cumplen la condición de B-lisos
            Z.append(z)
            W.append(w) 
            B.append(exp(w,Base)) #aqui tendríamos la matriz de exponentes
        i+=1
    print("A=",B) #sacamos la matriz de exponentes módulo 2
