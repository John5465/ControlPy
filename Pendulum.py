import numpy as np
import matplotlib.pyplot as plt
from PhasePortrait2D import PhasePortrait2D

class Pendulum(object):
    def  __init__(self, L:float = 10.):
        self._g = 9.81 # m/s^2
        self._L = L
        self._m = 1.
    
    def sys(self, x, t=0.):
        g, L = self._g, self._L
        return [x[1], (-g/L)*np.sin(x[0])]
    
    def sys_with_friction(self, x, t=0.):
        g, L = self._g, self._L
        k = 0.3
        m = self._m
        return [x[1], (-g/L)*np.sin(x[0]) + (-k/m)*x[1]]
    
if __name__ == "__main__":    
    pendulum = Pendulum()
    
    phase_portrait = PhasePortrait2D(pendulum.sys)
    
    ax = phase_portrait.draw_phase_portrait()
    
    x0 = [1., 5.]
    phase_portrait.draw_trajectory(ax, x0, t_end=1000.)
    
    plt.show()