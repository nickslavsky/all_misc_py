import time
import math
import random


start_time = time.time()
random.seed()
dist_count = 10000000
dist_sum = 0
offset = 1

for _ in range(dist_count):
    x1, y1 = 2 * random.random(), 2 * random.random()
    if x1 > 1.0 and y1 > 1.0:
        x1 += offset
        y1 += offset
    x2, y2 = 2 * random.random(), 2 * random.random()
    if x2 > 1.0 and y2 > 1.0:
        x2 += offset
        y2 += offset
    #print(str(x1) + '    ' + str(y1) + '\n' + str(x2) + '    ' + str(y2))
    dist_sum += math.sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) )

dist_average = dist_sum / dist_count
print(round(dist_average, 4))

print(time.time()-start_time)
