import sympy

V = sympy.Function('V')
C, R, t = sympy.symbols('C R t')

#C * V(t).diff(t) + V/R = x
x = C * V(t).diff(t) + V(t)/R

print(sympy.dsolve(x, V(t)))
