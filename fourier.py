import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def quadr(x, k):
    '''
    general term of the series
    
    x : float time
    k : int   sum index
    '''
    
    return (4 / (k * np.pi)) * (np.sin((2 * np.pi * k * x)))

N = 30
y = np.linspace(-2, 2, 10000)
C = np.zeros(len(y))
A = np.zeros((len(y), N))

for i in range (0,N):
    k = 2*i + 1
    C = C + quadr(y,k)
    A[:,i] = C



fig = plt.figure(1)

plt.title("Animation of fourier's series N=%d" %N)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.xlim(np.min(y), np.max(y))
plt.ylim(np.min(C)-1/2, np.max(C)+1/2)
plt.grid()

line, = plt.plot([], [], 'b')
def animate(i):
    line.set_data(y, A[:,i])
    return line,


anim = animation.FuncAnimation(fig, animate, frames=N, interval=200, blit=True, repeat=True)
#anim.save('Fourier.mp4', fps=5, extra_args=['-vcodec', 'libx264'])

"""
plt.figure(2)
plt.title("square wave N=%d" %N)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.grid()
plt.plot(y, C)
"""
plt.show()
