#function for solving quadratic equations
from math import sqrt

def solve_quadratic_equation(a,b,c):
    Discr = b**2 - 4*a*c             #  discriminant formula

    if Discr > 0:
        x1 = (-b + sqrt(Discr)) / (2*a)        #  formula for determining the root of a quadratic equation
        x2 = (-b - sqrt(Discr)) / (2*a)        #  formula for determining the root of a quadratic equation
    elif Discr == 0:  
        x1 = -b / 2*a 
        x2 = None 
    else:
        x1 = None
        x2 = None 
    return x1, x2
print(solve_quadratic_equation(-3,1,2))
print(solve_quadratic_equation(-5,6,1))
print(solve_quadratic_equation(5,6,1))
print(solve_quadratic_equation(1,2,1))
