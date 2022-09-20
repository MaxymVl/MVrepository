# function to determine and output what the number is

number = int(input("Введите любое число: "))

def sign_num(x):

    if x>0:  
        return +1
    elif x<0:
        return -1
    else:
        return 0

print(sign_num(number)) 
