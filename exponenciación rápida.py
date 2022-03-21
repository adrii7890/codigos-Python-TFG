
def binladders(base, num, mod): #algoritmo de la exponenciación rápida (variante izquierda a derecha)
    acu=base
    binary=format(num,"b")
    i=1
    while i<len(binary):
        acu=(acu**2)%mod
        if binary[i]=="1":
            acu=(acu*base)%mod
        i+=1
    return acu
