import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

random.seed(42)

T=1000
l=2

x=np.array([])
y=np.array([])
z=np.array([])
x=np.insert(x,0,random.uniform(0,7))
y=np.insert(y,0,random.uniform(0,7))
z=np.insert(z,0,random.uniform(0,7))

for i in range(0,T):
    t = random.uniform(0, 2*np.pi)
    f = random.uniform(0, np.pi)
    r = l*np.cos(t)*np.sin(f)
    b = l*np.sin(t)*np.sin(f)
    g = l*np.cos(f)
    x=np.insert(x,len(x),x[i]+r)
    y=np.insert(y,len(y),y[i]+b)
    z=np.insert(z,len(z),z[i]+g)

fig = plt.figure()
ax = fig.gca(projection='3d')
plt.grid()
ax.set_title('Moto browniano 3d', fontsize=20)
ax.set_xlabel('X(t)')
ax.set_ylabel('Y(t)')
ax.set_zlabel('Z(t)')
ax.set_xlim(np.min(x),np.max(x))
ax.set_ylim(np.min(y),np.max(y))
ax.set_zlim(np.min(z),np.max(z))

a, = ax.plot([], [], [], 'ro')
line, = plt.plot([],[],[],'b-', lw=0.5)

def animate(i):
    a.set_data_3d(x[i], y[i], z[i])
    line.set_data_3d(x[:i],y[:i], z[:i])
    return a,line

anim = animation.FuncAnimation(fig, animate, frames=1000, interval=50, blit=True, repeat=False)
#anim.save('Moto browniano 3d.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')
plt.grid()

ax1.set_title('Moto browniano 3d', fontsize=20)
ax1.set_xlabel('X(t)')
ax1.set_ylabel('Y(t)')
ax1.set_zlabel('Z(t)')
plt.grid()

ax1.plot(x,y,z)

plt.show()