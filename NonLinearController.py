import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from PhasePortrait2D import PhasePortrait2D

class NonLinearPlant(object):
    def __init__(self):
        pass
    
    def sys(self, x, u=0., t=0.):
        return x**2 - x**3 + u
    
    def sys_ode(self, t=0., x=0., u=0.):
        return x**2 - x**3 + u
    
    def sys_ode_u1(self, t, x):
        return x**2 - x**3 + (-x**2 + x**3 - x)
    
    def sys_ode_u2(self, t, x):
        return x**2 - x**3 + (-x**2 - x)
    
    def sys_ode_u3(self, t, x):
        return x**2 - x**3 + (-x**2)
    
if __name__ == "__main__":
    plant = NonLinearPlant()
    
    # phase portrait
    if True:        
        fig, ax = plt.subplots()
        ax.grid()
        
        x = np.arange(-10., 10., 0.5)
        x_prime = plant.sys(x)
        
        # solve ode
        x0 = 3.
        t_end = 10.
        
        xs = solve_ivp(plant.sys_ode, [0., t_end], [x0])
        t_solve, x_solve = xs.t, xs.y.squeeze()
        xs_prime = plant.sys(x_solve)

        ax.plot(x, x_prime, 'b')
        ax.plot(x_solve, xs_prime, 'r')
        ax.plot(x_solve[0],  xs_prime[0],  'o')
        ax.plot(x_solve[-1], xs_prime[-1], 's')
        
        fig, ax = plt.subplots()
        ax.grid()
        
        # open loop
        ax.plot(t_solve, x_solve)
        # close loop with u1
        xs = solve_ivp(plant.sys_ode_u1, [0., t_end], [x0])
        ax.plot(xs.t, xs.y.squeeze())
        xs = solve_ivp(plant.sys_ode_u2, [0., t_end], [x0])
        ax.plot(xs.t, xs.y.squeeze())
        xs = solve_ivp(plant.sys_ode_u3, [0., t_end], [x0])
        ax.plot(xs.t, xs.y.squeeze())
        
    plt.show()