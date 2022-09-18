# determination of high year or not

year = int(input("Введите любой год: "))

def leap(year):

    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):   #Leap year is a multiple of 4, but not a multiple of 100, or a multiple of 400
        return ('YES')
    else:
        return('NO')

print(leap(year))    