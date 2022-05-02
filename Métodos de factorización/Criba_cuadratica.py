import algoritmos_complementarios as alg

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

def isprime(n):
    prime=True
    i=2
    while i<=alg.NRsuelo(n) and prime==True:
        if n%i==0:
            prime=False
        i+=1
    return prime

def basef (n,M):       #M es la cota para los elementos de la base
    B=[-1,2]
    i=3
    while i<=M:
        if MR(i,6)==True and alg.jacobi(n,i)==1:    #Usamos la función jacobi(n) del módulo algoritmos_complementarios y el algoritmo de Miller-Rabin
            B.append(i)
        i+=1
    return B

def QS(n,M1,M2): #solo la primera parte del algoritmo, la "recolección de datos"
    z=0
    w=0
    Base=basef(n,M2) #generamos la base de factores
    S=[alg.NRsuelo(n)]
    #Generación de la lista S
    for i in range(1,M1):
        S.append(alg.NRsuelo(n)+i)
        S.append(alg.NRsuelo(n)-i)
    B = []
    Z = []
    W=[]
    i=0
    #Búsqueda de números lisos para nuestra base de factores
    while i<len(S) and len(Base)>=len(Z):
        z=S[i]
        w=z**2-n 
        if Bsmooth(w,Base):
            Z.append(z)
            W.append(w) 
            B.append(exp(w,Base)) #aqui tendríamos la matriz de exponentes
        i+=1

