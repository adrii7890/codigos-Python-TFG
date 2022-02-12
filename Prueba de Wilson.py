import math

def pruebaWilson(n):
    x=math.factorial(n-1)+1
    if x%n==0:
        return True
    else:
        return False
