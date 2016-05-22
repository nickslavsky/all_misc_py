from collections import namedtuple
import numpy as np
import time
from matplotlib import pyplot as plt

alpha = 1
beta = 2
gamma = 1
delta = 1.5
initial = [1, 0.05]
t_max = 100
tau = 0.001

def f(result):
    'compute the right part of the ODE - f()'
    return [(alpha - beta * result[1]) * result[0],
            (- gamma + delta * result[0]) * result[1]]

def sum_c_k(y, butcher):
    'returns sum(b_i * k_i)'
    k = np.zeros((butcher[0], 2))
    k[0] = f(y)
    if butcher[0] > 1:
        for i in range(1, butcher[0]):
            t = y + tau * butcher[2][i][:i].dot(k[:i])
            k[i] = f(np.reshape(t, 2))
    c = np.reshape(butcher[3], butcher[0])
    temp = k.T.dot(c)
    return temp

def compute_explicit(butcher):
    'returns results in form of N times t, y1, y2'
    y = np.array(initial)
    t = 0
    N = int(t_max/tau)
    res = np.zeros((N + 1, 3))
    res[0] = [t, y[0], y[1]]
    for i in range(1, N + 1):
        y += tau * sum_c_k(y, butcher)
        t += tau
        res[i] = [t, y[0], y[1]]
    return res

def compute_k_nplus(butcher, k_n, y_n):
    'k_n - Sx2 array of previous k_n'
    epsilon = 1
    temp = k_n
    k_nplus = np.zeros((butcher[0], 2))
    while epsilon > butcher[4]:
        for i in range(butcher[0]):
            t = y_n + tau * butcher[2][i].dot(temp)
            k_nplus[i] = f(np.reshape(t, 2))
        epsilon = max(np.linalg.norm(temp-k_nplus, axis= 1))
        temp = k_nplus
    return k_nplus

def compute_implicit(butcher):
    'returns results in form of N times t, y1, y2'
    y = np.array(initial)
    t = 0
    N = int(t_max / tau)
    res = np.zeros((N + 1, 3))
    res[0] = [t, y[0], y[1]]
    k_n = np.tile(initial, (butcher[0], 1))
    c = np.reshape(butcher[3], butcher[0])
    for i in range(1, N + 1):
        y += tau * k_n.T.dot(c)
        t += tau
        k_n = compute_k_nplus(butcher, k_n, y)
        res[i] = [t, y[0], y[1]]
    return res

def read_butcher(filename):
    with open(filename, 'rb') as fh:
        S = int(fh.readline())
        array = np.fromfile(fh, float, (S+1)**2, '\t')
        rest = fh.read().strip()

    array.shape = (S+1, S+1)
    a = array[:-1,  0]
    b = array[:-1, 1:]
    c = array[ -1, 1:]
    tolerance = float(rest) if rest else 0.0
    return S, a, b, c, tolerance


if __name__ == '__main__':
    #filename = input('Type file name: ')
    butcher = read_butcher(r'methods\implicit-euler.dat')
    start = time.time()
    result = compute_implicit(butcher) if butcher[4] > 0 else compute_explicit(butcher)
    np.savetxt('results.txt', result, fmt = '%.4f', delimiter = '\t', newline = '\r\n')
    print(time.time() - start)
    x = result[:, 1]
    y = result[:, 2]
    plt.plot(x, y)
    plt.show()
