import numpy as np
import matplotlib.pyplot as plt

# state space
A = np.array([[0., 2.],
			  [0., 3.]])

A_eigenvalue, A_featvec = np.linalg.eig(A)

# phase portraits
def f_open_loop(X:np.array, t):
	return A @ X



#t = 0.

#x1 = np.linspace(-10.0, 10.0, 50)
#x2 = np.linspace(-10.0, 10.0, 50)

#X1, X2 = np.meshgrid(x1, x2)

#u, v = np.zeros(X1.shape), np.zeros(X2.shape)

#NI, NJ = X1.shape

#for i in range(NI):
#    for j in range(NJ):
#        x = X1[i, j]
#        y = X2[i, j]
#        yprime = f_open_loop([x, y], t)
#        u[i,j] = yprime[0]
#        v[i,j] = yprime[1]

#Q = plt.quiver(X1, X2, u, v, color='r')

#plt.xlabel('$y_1$')
#plt.ylabel('$y_2$')
#plt.xlim([-6, 6])
#plt.ylim([-6, 6])

#from scipy.integrate import odeint

#for y20 in [0, 0.5, 1, 1.5, 2, 2.5]:
#    tspan = np.linspace(0, 50, 200)
#    y0 = [0.0, y20]
#    ys = odeint(f_open_loop, y0, tspan)
#    plt.plot(ys[:,0], ys[:,1], 'b-') # path
#    plt.plot([ys[0,0]], [ys[0,1]], 'o') # start
#    plt.plot([ys[-1,0]], [ys[-1,1]], 's') # end

#plt.show()