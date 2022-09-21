# determining if a number is even

def is_even(number):
    
    if (number < 2):
        return (is_even(number % 2 == 0))
n = int(input("Введите любое число:"))
if (is_even(n) == True):
      print("Число является четным!")
else:
      print("Число является нечетным!")
