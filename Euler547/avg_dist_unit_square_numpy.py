import time
import numpy as np
from joblib import Parallel, delayed  
import multiprocessing


N     = 1000 # number of numpy iterations
chunk = 25000000 #amount of points in one numpy iteration
dist_sum = 0 
dist_count = 0

def calc_avg_dist(size, n, leftX, leftY, offsetX, offsetY):
    x,y = n*np.random.random((2,size,2))
    rightX = leftX+offsetX
    upperY = leftY+offsetY
    x = x[
        np.logical_not(np.logical_and(
        np.logical_and(x[:,0] > leftX, x[:,0] < rightX),
        np.logical_and(x[:,1] > leftY, x[:,1] < upperY)
        ))
    ]
    y = y[
        np.logical_not(np.logical_and(
        np.logical_and(y[:,0] > leftX, y[:,0] < rightX),
        np.logical_and(y[:,1] > leftY, y[:,1] < upperY)
        ))
    ]
    n = min(x.shape[0], y.shape[0])
    diffs = x[:n,:] - y[:n,:]
    return np.sum(np.sqrt(np.einsum('ij,ij->i',diffs,diffs)))/n

def avg_square_lamina(N, size, n, num_cores, leftX, leftY, offsetX, offsetY):
    
    results = Parallel(n_jobs=num_cores)(delayed(calc_avg_dist)(chunk, n, leftX, leftY, offsetX,
                                                                offsetY) for i in range(N))
    return np.mean(results)

if __name__=='__main__':
    num_cores = multiprocessing.cpu_count()
    np.random.seed()
    start_time = time.time()
    results = 4*avg_square_lamina(N, chunk, 4, num_cores, 1, 1, 1,
                                  1) + 4*avg_square_lamina(N, chunk, 4, num_cores, 1, 1, 2,
                                                           1) + avg_square_lamina(N, chunk,
                                                                                  4, num_cores,
                                                                                  1, 1, 2, 2)
    out = round(results, 4)
    print(out)
    print(time.time()-start_time)

  

