import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#=======================================================
# Parameters
#=======================================================

sizept = 3                 # dimensions fo points
N = int(1e6)               # number of points

points = np.zeros([N, 2])  # matrix to store data

z1 = [0, 0]                # first  vertex of the triangle
z2 = [1, 0]                # second vertex of the triangle
z3 = [1/2, np.sqrt(3)/2]   # third  vertex of the triangle

yr = 0                     # initial condition on y
xr = 1/2                   # initial condition on x

zoom = True                # if true there is a zoom in the animation

#=======================================================
# Computation
#=======================================================
	
def newp(z):
    '''
    algorithm for constructing the Serpinski triangle
    
    Parameters
    ----------
    z : 1darray
        point of triangle at previus iteration
    
    Returns
    -------
    new point of the triangle
    '''
    # choice a vertex randomly
    index = int(random.uniform(1,4))
    # find new point
    if index == 1:
        return [(z[0] + z1[0])/2, (z[1] + z1[1])/2]
        
    if index == 2:
        return [(z[0] + z2[0])/2, (z[1] + z2[1])/2]
    
    if index == 3:
        return [(z[0] + z3[0])/2, (z[1] + z3[1])/2]
 

points[0, :] = xr, yr # initial point

for i in range(1,len(points[:,0])):  # loop for the serpinski triangle
    points[i,:] = newp(points[i-1,:])


#=======================================================
# Plot
#=======================================================

fig = plt.figure(1)
plt.title(f"Sierpinski Triangle - {N:.1e} points")
plt.plot([0,1,1/2],[0,0,np.sqrt(3)/2],'b.',markersize=sizept)
plt.plot(points[:,0],points[:,1],'b.',markersize=sizept)
plt.grid()


#=======================================================
# Animation
#=======================================================

fig = plt.figure(2, figsize=(16, 16))
plt.title(f"Sierpinski Triangle - {N:.1e} points")
plt.plot([0,1,1/2], [0,0,np.sqrt(3)/2],'b.',markersize=sizept)
plt.grid()

dot, = plt.plot([], [], 'b.',markersize=sizept)
def animate(i):
    if zoom : plt.ylim(i/N ,np.sqrt(3)/2)                     # Zoom y
    if zoom : plt.xlim(i/(N*np.sqrt(3)), 1-i/(N*np.sqrt(3)))  # Zoom x
    dot.set_data(points[:i,0], points[:i,1])
    return dot,


anim = animation.FuncAnimation(fig, animate, frames=np.arange(0, N, 3000), interval=100, blit=True, repeat=True)

plt.show()
