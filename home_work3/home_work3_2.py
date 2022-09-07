#!/usr/bin/python3
import math

def triangle_square_and_perimeter(a, b):
    a = float(input("Введите длину катета a: "))
    b = float(input("Введите длину катета b: "))
    c1 = math.sqrt(a**2 + b**2)
    c = round(c1,2)
    s = 1/2 * a * b
    per = a + b + c
    return s, per
print (triangle_square_and_perimeter('a','b'))
