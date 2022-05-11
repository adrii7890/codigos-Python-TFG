
import algoritmos_complementarios as alg
import Prueba_fuerte_de_Lucas as LucasS

def baillie_PSW(n):
    if alg.trialdiv(n)==False:
        return False
    elif alg.MR2(n)==False:
            return False
    elif LucasS.LucasStest(n)==False:
        return False
    else:
        return True
