#!/usr/bin/python3

a = input ("Введите любое трехзначное число: ")

def sum_of_digits(num):
    sum = 0
    l = ord(a[0])
    l1 = l - 48
    m = ord(a[1])
    m1 = m - 48
    c = ord(a[2])
    c1 = c - 48
    sum = l1 + m1 + c1
    return sum
print (sum_of_digits(sum))