import time
import numpy as np


start_time = time.time()
N = 450000000 # Edit this to change number of random points
np.random.seed()
x,y = np.random.random((2,N,2))
diffs = x-y
out = round(np.mean(np.sqrt(np.einsum('ij,ij->i',diffs,diffs))),6)
print(out)
print(time.time()-start_time)
