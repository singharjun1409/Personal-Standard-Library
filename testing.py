import math
def modfp(x):
    integerPart = int(x)
    fractionPart = x - integerPart
    
    return(integerPart , fractionPart)

print(modfp(1.05))
