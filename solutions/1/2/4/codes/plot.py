import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

fig = plt.figure()
len = 100
y = np.linspace(-4,4,len)

def parab_gen(y,a):
    x = y**2/a
    return x

V = np.array(([0,0],[0,1]))
u = np.array(([-2,-1]))
f = 5

D_vec,P = LA.eig(V)
D = np.diag(D_vec)

p = P[:,0]
eta = 2*u@p

foc = -eta/D_vec[1]

x = parab_gen(y,foc)

cA = np.vstack((u+eta*0.5*p,V))
cb = np.vstack((-f,(eta*0.5*p-u).reshape(-1,1)))
c = LA.lstsq(cA,cb,rcond=None)[0]
c = c.flatten()

xStandardparab = np.vstack((x,y))

xActualparab = P@xStandardparab + c[:,np.newaxis]

plt.plot(xActualparab[0,:],xActualparab[1,:],label='Given Parabola',color='r')
plt.plot(xStandardparab[0,:],xStandardparab[1,:],label='Standard Parabola',color='b')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
