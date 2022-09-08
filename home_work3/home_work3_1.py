from cmath import cos, pi
import math

deg = math.pi/180
def degrees2radians(x):
    deg = x*math.pi/180
    y = math.cos(x*pi/180)
    return deg, y
print(degrees2radians(60))
print(degrees2radians(45))
print(degrees2radians(40))
