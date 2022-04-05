def jacobi1(a,n):
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
 
    if a>=n:
        sol=jacobi1(a%n,n)
    elif a%2==0:
        sol=jacobi1(2,n)*jacobi1(a//2,n)
    else:
        if a%4==3 and n%4==3:
            sol=-jacobi1(n,a)
        else:
            sol=jacobi1(n,a)
 
    return sol
