import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#=======================================================
# Parameters
#=======================================================

T  = 2*np.pi
N  = 5000
o1 = 8
o2 = 9
t  = np.linspace(0,T, N)

#=======================================================
# Data
#=======================================================

x = np.sin(o1*t)
y = np.sin(o2*t)

#=======================================================
# Animation
#=======================================================

fig, ax = plt.subplots(1)
plt.title("Curve di lissajous $\omega_x$= %.2f; $\omega_y$= %.2f" %(o,o1), fontsize=20)
ax.set_xlim(np.min(x)-0.1,np.max(x)+0.1)
ax.set_ylim(np.min(y)-0.1,np.max(y)+0.1)
ax.set_xlabel('X(t)')
ax.set_ylabel('Y(t)')
plt.grid()

dot, = plt.plot([], [],'ro')
line, =plt.plot([], [],'b-')

def animate(i):
    dot.set_data(x[i],y[i])
    line.set_data(x[:i],y[:i])
    return dot, line

anim = animation.FuncAnimation(fig, animate, frames=N, interval=1, blit=True, repeat=True)

#anim.save('Curve di lissajous.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()

#=======================================================
# Plot
#=======================================================

plt.figure(2)
plt.title("Curve di lissajous $\omega_x$= %.2f; $\omega_y$= %.2f" %(o,o1), fontsize=20)
plt.xlabel('X(t)')
plt.ylabel('Y(t)')
plt.grid()

plt.plot(x,y)

plt.show()
