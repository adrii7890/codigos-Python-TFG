
def exprapID(base, num, mod): #algoritmo de la exponenciación rápida (variante izquierda a derecha)
    acu=1
    binary=format(num,"b")
    i=0
    while i<len(binary):
        acu=(acu**2)%mod
        if binary[i]=="1":
            acu=(acu*base)%mod
        i+=1
    return acu
