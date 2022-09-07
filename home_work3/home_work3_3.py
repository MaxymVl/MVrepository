#!/usr/bin/python3
import math

def cone_square_and_volume(radius, height):
    r = float(input("Введите радиус конуса r: "))
    h = float(input("Введите высоту конуса h: "))
    v1 = (math.pi*r**2*h)/3
    v = round(v1,2)
    s1 = math.pi*r*(r + math.sqrt(r**2 + h**2))
    s = round(s1,2)
    return s, v
print (cone_square_and_volume('r','h'))

