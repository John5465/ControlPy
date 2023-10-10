"""A general class for phase portrait plot
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class PhasePortrait2D(object):
    """class for phase portrait

    Args:
        sys (function): system state function
    """
    def __init__(self, sys, var_num : int = 2) -> None:
        self._sys = sys
        self._x_lim = [-10., 10.]
        self._fig_size = 7
        self._x_num = var_num
        
    def draw_phase_portrait(self, axis: plt.Axes = None, x_lim: list = None) -> plt.Axes:
        if axis is not None:
            ax = axis
        else:
            fig, ax = plt.subplots()
            fig.set_size_inches(self._fig_size, self._fig_size)
            
        if x_lim is None:
            x_lim = self._x_lim
        
        x_spl  = [np.arange(x_lim[0], x_lim[1], 1.) for i in range(self._x_num)]
        x_mesh = np.meshgrid(x_spl[0], x_spl[1])
        
        n_i, n_j = x_mesh[0].shape
        
        u, v = np.zeros([n_i, n_j]), np.zeros([n_i, n_j])
        
        for i in range(n_i):
            for j in range(n_j):
                x1 = x_mesh[0][i, j]
                x2 = x_mesh[1][i, j]
                x_prime = self._sys([x1, x2])
                u[i, j] = x_prime[0]
                v[i, j] = x_prime[1]
                
        ax.quiver(x_mesh[0], x_mesh[1], u, v, units='xy', color='b')

        return ax
    
    def draw_trajectory(self, axis: plt.Axes = None, x0:list = [0., 0.], t_end: float = 10.) -> plt.Axes:
        if axis is not None:
            ax = axis
        else:
            fig, ax = plt.subplots()
            fig.set_size_inches(self._fig_size, self._fig_size)
            
        tspan = np.arange(0, t_end, 0.5)
        
        xs = odeint(self._sys, x0, tspan)
        
        ax.plot(xs[ :, 0], xs[ :, 1], 'r-')   # trajectory
        ax.plot(xs[ 0, 0], xs[ 0, 1], 'o')    # start
        ax.plot(xs[-1, 0], xs[-1, 1], 's')    # end
            
        return ax
    
if __name__ == "__main__":
    """Demo
    """
    def sys(X:list, t=0.):
        return [X[1], -np.sin(X[0])]
    
    phase_portrait = PhasePortrait2D(sys)
    
    ax = phase_portrait.draw_phase_portrait()
    
    x0 = [0., 1.]
    ax = phase_portrait.draw_trajectory(ax, x0)
    
    plt.show()
