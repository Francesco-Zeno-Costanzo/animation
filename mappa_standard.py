import glob
import imageio
import numpy as np
import matplotlib.pyplot as plt

#=======================================================
# Parameters
#=======================================================

num_steps = 1000 # number of points

N = 15           # grid size on x
M = 15           # grid size on y
K = 0.99         # parameter of the mapp

t_0 = np.linspace(0, 6, N)  # initial condition
p_0 = np.linspace(-3, 3, M)

#=======================================================
# Simulation
#=======================================================

def MS(t0, p0, K):
    '''
    Return an iteretion of standard map
    
    Parameter
    ---------
    t0 : float
        initial condition
    p0 : float
        initial condition
    K : float
        parameter of mapp
    
    Returns
    -------
    t, p : 1darray, an iteration of the map 
    '''

    p = np.zeros(num_steps + 1)
    t = np.zeros(num_steps + 1)

    p[0], t[0] = p0, t0

    for i in range(num_steps):
        p[i + 1] = p[i] + K*np.sin(t[i])

        if p[i + 1] > np.pi:
            p[i + 1] -= 2*np.pi
        if p[i + 1] < -np.pi:
            p[i + 1] += 2*np.pi

        t[i + 1] = t[i] + p[i + 1]

        if t[i + 1] > 2*np.pi:
            t[i + 1] -= 2*np.pi
        if t[i + 1] < 0:
            t[i + 1] += 2*np.pi


    return t, p

#=======================================================
# Plot
#=======================================================

plt.figure(1)
plt.title(f"Standatd map con k = {K}", fontsize=20)
for t0 in t_0:
    for p0 in p_0:
        plt.grid()
        a, b = MS(t0, p0, K)
        plt.plot(a, b, linestyle='', marker='.')

plt.show()

#=======================================================
# Animation
#=======================================================
"""
path = r'...'
def GIF(path, name, ext='png'):
    '''
    function to create a gif from several plot
    
    Parameters
    ----------
    path : string
        path of the varius plot
    name : string
        name of the gif
    ext : string, optional, default .png
        type of file
    
    '''

    path_in = path+'/*.'+ext
    path_out = path+f'/{name}.gif'

    imgs=[]

    file = glob.glob(path_in, recursive = True)
    file.sort(key=len)
    for im in file:
        imgs.append(imageio.imread(im))

    imageio.mimsave(path_out, imgs)

K = np.linspace(0, 1, 100)
for i in range(len(K)):
    fig = plt.figure(i)
    plt.title(f'Mappa standatd con k = {K[i]:.3f}', fontsize=20)
    for t0 in t_0:
        for p0 in p_0:
            plt.grid()
            a, b = MS(t0, p0, K[i])
            plt.plot(a, b, linestyle='',marker='.')
    plt.savefig(path + '/%d'%(i))
    plt.close(fig)

GIF(path, 'standard map')
"""
