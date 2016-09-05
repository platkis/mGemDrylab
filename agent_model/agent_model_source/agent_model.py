from images2gif import writeGif
import numpy as np
from numpy.random import *
from matplotlib.pyplot import *
from PIL import Image,ImageSequence
import sys,os,csv

#Default parameters:
#run_number = 0
#passive_signal_production = 0.5
#active_signal_production = 5.0
#factor_production = 0.1
#Dz=0.02;
#Rz=0.001;
#signal_thresh = 10.0
#factor_thresh = 10.0
#Dz_factor = 0.02
#Rz_factor = 0.001

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

# Get directory for images
directory = "./img/agent"+str(run_number)
if not os.path.exists(directory):
  os.makedirs(directory)
filename = "./img/agent"+str(run_number)+"/agent"+str(run_number)+".gif"

# Write parameters for future reference
with open("./img/agent"+str(run_number)+"/agent"+str(run_number)+".csv","wb") as paramsFile:
  paramsWriter = csv.writer(paramsFile,delimiter=",")
  paramsWriter.writerow([sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10]])

# Steps in x and y directions, and time
dt=0.002;
dx=1;
dy=1;

# Open csv as map
positions = []
with open("./map.csv","rb") as mapfile:
  mapreader = csv.reader(mapfile,delimiter=",")
  for row in mapreader:
    positions.append(row)
    
# Size of map
nx=len(positions[0]);
ny=len(positions);
nt=50001;
# Fill signal and factor matrices with zeros
signals = np.zeros([nx,ny,2]);
factors = np.zeros([nx,ny,2]);
compare = np.zeros([nx,ny,2]);

compare[:,:,1] = 0.001

frame_names = []
# Each step
for m in range(1,nt):
  # Diffusion
  signals[:,:,0] = signals[:,:,1]
  signals[1:nx-1,1:ny-1,1]=signals[1:nx-1,1:ny-1,0]-dt*Rz*signals[1:nx-1,1:ny-1,0]+dt*Dz*((signals[2:nx,1:ny-1,0]-2*signals[1:nx-1,1:ny-1,0]+signals[0:nx-2,1:ny-1,0])/np.power(dx,2)+(signals[1:nx-1,2:ny,0]-2*signals[1:nx-1,1:ny-1,0]+signals[1:nx-1,0:ny-2,0])/np.power(dy,2));
  
  # Thresholds and signal production
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

  # Factor production
  factors[:,:,0] = factors[:,:,1]
  factors[1:nx-1,1:ny-1,1]=factors[1:nx-1,1:ny-1,0]-dt*Rz_factor*factors[1:nx-1,1:ny-1,0]+dt*Dz_factor*((factors[2:nx,1:ny-1,0]-2*factors[1:nx-1,1:ny-1,0]+factors[0:nx-2,1:ny-1,0])/np.power(dx,2)+(factors[1:nx-1,2:ny,0]-2*factors[1:nx-1,1:ny-1,0]+factors[1:nx-1,0:ny-2,0])/np.power(dy,2));
  for row in range(len(positions)):
    for col in range(len(positions[row])):
      if positions[row][col] == "ba":
        factors[col,row,1] += factor_production
        
  # Save images for gif on multiples of 500
  if m % 1000 == 0:
    print(m)    
    fig = figure(figsize=(6,2),dpi=120)
    axis([0,ny,0,nx])
    pcolor(factors[:,:,1],vmin=-0.001,vmax=0.001,cmap='jet')
    axis('off')
    savefig("./img/agent"+str(run_number)+"/step"+str(m)+".png",bbox_inches="tight",pad_inches=-0.2)
    frame_names.append("./img/agent"+str(run_number)+"/step"+str(m)+".png")
    close()

frame_images = []
for i in frame_names:
  frame_images.append(Image.open(i))

# Check to see if right side of image has no factor
if np.amax(factors[:,250:,1]) < compare[:,250:,1].all():
  with open("notable_runs.txt","a") as runs_file:
    runs_file.write("\nagent"+str(run_number))
  print("\nagent"+str(run_number)+" is an interesting run!! (^-^)")
  
# Make gif
writeGif(filename,frame_images,duration=0.02,repeat=True)

for i in frame_names:
  os.remove(i)