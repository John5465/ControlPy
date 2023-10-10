import numpy as np
import matplotlib.pyplot as plt
from PhasePortrait2D import PhasePortrait2D

class PlantError(object):
    def __init__(self, L:float = 1., xd:float = 5.):
        self._g = 10
        self._L = L
        self._xd = xd
        
        g = self._g
        self._A = np.array([[  0., -1.], 
                            [-g/L,  0.]])
        self._B = np.array([[ 0.], 
                            [-1.]])
        self._E = np.array([[(g/L) * self._xd],
                            [0.]])
    
    def sys_A(self, x, u=0., t=0.):
        return (self._A @ np.array(x) + self._B @ np.array(u)[np.newaxis] + self._E.squeeze()).tolist()
    
    @property
    def A(self):
        return self._A
    
    @property
    def B(self):
        return self._B
    
if __name__ == "__main__":
    plant = PlantError()

    if True:
        phase_portrait = PhasePortrait2D(plant.sys_A)
        ax = phase_portrait.draw_phase_portrait()
        
        #x0 = [5., 0.]
        #phase_portrait.draw_trajectory(ax, x0, t_end=5.)

    plt.show()