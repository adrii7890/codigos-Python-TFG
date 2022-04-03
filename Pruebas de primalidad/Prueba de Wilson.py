from math import factorial

def pruebaWilson(n):
    x=factorial(n-1)+1
    if x%n==0:
        return True
    else:
        return False
