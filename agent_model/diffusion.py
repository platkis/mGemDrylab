from graphics import *
import random
import math
import numpy as np
win = GraphWin()
win.autoflush = False

# refresh graphics every x iterations
refreshTime = 1

map_size_i = 20
map_size_j = 20

ai_diffusion_constant = 0.02
ai_decay_rate = 0.001
chem_diffusion_constant = 0.05
chem_decay_rate = 0.0001

step = 0
positions = []
for i in range(20):
  positions.append([])
  for j in range(20):
    positions[i].append(" ")

    
aiMap = []
for i in range(20):
  aiMap.append([])
  for j in range(20):
    aiMap[i].append(1)


#for i in range(len(positions)):
#  for j in range(len(positions[i])):
#    if random.randint(0,45) == 30:
#      positions[i][j] = "b"
       
chemMap = []
for i in range(20):
  chemMap.append([])
  for j in range(20):
    chemMap[i].append(0.001)

graphicsMap = []
for i in range(20):
  graphicsMap.append([])
  for j in range(20):
    graphicsMap[i].append(Rectangle(Point(j*10,i*10,),Point(j*10+10,i*10+10)))

# Derivative matrices for diffusion
ai_div = []
for i in range(20):
  ai_div.append([])
  for j in range(20):
    ai_div[i].append([0.0,0.0])
ai_divsq = []
for i in range(20):
  ai_divsq.append([])
  for j in range(20):
    ai_divsq[i].append([0.0,0.0])
    
chem_div = []
for i in range(20):
  chem_div.append([])
  for j in range(20):
    chem_div[i].append([0.0,0.0])
chem_divsq = []
for i in range(20):
  chem_divsq.append([])
  for j in range(20):
    chem_divsq[i].append([0.0,0.0])    
    
positions[10][10] = "b"
#positions[6][10] = "b"
#positions[10][12] = "b"
#positions[8][12] = "b"
#positions[10][8] = "b"
#positions[6][12] = "b"
#positions[10][3] = "b"
#positions[8][10] = "b"
#positions[12][12] = "b"
#positions[8][8] = "b"
#positions[12][8] = "b"
#positions[12][10] = "b"
#positions[6][8] = "b"

