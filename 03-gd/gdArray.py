import gd2 as gd

def f(p):
    [x, y, z] = p
    return x*x + 3*y*y + z*z - 4*x - 3*y - 5*z + 8

p = [0.0, 0.0, 0.0]
gd.gradientDescendent(f, p)
