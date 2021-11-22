 # Import the required modules
import numpy as np
import matplotlib.pyplot as plt
# This makes the plots appear inside the notebook
# %matplotlib inline
from scipy.integrate import odeint

# define a projection from the 3D simplex on a triangle
proj = np.array(
[[-1 * np.cos(30. / 360. * 2. * np.pi),np.cos(30. / 360. * 2. * np.pi),0.],
[-1 * np.sin(30. / 360. * 2. * np.pi),-1 * np.sin(30. / 360. * 2. * np.pi),1.]])
# project the boundary on the simplex onto the boundary of the triangle
ts = np.linspace(0, 1, 10000)
PBd1 = proj@np.array([ts,(1-ts),0*ts])
PBd2 = proj@np.array([0*ts,ts,(1-ts)])
PBd3 = proj@np.array([ts,0*ts,(1-ts)])


# choose game
# game Ex 1.7 notes
# A = np.array([[ 0, 1 ,0], [ 0, 0 ,2], [ 0, 0 ,1]]) # row, 2nd row, 3rd row
A = np.array([[ 2, 0 ,1], [ 1, 2 ,0], [ 0, 1 ,2]]) # row, 2nd row, 3rd row

x01 = np.array([0.92, 0.01, 0.07])
x02 = np.array([0.65,0.05,0.3])
x03 = np.array([2/3, 1/3, 0])
x04 = np.array([2/3, 1/3, 0])
x05 = np.array([2/3, 1/3, 0])
x06 = np.array([2/3, 1/3, 0])

#define replicator equation
def replicator(x,t):
    return x * (A@x - np.transpose(x) @ (A@x))
# compute orbits
ts = np.linspace(0,100,10000)
xt1 = odeint(replicator, x01, ts)
xt2 = odeint(replicator, x02, ts)
xt3 = odeint(replicator, x03, ts)


 # project the orbits on the triangle
orbittriangle1=proj@xt1.T
orbittriangle2=proj@xt2.T
orbittriangle3=proj@xt3.T
ic1=proj@x01
ic2=proj@x02
ic3=proj@x03
# no box
plt.box(False)
plt.axis(False)
# plot the orbits, the initial values, the corner points, and the boundary points
plt.plot(orbittriangle1[0],orbittriangle1[1],".",markersize=10,color='green')
plt.plot(orbittriangle2[0],orbittriangle2[1],".",markersize=10,color='red')
plt.plot(orbittriangle3[0],orbittriangle3[1],".",markersize=10,color='blue')
plt.plot(ic1[0],ic1[1],"+",markersize=10,color='green')
plt.plot(ic2[0],ic2[1],"+",markersize=10,color='red')
plt.plot(ic3[0],ic3[1],"+",markersize=10,color='blue')
plt.text(-0.8660254-0.1, -0.5 +0.05 , "$e_1$",fontsize=12)
plt.text(+0.8660254+0.05, -0.5 +0.05 , "$e_2$",fontsize=12)
plt.text(0-0.03, 1 +0.1 , "$e_3$",fontsize=12)
plt.plot(PBd1[0], PBd1[1], ".",color='black',markersize=1)
plt.plot(PBd2[0], PBd2[1], ".",color='black',markersize=1)
plt.plot(PBd3[0], PBd3[1], ".",color='black',markersize=1)
# add the game matrix in the figure
for i in [0,1,2]:
    for j in [0,1,2]:
        c = A[i][j]
        plt.text(0.2*j-0.8, -0.2*i+0.9, str(c))
        plt.text(0.3-1.3,0.7,"A =")
#plt.text(0-0.03, 1 +0.1 ,A[0,0],A[0,1],A[0,2] ,fontsize=12)
#plt.plot(pE[0],pE[1],"+")
plt.savefig("flowportrait.pdf")
