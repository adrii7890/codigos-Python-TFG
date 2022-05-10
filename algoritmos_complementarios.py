from math import floor
from random import randint

def NRfloor(n): #Calculo de la función suelo de la raiz cuadrada mediante el método de Newton
    x = n
    y = math.floor((x + 1) / 2)
    while y < x:
        x = y
        y = math.floor((x + n / x) / 2)
    return x

def NRsuelo(n): 
    x = n
    y = floor((x + 1) / 2)
    while y < x:
        x = y
        y = floor((x + n / x) / 2)
    return x

def trialdiv(n): #modificado limite 1000 (para Baillie_PSW)
    L=[]
    m=NRsuelo(n)
    for i in range (2,min(NRsuelo(n), 1000)):
        if n%i==0:
            return False
    return True

def binladders(base, num, mod):
    acu=base
    binary=format(num,"b")
    i=1
    while i<len(binary):
        acu=(acu**2)%mod
        if binary[i]=="1":
            acu=(acu*base)%mod
        i+=1
    return acu
  
def jacobi(a,n):
    sol=0
    if a==0:
        if n==1:
            return 1
        else:
            return 0
    if a==2:
        r=n%8
        if r==7 or r==1:
            return 1
        if r==5 or r==3:
            return -1
    if a<0:
        if n%4==1:
            sol= jacobi(-a,n)
        else:
            sol=-jacobi(-a,n)
    elif a>=n:
        sol=jacobi(a%n,n)
    elif a%2==0:
        sol=jacobi(2,n)*jacobi(a//2,n)
    else:
        if a%4==3 and n%4==3:
            sol=-jacobi(n,a)
        else:
            sol=jacobi(n,a)
 
    return sol

def suclucas(n,r, P,Q):
    if r==1:
        return [1,1]
    else:
        v1 = format(n,"b")
        v2 = format(r,"b")
        l1 = len(v1)
        l2 = len(v2)
        U1 = 1
        U2 = P
        U1aux=U1
        k = 1
        for i in range( 1, l2):
            if v2[i] == '0':
                k = 2*k;
                U1 = (2*U1*U2 - P*U1**2)%n
                U2 = (U2**2 - Q*U1aux**2)%n
                U1aux=U1
            else:
                k = 2*k + 1;
                U1 = (U2**2 - Q*U1**2)%n
                U2 = (P*U2**2 - 2*Q*U1aux*U2)%n
                U1aux=U1
            if k==r:
                return [U1,(2*U2-P*U1)%n]
     
def MR(n,k):
    j, d= 0, n-1
    while d%2==0:
        j+=1
        d//=2
    for _ in range(0,k):
        a=randint(2,n-1)
        e=binladders(a,d,n)
        if e!=1 and e!=n-1:            
            i=1
            bool=True
            while i<j and bool==True:
                e=e**2%n
                if e==n-1:
                    bool=False       
                i+=1
            if bool==True:   
                return False
            
    return True
