import algortimos_complementarios as alg

def LucasStest(n):
    D=5
    i=1
    while alg.jacobi(D,n)!=-1:
        D=-D+2*(-1)**i
        i+=1
    P=1
    Q=(1-D)//4
    s,d=0,n+1
    while d%2==0:
        s+=1
        d//=2
    L=alg.suclucas(n,d,P,Q)
    if L[0]==0 or L[1]==0:
        return True
    else:
        r=2
        V=(L[1]**2-2*(Q**d))%n
        if V==0:
            return True
        chi=True
        while r<s and chi==True:
            V=(V**2)%n-(2*(alg.binladders(Q,2**(r-1)*d,n)))%n
            if V==0:
                return True
            r+=1
        return False
            