while step < 100:
  print(step)
  step += 1

  for i in range(len(positions)):
    for j in range(len(positions[i])):
  #    if i == 10 and j == 10:
  #      print chemMap[i][j]
      ###################################
      # Start diffusion
      ###################################
    
      # Find laplace operator
      
      # For autoinducer
      # First derivative
      if i != 0 and i != map_size_i-1 and j != 0 and j != map_size_j-1:
        neighbours_x = [aiMap[i][j-1],aiMap[i][j],aiMap[i][j+1]]
        neighbours_y = [aiMap[i-1][j],aiMap[i][j],aiMap[i+1][j]]
        neighbours_index = [1.0,2.0,3.0]
        m_x,b_x = np.polyfit(neighbours_index,neighbours_x,1)
        m_y,b_y = np.polyfit(neighbours_index,neighbours_y,1)
        ai_div[i][j] = [m_x,m_y]
        

      #Second derivative
      if i > 1 and i < map_size_i - 2 and j > 1 and j < map_size_j - 2:
        neighbours_x = [ai_div[i][j-1][0],ai_div[i][j][0],ai_div[i][j+1][0]]
        neighbours_y = [ai_div[i-1][j][1],ai_div[i][j][1],ai_div[i+1][j][1]]
        neighbours_index = [1.0,2.0,3.0]
        m_x,b_x = np.polyfit(neighbours_index,neighbours_x,1)
        m_y,b_y = np.polyfit(neighbours_index,neighbours_y,1)
        ai_divsq[i][j] = m_x+m_y
        
      # For chem
      # First derivative
      if i != 0 and i != map_size_i-1 and j != 0 and j != map_size_j-1:
        neighbours_x = [chemMap[i][j-1],chemMap[i][j],chemMap[i][j+1]]
        neighbours_y = [chemMap[i-1][j],chemMap[i][j],chemMap[i+1][j]]
        neighbours_index = [1.0,2.0,3.0]
        m_x,b_x = np.polyfit(neighbours_index,neighbours_x,1)
        m_y,b_y = np.polyfit(neighbours_index,neighbours_y,1)
        chem_div[i][j] = [m_x,m_y]
        

      #Second derivative
      if i > 1 and i < map_size_i - 2 and j > 1 and j < map_size_j - 2:
        neighbours_x = [chem_div[i][j-1][0],chem_div[i][j][0],chem_div[i][j+1][0]]
        neighbours_y = [chem_div[i-1][j][1],chem_div[i][j][1],chem_div[i+1][j][1]]
        neighbours_index = [1.0,2.0,3.0]
        m_x,b_x = np.polyfit(neighbours_index,neighbours_x,1)
        m_y,b_y = np.polyfit(neighbours_index,neighbours_y,1)
        chem_divsq[i][j] = m_x+m_y
        if i == 10 and j == 9:
          print neighbours_x
          print chem_divsq[i][j]
      # Compute diffusion
      if i > 1 and i < map_size_i - 2 and j > 1 and j < map_size_j - 2:
        # for autoinducer
        if i == 10 and j == 9:
          print chem_divsq[i][j]
        aiMap[i][j] = ai_diffusion_constant*ai_divsq[i][j]*aiMap[i][j] - ai_decay_rate*aiMap[i][j]
        chemMap[i][j] = chem_diffusion_constant*chem_divsq[i][j]*chemMap[i][j] - chem_decay_rate*chemMap[i][j]
        
      ###################################
      # Beginning of cell behaviour
      ###################################
      if positions[i][j] == "b":
        
        # Behaviour of cell here
        chemMap[i][j] += 10
        chemMap[i-1][j] += 10
        chemMap[i+1][j] += 10
        chemMap[i][j-1] += 10
        chemMap[i][j+1] += 10

        ################################
        #Everything here down is fine
        ################################  
        
        maxChem = 0  
        for k in range(len(chemMap)):
          for l in range(len(chemMap[i])):
            if chemMap[k][l] > maxChem:
              maxChem = chemMap[k][k]
        
  if step%refreshTime==0:
    for i in range(len(chemMap)):
      for j in range(len(chemMap[i])):
        if chemMap[i][j] > maxChem*5/6:
          graphicsMap[i][j].setFill('red')
        elif chemMap[i][j] > maxChem*4/6:
          graphicsMap[i][j].setFill('orange')
        elif chemMap[i][j] > maxChem*3/6:
          graphicsMap[i][j].setFill('yellow')
        elif chemMap[i][j] > maxChem*2/6:
          graphicsMap[i][j].setFill('green')
        elif chemMap[i][j] > maxChem*1/6:
          graphicsMap[i][j].setFill('blue')
        elif chemMap[i][j] > 0:
          graphicsMap[i][j].setFill('purple')
        else:
          graphicsMap[i][j].setFill('white')
      
  if step%refreshTime==0:
   
    for i in range(len(graphicsMap)):
      for j in range(len(graphicsMap[i])):
        if step > 0:
          graphicsMap[i][j].undraw()
        graphicsMap[i][j].draw(win)
      
  win.flush()
  update() 
  for i in chemMap:
    print(i)
for i in chemMap:
  print(i)


maxChem = 0  
for i in range(len(chemMap)):
  for j in range(len(chemMap[i])):
    if chemMap[i][j] > maxChem:
      maxChem = chemMap[i][j]
for i in range(len(chemMap)):
  for j in range(len(chemMap[i])):
    
    rect = Rectangle(Point(j*10,i*10,),Point(j*10+10,i*10+10))
    if chemMap[i][j] > maxChem*5/6:
      rect.setFill('red')
    elif chemMap[i][j] > maxChem*4/6:
      rect.setFill('orange')
    elif chemMap[i][j] > maxChem*3/6:
      rect.setFill('yellow')
    elif chemMap[i][j] > maxChem*2/6:
      rect.setFill('green')
    elif chemMap[i][j] > maxChem*1/6:
      rect.setFill('blue')
    elif chemMap[i][j] > 0:
      rect.setFill('purple')
    rect.draw(win)
    
    if positions[i][j] == "b":
      cir = Circle(Point(j*10+5,i*10+5),3)
      cir.draw(win)

win.getMouse()
win.close()
    