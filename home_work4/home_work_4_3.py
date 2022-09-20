#Definition of the intersection of circles

from math import sqrt

def calc_interception(x1, y1, r1, x2, y2, r2):
    
    cen_dist = sqrt((x1-x2)**2 + (y1-y2)**2)
    if cen_dist > (r1 + r2) or ((x1-x2)**2 + (y1-y2)**2) >= (r2+r1)**2:
        return False
    elif cen_dist == 0:
        return False
    else:
        return True
print(calc_interception(4, 3, 2, 7, 5, 3))
