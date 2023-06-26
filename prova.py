import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


sizept = 3                  # dimesioni punti
N = int(1e6)                # numero di punti

points = np.zeros([N, 2])  # Matrice che conterrà i punti
alpha = 3*np.pi/5
#z1 = [0, 0]                # primo vertice
#z2 = [1, 0]                # secondo vertice
#z3 = [1-np.cos(alpha), np.sin(alpha)]   # terzo vertice
#z4 = [1/2, np.sin(alpha)+np.cos(alpha/2)]
#z5 = [np.cos(alpha), np.sin(alpha)]

z1 = np.array([[0, 0],
      [1, 0],
      [1-np.cos(alpha), np.sin(alpha)],
      [1/2, np.sin(alpha)+np.cos(alpha/2)],
      [np.cos(alpha), np.sin(alpha)]
     ])

yr = 0                     # y primo punto iterazione
xr = 1/2                   # x primo punto iterazione
	
def newp(z):
    #estraggo a caso un vertice
    index = int(random.uniform(0,5))
    #print(z1.shape)
    #media del punto con il vertice estratto
    lamb = 1/((1+np.sqrt(5))/2)
    xn = z[0] + (z1[index, 0] - z[0])*lamb
    yn = z[1] + (z1[index, 1] - z[1])*lamb
    return xn, yn
 

points[0, :] = xr, yr # punto inizale

for i in range(1,len(points[:,0])):  #creo il triangolo
    points[i,:] = newp(points[i-1,:])


#Plot
fig = plt.figure(1)
plt.title(f"Sierpinski Triangle - {N:.1e} points")
plt.plot(z1[:, 0], z1[:, 1],'b.',markersize=sizept)
plt.plot(points[:,0],points[:,1],'b.',markersize=sizept)
plt.grid()

plt.show()
