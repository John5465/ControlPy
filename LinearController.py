import numpy as np
import sympy
import matplotlib.pyplot as plt
from PhasePortrait2D import PhasePortrait2D

class Plant(object):
    def __init__(self):
        self._A = np.array([[0., 2.], 
                            [0., 3.]])
        self._B = np.array([[0.], 
                            [1.]])
        self._k = np.array([0., 0.])
    
    def sys_A(self, x, u=0., t=0.):
        return (self._A @ np.array(x) + self._B @ np.array(u)[np.newaxis]).tolist()
    
    def sys_close_A(self, x, t=0.):
        return (self._A @ np.array(x) + self._B @ self._k @ x).tolist()
    
    @property
    def A(self):
        return self._A
    
    @property
    def B(self):
        return self._B
    
    @property
    def k(self):
        return self._k
    @k.setter
    def k(self, k):
        self._k = np.array(k)[np.newaxis]
    
if __name__ == "__main__":
    plant = Plant()
    
    # draw phase portrait
    if False:
        phase_portrait = PhasePortrait2D(plant.sys_A)
        ax = phase_portrait.draw_phase_portrait()
        x0 = [1., 0.]
        phase_portrait.draw_trajectory(ax, x0)
        plt.show()
    
    eg_value, eg_vector = np.linalg.eig(plant.A)
    
    # derive
    if False:
        A_mat = sympy.Matrix(plant.A)
        B_mat = sympy.Matrix(plant.B)
        
        k = sympy.symbols('k1:3')
        K_mat = -sympy.Matrix(k)

        A_cl  = A_mat + B_mat * K_mat.T
        
        v = sympy.symbols('v')
        A_cl_lambda = sympy.Matrix([[v, 0.], [0., v]]) - A_cl
        
        A_cl_lambda_det = A_cl_lambda.det()
        #print(A_cl)
    
    # eigen value = [-1, -1], k1 = -0.5, k2 = 5
    k = [-0.5, -5]
    
    plant.k = k
        
    # phase portrait for close sys
    if True:
        phase_portrait = PhasePortrait2D(plant.sys_close_A)
        ax1 = phase_portrait.draw_phase_portrait()
        x0 = [1., 10.]
        phase_portrait.draw_trajectory(ax1, x0)
        
        #A_cl = np.array([[  0.,  2.,],
        #                 [-0.5, -2.]])
        
        #eg_value, eg_vector = np.linalg.eig(A_cl)
        #print(eg_value)
        
        #def f_Acl(x, t=0.):
        #    return (A_cl @ x).tolist()
        #phase_portrait = PhasePortrait2D(f_Acl)
        #ax2 = phase_portrait.draw_phase_portrait()
        
        plt.show()