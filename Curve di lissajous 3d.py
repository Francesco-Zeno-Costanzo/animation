import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
o=3
def fx(t):
    return np.sin(o*t)
o1=5
def fy(t):
    return np.sin(o1*t)
o2=8
def fz(t):
    return np.sin(o2*t)

T=2*np.pi
N=5000
x = np.array([])
y = np.array([])
z = np.array([])
t = np.linspace(0,T, N)


x = np.append(x, fx(t))
y = np.append(y, fy(t))
z = np.append(z, fz(t))

fig = plt.figure()
ax = fig.gca(projection='3d')
plt.title("Curve di lissajous 3d \n $\omega_x$= %.2f; $\omega_y$= %.2f; $\omega_z$= %.2f" %(o, o1, o2), fontsize=20)
ax.set_xlim(np.min(x)-0.1,np.max(x)+0.1)
ax.set_ylim(np.min(y)-0.1,np.max(y)+0.1)
ax.set_zlim(np.min(z)-0.1,np.max(z)+0.1)
ax.set_xlabel('X(t)')
ax.set_ylabel('Y(t)')
ax.set_ylabel('Z(t)')
plt.grid()

dot, = plt.plot([], [], [],'ro')
line, =plt.plot([], [], [],'b-')

def animate(i):
    dot.set_data_3d(x[i],y[i], z[i])
    line.set_data_3d(x[:i],y[:i], z[:i])
    return line, dot

anim = animation.FuncAnimation(fig, animate, frames=N, interval=1, blit=True, repeat=True)

#anim.save('Curve di lissajous 3d .mp4', fps=100, extra_args=['-vcodec', 'libx264'])

fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')
plt.grid()

ax1.set_title("Curve di lissajous 3d \n $\omega_x$= %.2f; $\omega_y$= %.2f; $\omega_z$= %.2f" %(o, o1, o2), fontsize=20)
ax1.set_xlabel('X(t)')
ax1.set_ylabel('Y(t)')
ax1.set_zlabel('Z(t)')
plt.grid()

ax1.plot(x,y,z)

plt.show()