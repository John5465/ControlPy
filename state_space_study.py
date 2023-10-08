import sympy
# from sympy import init_session
# init_session(quiet=True) 

t, s = sympy.symbols('t s')
x = sympy.Function('x')
m, b, k = sympy.symbols('m b k')

# 弹簧阻尼系统
f = m * x(t).diff(t).diff(t) + b*x(t).diff(t) + k*x(t)

f_lap = sympy.laplace_transform(f, t, s)

#f_lap = sympy.simplify(f_lap)

# 传递函数 X(s) / F(s)
Gs = 1 / (m * s**2 + b * s + k)

z1 = x(t)
z2 = z1.diff(t)

z1
z2