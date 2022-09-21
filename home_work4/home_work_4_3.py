#Definition of the intersection of circles

from math import sqrt

def circles_intersect(x1, y1, r1, x2, y2, r2):
    p = (x1-x2)**2 + (y1-y2)**2
    cen_dist = sqrt(p)
    if cen_dist > (r1 + r2) or p >= (r2+r1)**2:
        return False 
    elif cen_dist == 0:
        return False 
    else:
        return True
print(circles_intersect(4, 3, 2, 7, 5, 3))
