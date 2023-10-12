import sympy

t = sympy.symbols('t')
 
# robot pose & vel
x_r, y_r, theta_r = sympy.symbols('x_r y_r theta_r')
v_r, w_r = sympy.symbols('v_r w_r')

# desired pose & vel
x_d, y_d, theta_d = sympy.symbols('x_d y_d theta_d')
v_d, w_d = sympy.symbols('v_d w_d')

# err
#x_e, y_e, theta_e = sympy.symbols('x_e y_e theta_e')
v_e, w_e = sympy.symbols('v_e w_e')

# rotation matrix
#rot_mat_vel = sympy.Matrix([sympy.cos(t)])
rot_mat_vel = lambda theta: sympy.Matrix([[sympy.cos(theta), 0],
                                          [sympy.sin(theta), 0],
                                          [               0, 1]])

rot_mat_pos = lambda theta: sympy.Matrix([[sympy.cos(theta), -sympy.sin(theta), 0],
                                          [sympy.sin(theta),  sympy.cos(theta), 0],
                                          [               0,                 0, 1]])

# kinematic
x_r_dot, y_r_dot, theta_r_dot = rot_mat_vel(theta_r) * sympy.Matrix([[v_r], [w_r]])
x_d_dot, y_d_dot, theta_d_dot = rot_mat_vel(theta_d) * sympy.Matrix([[v_d], [w_d]])

err_vec = sympy.Matrix([[x_r - x_d], [y_r - y_d], [theta_r - theta_d]])

x_e, y_e, theta_e = rot_mat_pos(-theta_d) * err_vec

x_e, y_e, theta_e = sympy.symbols('x_e y_e theta_e')
x_e_dot = -v_d + v_r * sympy.cos(theta_e) + w_d * y_e
y_e_dot = v_r*sympy.sin(theta_e) - w_d * x_e
theta_e_dot = theta_r_dot - theta_d_dot