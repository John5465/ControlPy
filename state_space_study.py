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

# ===============
# state space
# 令 z1 = x, z2 = dx/dt
#    z1_dot = z2, z2_dot = d2x/dt2
A = sympy.Matrix([[0,       1],
                  [-k/m, -b/m]])
B = sympy.Matrix([0, 1/m])
C = sympy.Matrix([1, 0])
D = sympy.Matrix([0])
I = sympy.eye(2,2)

f_tran = C.T*((s*I-A).inv())*B

f_tran