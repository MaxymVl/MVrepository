# function to determine and output what the number is

number = int(input("Введите любое число: "))

def sign_num(x):

    if x>0:   #Leap year is a multiple of 4, but not a multiple of 100, or a multiple of 400
        return ('Число положительное')
    elif x<0:
        return('Число отрицательное')
    else:
        return('Число равно 0')

print(sign_num(number)) 