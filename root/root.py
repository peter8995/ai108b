import cmath

def root(a,b,c):
    t = cmath.sqrt(b*b-4*a*c)
    return [(-b+2)/(2*a), (-b-t)/(2*a)]


print("root of 4x^2+1x+3=", root(4,1,3))
