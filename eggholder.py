import math
def eggholder(x,y):
    eggholder = (y + 47) * math.sin(math.sqrt(abs(x/2+(y+47)))) + x * math.sin(math.sqrt(abs(x - (y + 47))))
    return eggholder

