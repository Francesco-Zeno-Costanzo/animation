import numpy as np
import matplotlib.pyplot as plt


def update(r, args_x, args_y):
    '''
    Function tha compute new point of attractor
    
    Parameters
    ----------
    r : 1darray
        old point, r = np.array([x, y])
    args_x : list or tulple
        parameter for new point on x
    args_y : list or tulple
        parameter for new point on y
    
    Returns
    -------
    [x_n, y_n] : list
        new point
    '''
    
    x, y = r
    
    pol = np.array([1, x, y, x*y, x**2, y**2])
    
    x_n = pol @ np.array(args_x)
    y_n = pol @ np.array(args_y)
    
    return [x_n, y_n]
    
#============================================================
# Parameters
#============================================================
    
N = int(1e5)

data1 = np.zeros((N + 1, 2))
data2 = np.zeros((N + 1, 2))


x0 = -0.72
y0 = -0.64

k1 = 0
k2 = 0
a = 0.9
b = -0.6013
c = 2
d = 0.5

data1[0, :] = [x0, y0] 
data2[0, :] = [0,   0]

#============================================================
# computation
#============================================================

for i in range(N):
	data1[i+1, :] = update(data1[i, :], args_x=(k1, a, b, 0, 1, -1), args_y=(k2, c, d, 2, 0, 0))
	data2[i+1, :] = update(data2[i, :], args_x=(-0.8, -0.1, 0.3, -1.2, 1.1, 1.1), args_y=(0, 0.3, -1.1, 0.2, 0.4, 0.7))

#============================================================
# Plot
#============================================================
	
plt.figure(1)	

plt.plot(data1[:,0], data1[:,1],'.',markersize = 1)

plt.figure(2)

plt.plot(data2[:,0], data2[:,1],'.',markersize = 1)

plt.show()


