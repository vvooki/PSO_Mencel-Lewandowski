import math
def rastrign(x,y):
    rastrign = -(10 * 2 + (x * x - 10 * math.cos(2 * math.pi * x)) + (y * y - 10 * math.cos(2 * math.pi * y)))
    return rastrign