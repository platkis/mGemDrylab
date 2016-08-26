from graphics import *
import random
import math
win = GraphWin()
win.autoflush = False

# refresh graphics every x iterations
refreshTime = 1

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
    chemMap[i].append(0)

graphicsMap = []
for i in range(20):
  graphicsMap.append([])
  for j in range(20):
    graphicsMap[i].append(Rectangle(Point(j*10,i*10,),Point(j*10+10,i*10+10)))
    
positions[10][10] = "b"
positions[6][10] = "b"
positions[10][12] = "b"
positions[8][12] = "b"
positions[10][8] = "b"
positions[6][12] = "b"
positions[10][3] = "b"
positions[8][10] = "b"
positions[12][12] = "b"
positions[8][8] = "b"
positions[12][8] = "b"
positions[12][10] = "b"
positions[6][8] = "b"

while step < 100:
  print(step)
  step += 1
  
  for i in range(len(chemMap)):
    for j in range(len(chemMap[i])):
      if chemMap[i][j] > 0:
        chemMap[i][j] -= 1
      if aiMap[i][j] > 0.2:
        aiMap[i][j] -= 0.2
  
  for i in range(len(positions)):
    for j in range(len(positions[i])):

      if positions[i][j] == "b":
        
        # Behaviour of cell here
 
        autoinducers = 0.1 + aiMap[i][j]
        
        # Barbaric inverse square for autoinducer diffusion
        try:
          print(str(i)+","+str(j))
          aiMap[i-1][j-1] += 16 * autoinducers / 16
          aiMap[i-1][j] += 16 * autoinducers / 16
          aiMap[i-1][j+1] += 16 * autoinducers / 16
          aiMap[i][j-1] += 16 * autoinducers / 16
          aiMap[i][j+1] += 16 * autoinducers / 16
          aiMap[i+1][j-1] += 16 * autoinducers / 16
          aiMap[i+1][j] += 16 * autoinducers / 16
          aiMap[i+1][j+1] += 16 * autoinducers / 16
            
          aiMap[i-2][j-2] += 4 * autoinducers / 16
          aiMap[i-2][j-1] += 4 * autoinducers / 16
          aiMap[i-2][j] += 4 * autoinducers / 16
          aiMap[i-2][j+1] += 4 * autoinducers / 16
          aiMap[i-2][j+2] += 4 * autoinducers / 16
          aiMap[i-1][j-2] += 4 * autoinducers / 16
          aiMap[i][j-2] += 4 * autoinducers / 16
          aiMap[i+1][j-2] += 4 * autoinducers / 16
          aiMap[i+2][j-2] += 4 * autoinducers / 16
          aiMap[i-1][j+2] += 4 * autoinducers / 16
          aiMap[i][j+2] += 4 * autoinducers / 16
          aiMap[i+1][j+2] += 4 * autoinducers / 16
          aiMap[i+2][j+2] += 4 * autoinducers / 16
          aiMap[i+2][j-1] += 4 * autoinducers / 16
          aiMap[i+2][j] += 4 * autoinducers / 16
          aiMap[i+2][j+1] += 4 * autoinducers / 16
          
          aiMap[i-3][j-3] += 1.7777778 * autoinducers / 16
          aiMap[i-3][j-2] += 1.7777778 * autoinducers / 16
          aiMap[i-3][j-1] += 1.7777778 * autoinducers / 16
          aiMap[i-3][j] += 1.7777778 * autoinducers / 16
          aiMap[i-3][j+1] += 1.7777778 * autoinducers / 16
          aiMap[i-3][j+2] += 1.7777778 * autoinducers / 16
          aiMap[i-3][j+3] += 1.7777778 * autoinducers / 16
          aiMap[i-2][j-3] += 1.7777778 * autoinducers / 16
          aiMap[i-1][j-3] += 1.7777778 * autoinducers / 16
          aiMap[i][j-3] += 1.7777778 * autoinducers / 16
          aiMap[i+1][j-3] += 1.7777778 * autoinducers / 16
          aiMap[i+2][j-3] += 1.7777778 * autoinducers / 16
          aiMap[i+3][j-3] += 1.7777778 * autoinducers / 16
          aiMap[i-2][j+3] += 1.7777778 * autoinducers / 16
          aiMap[i-1][j+3] += 1.7777778 * autoinducers / 16
          aiMap[i][j+3] += 1.7777778 * autoinducers / 16
          aiMap[i+1][j+3] += 1.7777778 * autoinducers / 16
          aiMap[i+2][j+3] += 1.7777778 * autoinducers / 16
          aiMap[i+3][j+3] += 1.7777778 * autoinducers / 16
          aiMap[i+3][j+2] += 1.7777778 * autoinducers / 16
          aiMap[i+3][j+1] += 1.7777778 * autoinducers / 16
          aiMap[i+3][j] += 1.7777778 * autoinducers / 16
          aiMap[i+3][j-1] += 1.7777778 * autoinducers / 16
          aiMap[i+3][j-2] += 1.7777778 * autoinducers / 16

        except:
          print(str(i)+","+str(j)+"!")
            
        # If enough autoinducers, raise chemical concentration    
        if autoinducers >= 5:
          try:
            chemMap[i-1][j-1] += 15
            chemMap[i-1][j] += 15
            chemMap[i-1][j+1] += 15
            chemMap[i][j-1] += 15
            chemMap[i][j] += 15
            chemMap[i][j+1] += 15
            chemMap[i+1][j-1] += 15
            chemMap[i+1][j] += 15
            chemMap[i+1][j+1] += 15
          except:
            border = True
          # chem here
       
        
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
    