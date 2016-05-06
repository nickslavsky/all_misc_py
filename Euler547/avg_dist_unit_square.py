import time
import math
import random

def is_within_exclusion(x, y, offsetX, offsetY, leftX = 1, leftY = 1):
  if x>leftX and x<leftX+offsetX and y>leftY and y<leftY+offsetY:
    return True
  else:
    return False

start_time = time.time()
random.seed()
N = 1000000000 #number of iterations
dim = 4      #square side length

def avg_dist_lamina(leftX, leftY, offsetX, offsetY):
  dist_count = 0 
  dist_sum = 0
  prevX = 0
  prevY = 0
  while prevX==0:
    x1, y1 = dim * random.random(), dim * random.random()
    #print(x1, '\t', y1)
    if(not is_within_exclusion(x1, y1, offsetX, offsetY, leftX, leftY)):
      prevX=x1
      prevY=y1

  while dist_count < N:
    x1, y1 = dim * random.random(), dim * random.random()
    if(not is_within_exclusion(x1, y1, offsetX, offsetY, leftX, leftY)):
      dist_sum += math.sqrt( (x1-prevX)*(x1-prevX) + (y1-prevY)*(y1-prevY) )
      prevX=x1
      prevY=y1
      dist_count += 1
      
  return dist_sum / (dist_count-1)

dist_average = 4*avg_dist_lamina(1, 1, 1, 1) + 4*avg_dist_lamina(1, 1, 2, 1) + avg_dist_lamina(1, 1, 2, 2)

print(round(dist_average, 4))

print(time.time()-start_time)
