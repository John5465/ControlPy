import numpy as np
import sympy
import matplotlib.pyplot as plt
from PhasePortrait2D import PhasePortrait2D
from scipy.linalg import solve_continuous_are

class LQRController(object):
    def __init__(self):
        pass

    def compute(self, A, B, Q, R):
        # first, try to solve the ricatti equation
        X, K = self.solve_CARE(A, B, Q, R)
        
        eig_val, eig_vec = np.linalg.eig(A - B @ K)
        
        return K, X, eig_val

    def solve_CARE(self, A, B, Q, R):
        X = solve_continuous_are(A, B, Q, R)
        E = np.eye(X.shape[0])
        S = np.zeros([B.T.shape[0], E.shape[1]])
        
        K = np.linalg.inv(R) @ (B.T @ X @ E + S)

        return X, K

    def solve_DARE(self, A, B, Q, R):
        """
        solve a discrete time_Algebraic Riccati equation (DARE)
        """
        X = Q
        maxiter = 150
        eps = 0.01

        for i in range(maxiter):
            Xn = A.T @ X @ A - A.T @ X @ B @ \
                np.linalg.inv(R + B.T @ X @ B) @ B.T @ X @ A + Q
            if (abs(Xn - X)).max() < eps:
                break
            X = Xn

        K = np.linalg.inv(B.T @ X @ B + R) @ (B.T @ X @ A)

        return Xn, K

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
    
if __name__ == "__main__":
    plant = Plant()
    
    eg_value, eg_vector = np.linalg.eig(plant.A)
    
    print(eg_value)
    
    # draw phase portrait
    if False:
        phase_portrait = PhasePortrait2D(plant.sys_A)
        ax = phase_portrait.draw_phase_portrait()
        
        #x0 = [5., 0.]
        #phase_portrait.draw_trajectory(ax, x0, t_end=5.)
        
    # LQR
    lqr = LQRController()
    
    Q = np.array([[ 1., 0.],
                  [ 0., 1.]])
    R = np.array([100.])[np.newaxis]
    K, X, eig_val = lqr.compute(plant.A, plant.B, Q, R)
    
    if True:
        A_cl = plant.A - plant.B @ K
        
        def f(x, u=0., t=0.):
            return (A_cl @ np.array(x) + plant.B @ np.array(u)[np.newaxis]).tolist()
        
        phase_portrait = PhasePortrait2D(f)
        ax = phase_portrait.draw_phase_portrait()
        
        x0 = [1., 0.]
        phase_portrait.draw_trajectory(ax, x0, t_end=5.)
        
    plt.show()