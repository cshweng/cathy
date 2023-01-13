


import numpy as np
import matplotlib.pyplot as plt

def rotation(x,y,theta):
	xr = x*np.cos(theta)+y*np.sin(theta)
	yr = -x*np.sin(theta)+y*np.cos(theta)
	return(xr,yr)


def rotation_3d(x,y,z,theta):
    xr = x*np.cos(theta)-y*np.sin(theta)
    yr = x*np.sin(theta)+y*np.cos(theta)
    zr = z
    return(xr,yr,zr)
#plt.axis

#.set_aspect('equal')
x=np.linspace(0,5,30)
x= np.meshgrid(x,x)
y=np.linspace(0,5,30)
z=np.linspace(0,10,30)
theta=np.pi/10

i=0
ax = plt.axes(projection='3d')
while i<=30:
	#plt.cla()
	
	ax.set_xlim3d(-10, 10) 
	ax.set_ylim3d(-10, 10)
	ax.set_zlim3d(-10, 10)
	#plt.axes().set_aspect('equal')
	xr,yr,zr = rotation_3d(x,y,z,theta)
	ax.scatter(xr,yr,zr,c="b",s=2)
	x = xr
	y = yr
	plt.pause(0.1)
	i+=1
plt.show()
