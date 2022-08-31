#!/usr/bin/python3
line = str(input("Введите строку: "))
line = line.replace("_", ' ').title()
line = line.replace(' ', '' )
print(line)