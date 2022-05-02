import algortimos_complementarios as alg

def LucasStest(n):
    D=5
    i=1
    while alg.jacobi(D,n)==1:
        D=-D+2*(-1)**i
        i+=1
    print("D=",D)
    P=1
    Q=(1-D)/4
    s,d=0,n+1
    while d%2==0:
        s+=1
        d//=2
    print("n=2^",s,"*",d)
    U_0,U_1=0,1
    V_0,V_1=2,P
    t=1
    for _ in range(2,d+1):
        U=(P*U_1-Q*U_0)%n
        U_0=U_1
        U_1=U
        V=(P*V_1-Q*V_0)%n
        V_0=V_1
        V_1=V
    print(int(U),int(V))
    if U==0 or V==0:
        return True
    else:
        r=1
        chi=True
        while r<s and chi==True:
            V=(V**2)%n-(2*(alg.binladders(Q,2**(r-1)*d,n)))%n
            print(int(V))
            if V==0:
                chi=False
            r+=1
        if chi==True:
            return False
        else:
            return True
