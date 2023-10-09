import numpy as np
import matplotlib.pyplot as plt

def f(X, t):
    x1, x2 = X
    return [x2 - 0.5*x1, np.sin(x1)]

x1 = np.linspace(-6.0, 6.0, 50)
x2 = np.linspace(-6.0, 6.0, 50)

X1, X2 = np.meshgrid(x1, x2)

t = 0

u, v = np.zeros(X1.shape), np.zeros(X2.shape)

NI, NJ = X1.shape

#for i, j in zip(range(NI), range(NJ)):
for i in range(NI):
    for j in range(NJ):
        x = X1[i, j]
        y = X2[i, j]
        xprime = f([x, y], t)
        u[i,j] = xprime[0]
        v[i,j] = xprime[1]
    
Q = plt.quiver(X1, X2, u, v, color='r', units='xy')

plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.xlim([-6, 6])
plt.ylim([-6, 6])

plt.show()
