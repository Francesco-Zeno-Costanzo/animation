import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N=30
def quadr(x, k):
    return (4 / (k * np.pi)) * (np.sin((2 * np.pi * k * x)))

yy=np.linspace(-2, 2, 10000)

C=np.zeros(len(yy))
A=np.zeros((len(yy), N))

for i in range (0,N):
    k=2*i+1
    C=C+quadr(yy,k)
    A[:,i]=C

plt.figure(1)
plt.grid()
plt.plot(yy,C)

fig = plt.figure(2)

plt.title("Sviluppo di Fourier per l'onda quadra N=%d" %N)
plt.xlim(np.min(yy), np.max(yy))
plt.ylim(np.min(C)-1/2, np.max(C)+1/2)
plt.grid()

line, = plt.plot([], [], 'b')
def animate(i):
    line.set_data(yy, A[:,i])
    return line,


anim = animation.FuncAnimation(fig, animate, frames=N, interval=200, blit=True, repeat=True)
#anim.save('Fourier.mp4', fps=5, extra_args=['-vcodec', 'libx264'])

plt.show()