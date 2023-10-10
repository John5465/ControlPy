import numpy as np
import matplotlib.pyplot as plt
from PhasePortrait2D import PhasePortrait2D

class Plant(object):
    def __init__(self, L:float = 1.):
        self._g = 10
        self._L = L
        
        g = self._g
        self._A = np.array([[ 0., 1.], 
                            [g/L, 0.]])
        self._B = np.array([[ 0.], 
                            [-1.]])
    
    def sys_A(self, x, u=0., t=0.):
        return (self._A @ np.array(x) + self._B @ np.array(u)[np.newaxis]).tolist()
    
    @property
    def A(self):
        return self._A
    
    @property
    def B(self):
        return self._B