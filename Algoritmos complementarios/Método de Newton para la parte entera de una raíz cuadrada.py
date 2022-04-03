from math import floor

def NRsuelo(n): 
    x = n
    y = math.floor((x + 1) / 2)
    while y < x:
        x = y
        y = math.floor((x + n / x) / 2)
    return x
