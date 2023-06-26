import numpy as np
import matplotlib.pyplot as plt

def update(r,a,b,c,d,k1,k2):
	x = r[0]
	y = r[1]
	return [k1+x**2-y**2+a*x+b*y,k2+2*x*y+c*x+d*y]
	
def update1(r,k1,a,b,c,d,e,f,g,h,i,j):
	x = r[0]
	y = r[1]
	return [k1+a*x+b*x**2+c*x*y+d*y+e*y**2,f*x+g*x**2+h*x*y+i*y+j*y**2]
	
N = 100000

x0 = -0.72
y0 = -0.64

k1 = 0
k2 = 0
a = 0.9
b = -0.6013
c = 2
d = 0.5

data = np.zeros((N+1,2))
data[0,:] = [x0,y0] 
plt.figure(1)
for i in range(N):
	data[i+1,:] = update(data[i,:],a,b,c,d,k1,k2)
plt.plot(data[:,0],data[:,1],'.',markersize = 1)


data[0,:] = [0,0] 
plt.figure(2)
for i in range(N):
	data[i+1,:] = update1(data[i,:],-0.8,-0.1,1.1,-1.2,0.3,1.1,0.3,0.4,0.2,-1.1,0.7)
plt.plot(data[:,0],data[:,1],'.',markersize = 1)

plt.show()


