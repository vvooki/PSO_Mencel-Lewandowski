import math
def ackley(x,y):
    ackley = 20 * math.exp(-0.2 * math.sqrt(0.5 * (x * x + y * y))) + math.exp(0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))) - 20
    return ackley