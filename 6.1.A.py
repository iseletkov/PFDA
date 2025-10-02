# from math import log, pow, cos, sin,pi, e
import math

x = float(input())

ret = math.log(math.pow(x, 3 / 16), 32) + math.pow(x, math.cos(math.pi * x / 2 / math.e)) - (math.sin(x / math.pi)**2)
print(ret)