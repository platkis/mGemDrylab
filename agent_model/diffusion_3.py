import numpy as np
from numpy.random import *
from matplotlib.pyplot import *
dt=0.002;
Dz=1;
dx=1;
dy=1;
#Those parameters fix the number of points in the grid. For isntance, the total x length of the plate will be dx*nx
nx=120;
ny=120;
nt=50000;
#We precharge the p matrix which will have inside the numerical solutions.
p=np.zeros([nx,ny,2]);
#Here we set the boundary conditions for t (can be call initial conditions). It is going to be 20 hot or cold points in random positions.
for f in range(20):
  p[round((nx-1)*rand()),round((ny-1)*rand()),0]=np.sign(rand()-0.51);
for m in range(1,nt):
  print(m)
#A simple implementation (but not quite eficient) will be iterating each point at a time. Because we have a matrix, we can operate with whole sections of the matrix at each time.
#Basically, we take time slices and operate them as a whole. To use centered differences, we simply shift the matrix one element in the x direction or in the y direction.
  
  if m == 0:
    p[1:nx-1,1:ny-1,1]=p[1:nx-1,1:ny-1,m-1]+dt*Dz*((p[2:nx,1:ny-1,m-1]-2*p[1:nx-1,1:ny-1,m-1]+p[0:nx-2,1:ny-1,m-1])/np.power(dx,2)+(p[1:nx-1,2:ny,m-1]-2*p[1:nx-1,1:ny-1,m-1]+p[1:nx-1,0:ny-2,m-1])/np.power(dy,2));
  
  else:
    p[:,:,0] = p[:,:,1]
    p[1:nx-1,1:ny-1,1]=p[1:nx-1,1:ny-1,0]+dt*Dz*((p[2:nx,1:ny-1,0]-2*p[1:nx-1,1:ny-1,0]+p[0:nx-2,1:ny-1,0])/np.power(dx,2)+(p[1:nx-1,2:ny,0]-2*p[1:nx-1,1:ny-1,0]+p[1:nx-1,0:ny-2,0])/np.power(dy,2));

  if m % 100 == 0:
    #Finally we plot several iterations
    fig = figure()
    for g in range(18):
      subplot(3,6,1)
    axis([0,nx,0,ny])
    pcolor(p[:,:,1],vmin=-0.001,vmax=0.001,cmap='jet')
    axis('off')
    savefig("./img/step"+str(m)+".png",bbox_inches="tight",pad_inches=0)