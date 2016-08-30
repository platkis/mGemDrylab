# Must have Pillow installed

from images2gif import writeGif
import numpy as np
from numpy.random import *
from matplotlib.pyplot import *
from PIL import Image,ImageSequence
import sys,os,csv

#run_number = 0
#passive_signal_production = 0.5
#active_signal_production = 5.0
#factor_production = 0.1
#Dz=0.02;
#Rz=0.001;
#signal_thresh = 10.0
#factor_thresh = 10.0

run_number = float(sys.argv[1])
passive_signal_production = float(sys.argv[2])
active_signal_production = float(sys.argv[3])
factor_production = float(sys.argv[4])
Dz=float(sys.argv[5])
Rz=float(sys.argv[6])
signal_thresh = float(sys.argv[7])
factor_thresh = float(sys.argv[8])
Dz_factor = float(sys.argv[9])
Rz_factor = float(sys.argv[10])


directory = "./img/agent"+str(run_number)
if not os.path.exists(directory):
  os.makedirs(directory)
filename = "./img/agent"+str(run_number)+"/agent"+str(run_number)+".gif"

with open("./img/agent"+str(run_number)+"/agent"+str(run_number)+".csv","wb") as paramsFile:
  paramsWriter = csv.writer(paramsFile,delimiter=",")
  paramsWriter.writerow([sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10]])

dt=0.002;
dx=1;
dy=1;
#Those parameters fix the number of points in the grid. For isntance, the total x length of the plate will be dx*nx
size = 120;
nx=size;
ny=size;
nt=50000;
#We precharge the p matrix which will have inside the numerical solutions.
signals = np.zeros([nx,ny,2]);
factors = np.zeros([nx,ny,2]);

#Here we set the boundary conditions for t (can be call initial conditions). It is going to be 20 hot or cold points in random positions.
#for f in range(20):
#  signals[round((nx-1)*rand()),round((ny-1)*rand()),1]=np.sign(rand()-0.51);

positions = []
with open("./map.csv","rb") as mapfile:
  mapreader = csv.reader(mapfile,delimiter=",")
  for row in mapreader:
    positions.append(row)

frame_names = []
for m in range(1,nt):
#A simple implementation (but not quite eficient) will be iterating each point at a time. Because we have a matrix, we can operate with whole sections of the matrix at each time.
#Basically, we take time slices and operate them as a whole. To use centered differences, we simply shift the matrix one element in the x direction or in the y direction.
  signals[:,:,0] = signals[:,:,1]
  signals[1:nx-1,1:ny-1,1]=signals[1:nx-1,1:ny-1,0]-dt*Rz*signals[1:nx-1,1:ny-1,0]+dt*Dz*((signals[2:nx,1:ny-1,0]-2*signals[1:nx-1,1:ny-1,0]+signals[0:nx-2,1:ny-1,0])/np.power(dx,2)+(signals[1:nx-1,2:ny,0]-2*signals[1:nx-1,1:ny-1,0]+signals[1:nx-1,0:ny-2,0])/np.power(dy,2));
  for row in range(len(positions)):
    for col in range(len(positions[row])):
      if positions[row][col]=="b":
        signals[col,row,1] += passive_signal_production
      elif positions[row][col] == "ba":
        signals[col,row,1] += active_signal_production
      if positions[row][col] == "b" and signals[col,row,1] >= signal_thresh:
        positions[row][col] = "ba"
      elif positions[row][col] == "ba" and signals[col,row,1] < factor_thresh:
        positions[row][col] = "b" 

  factors[:,:,0] = factors[:,:,1]
  factors[1:nx-1,1:ny-1,1]=factors[1:nx-1,1:ny-1,0]-dt*Rz_factor*factors[1:nx-1,1:ny-1,0]+dt*Dz_factor*((factors[2:nx,1:ny-1,0]-2*factors[1:nx-1,1:ny-1,0]+factors[0:nx-2,1:ny-1,0])/np.power(dx,2)+(factors[1:nx-1,2:ny,0]-2*factors[1:nx-1,1:ny-1,0]+factors[1:nx-1,0:ny-2,0])/np.power(dy,2));
  for row in range(len(positions)):
    for col in range(len(positions[row])):
      if positions[row][col] == "ba":
        factors[col,row,1] += factor_production
        
  #if m % 100 == 0:
  #  print(factors[50,50,1])
  if m % 100 == 0:
    print(m)
    #Finally we plot several iterations
    fig = figure()
    for g in range(18):
      subplot(3,6,1)
    axis([0,nx,0,ny])
    pcolor(factors[:,:,1],vmin=-0.001,vmax=0.001,cmap='jet')
    axis('off')
    savefig("./img/agent"+str(run_number)+"/step"+str(m)+".png",bbox_inches="tight",pad_inches=0)
    frame_names.append("./img/agent"+str(run_number)+"/step"+str(m)+".png")
    close()

frame_images = []
for i in frame_names:
  frame_images.append(Image.open(i))

writeGif(filename,frame_images,duration=0.02,repeat=True)
os.remove("./img/agent"+str(num_number)+"/*png")