import numpy as np


N = 10 # Edit this to change number of random points
np.random.seed()
x, y = 2 * np.random.random((2,N,2))


diffs = x-y
out = round(np.mean(np.sqrt(np.einsum('ij,ij->i',diffs,diffs))),4)
print(out)