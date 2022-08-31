#!/usr/bin/python3
l = int(input("Введите трехзначное число: "))
a = l//100
b = (l//10)%10
c = l%10
print ("Сумма цифр числа:", a + b + c)
