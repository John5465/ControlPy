import numpy as np
import matplotlib.pyplot as plt
from PhasePortrait2D import PhasePortrait2D

class SpringDamperSystem(object):
    def __init__(self):
        self._m = 1.0
        self._k = 0.2
        self._b = 0.5
    
    def f_sys(self, X:np.array=np.array([0., 0.]), t=0., u:float=0.) -> np.array:
        X = np.array(X)
        return self.f_state(X) + self.f_input(u)
    
    def f_state(self, X) -> np.array:
        m, alpha = self._m, self._alpha
        state = [X[1], (-alpha/m) * (X[0]**3)]
        return np.array(state)
    
    def f_input(self, u) -> np.array:
        m = self._m
        vec_input = [0., (1./m)*u]
        return np.array(vec_input)
    
    
if __name__ == "__main__":
    sys = SpringDamperSystem()
    
    # phase portrait
    if True:        
        phase_portrait = PhasePortrait2D(sys.f_sys)
        ax = phase_portrait.draw_phase_portrait()
        
        x0 = [1., 0.]
        t_end = 100.
        phase_portrait.draw_trajectory(ax, x0=x0, t_end=t_end)
        
    plt.show()