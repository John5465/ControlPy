import sympy

#from sympy import init_session
#init_session(quiet=True)

x, y, z = sympy.symbols('x y z')

Yn = sympy.symbols('y1:10')
Yv = sympy.Matrix(Yn)

f = sympy.Function('f')
f_mat = sympy.Matrix([f(y) for y in Yv])

#f(Yv).diff(Yv)
f_diff = sympy.Matrix([f_mat.diff(y) for y in Yv])