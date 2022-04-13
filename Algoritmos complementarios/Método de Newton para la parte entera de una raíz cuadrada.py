from math import floor

def NRsuelo(n): 
    x = n
    y = floor((x + 1) / 2)
    while y < x:
        x = y
        y = floor((x + n / x) / 2)
    return x
