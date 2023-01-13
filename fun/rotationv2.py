from colorsys import yiq_to_rgb
from tkinter import OFF
from traceback import clear_frames
import numpy as np
import matplotlib.pyplot as plt

def rotation(x,y,theta):
	xr = x*np.cos(theta)+y*np.sin(theta)
	yr = -x*np.sin(theta)+y*np.cos(theta)
	return(xr,yr)


def rotation_3d(v,theta,beta,garma):
    R = np.array(((np.cos(beta)*np.cos(garma),np.sin(theta)*np.sin(beta)*np.cos(garma)-np.cos(theta)*np.sin(garma),np.cos(theta)*np.sin(beta)*np.cos(garma)+np.sin(theta)*np.sin(garma)),
                (np.cos(beta)*np.sin(garma),np.sin(theta)*np.sin(beta)*np.sin(garma)+np.cos(theta)*np.cos(garma),np.cos(theta)*np.sin(beta)*np.sin(garma)-np.sin(theta)*np.cos(garma)),
                (-np.sin(beta),np.sin(theta)*np.cos(beta),np.cos(theta)*np.cos(beta))))
    
    return(np.dot(R,v))
 

v=np.array([[1,-1,-1, 1,],
            [1, 1,-1,-1,],
            [-1, -1, -1,-1,]])
v2=np.array([[1, 1, 1, 1,],
            [1, 1,-1,-1,],
            [-1, 1, 1, -1,]])
v3=np.array([[1, 1, -1, -1,],
            [1, -1,-1, 1,],
            [1, 1, 1,  1,]])
v4=np.array([[-1, -1, -1, -1,],
            [1, -1,-1, 1,],
            [1, 1, -1,  -1,]])
v5=np.array([[1, 1, -1, -1,],
             [-1, -1,-1, -1,],
             [-1, 1, 1,  -1,]])
v6=np.array([[1, 1, -1, -1,],
            [1, 1, 1, 1,],
            [-1, 1, 1,  -1,]])

theta= np.pi/4.2
beta = np.pi/7.2
garma = np.pi/2.3
v  = rotation_3d(v,theta,beta,garma)
v2 = rotation_3d(v2,theta,beta,garma)
v3 = rotation_3d(v3,theta,beta,garma)
v4 = rotation_3d(v4,theta,beta,garma)
v5 = rotation_3d(v5,theta,beta,garma)
v6 = rotation_3d(v6,theta,beta,garma)

theta = -np.pi/45
beta  = np.pi/45
garma = np.pi/45
i=0
ax = plt.axes()
ax.set_xlim(-3,3)
ax.set_ylim(-3,3)
ax.set_aspect('equal')

while i<=300:
    ax.cla()
    ax.axis("off")
    z=[]
    rotate  = rotation_3d(v,theta,beta,garma)
    rotate2 = rotation_3d(v2,theta,beta,garma)
    rotate3 = rotation_3d(v3,theta,beta,garma)
    rotate4 = rotation_3d(v4,theta,beta,garma)
    rotate5 = rotation_3d(v5,theta,beta,garma)
    rotate6 = rotation_3d(v6,theta,beta,garma)
    z.append(max(rotate[2]))
    z.append(max(rotate2[2]))
    z.append(max(rotate3[2]))
    z.append(max(rotate4[2]))
    z.append(max(rotate5[2]))
    z.append(max(rotate6[2]))

    m = max(z)
    if (m in rotate[2]):
        ax.fill(rotate[0], rotate[1],c="b")
    if (m in rotate2[2]):
        ax.fill(rotate2[0], rotate2[1],c="r")
    if (m in rotate3[2]):
        ax.fill(rotate3[0], rotate3[1],c="black")
    if (m in rotate4[2]):    
        ax.fill(rotate4[0], rotate4[1],c="brown")
    if (m in rotate5[2]):
        ax.fill(rotate5[0], rotate5[1],c="g")
    if (m in rotate6[2]):
        ax.fill(rotate6[0], rotate6[1],c="yellow")
    
    v =rotate
    v2 = rotate2
    v3 = rotate3
    v4 = rotate4
    v5 = rotate5
    v6 = rotate6
    
    i+=1
    plt.pause(0.1)
    #
plt.show()