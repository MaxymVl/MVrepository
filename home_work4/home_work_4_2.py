#function for solving quadratic equations
from math import sqrt

def solve_quadratic_equation(a,b,c):
    Discr = b**2 - 4*a*c             #  discriminant formula

    if Discr >= 0:
        x1 = (-b + sqrt(Discr)) / (2*a)        #  formula for determining the root of a quadratic equation
        x2 = (-b - sqrt(Discr)) / (2*a)        #  formula for determining the root of a quadratic equation
        text = "Дискриминант: %s \n x1 = %s \n x2 = %s \n" % (Discr, x1, x2)        
    else:
        text = "Дискриминант: %s \n У уравнения решений нет" % Discr 
    return text
print(solve_quadratic_equation(-3,1,2))
print(solve_quadratic_equation(-5,6,1))
print(solve_quadratic_equation(5,6,1))
