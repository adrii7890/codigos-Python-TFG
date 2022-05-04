from math import floor

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

def NRsuelo(n): 
    x = n
    y = floor((x + 1) / 2)
    while y < x:
        x = y
        y = floor((x + n / x) / 2)
    return x
  
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

def suclucas(n,r, P,Q): #calccula U_r(n) y V_(r) para P y Q dados

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
