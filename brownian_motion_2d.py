import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

random.seed(42)

#=======================================================
# Parameters
#=======================================================

T = 10000 # time
l = 5     # step size

x = np.array([])
y = np.array([])
x = np.insert(x, 0, random.uniform(0,7)) # intial conditions
y = np.insert(y, 0, random.uniform(0,7))

#=======================================================
# simulation
#=======================================================

for i in range(0, T):
    angle = random.uniform(0, 2*np.pi)
    r = l*np.cos(angle)
    b = l*np.sin(angle)
    x = np.insert(x, len(x), x[i] + r)
    y = np.insert(y, len(y), y[i] + b)

#=======================================================
# Animation
#=======================================================

fig, ax = plt.subplots(1)
plt.title("Brownian motion", fontsize=20)
ax.set_xlim(np.min(x),np.max(x))
ax.set_ylim(np.min(y),np.max(y))
ax.set_xlabel('X(t)')
ax.set_ylabel('Y(t)')
plt.grid()


redDot, = plt.plot([], [], 'ro')
line, = plt.plot([],[],'b-', lw=0.5)
def animate(i):
    redDot.set_data(x[i], y[i])
    line.set_data(x[:i],y[:i])
    return redDot, line

anim = animation.FuncAnimation(fig, animate, frames=range(0, T), interval=5, blit=True, repeat=False)
#anim.save('Moto browniano.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()

#=======================================================
# Plot
#=======================================================

plt.figure(2)
plt.title("Brownian motion" , fontsize=20)
plt.xlabel('X(t)')
plt.ylabel('Y(t)')
plt.grid()

plt.plot(x, y)

plt.show()
