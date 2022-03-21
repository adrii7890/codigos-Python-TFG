import math


def NRtecho(n):  #Calcula la función techo de la raiz cuadrada usando el método de Newton
    x = n
    y = math.ceil((x + 1) / 2)
    while y < x:
        x = y
        y = math.ceil((x + n / x) / 2)
    return x


def isPerfectSquare(num): #determina si num es un cuadrado perfecto
        return math.sqrt(num) % 1 == 0


def FermatFact1(n,M):
    x=NRtecho(n)
    j=1
    while j<=M and isPerfectSquare(x**2-n)==False:
        x+=1
        j+=1
    if isPerfectSquare(x**2-n)==True:
        y=math.sqrt(x**2-n)
        return [(x-y),(y+x)]
    else:
        return 0 #Devuelve 0 si el método falla
