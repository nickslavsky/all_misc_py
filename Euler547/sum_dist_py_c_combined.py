from ctypes import *
lib = cdll.LoadLibrary('Euler.dll')
avg_dist = lib.averageDistanceLamina
avg_dist.restype = c_double
avg_dist.argtypes = [c_long, c_int, c_int, c_int, c_int, c_int]

if __name__ == '__main__':
    f = avg_dist(1000000000, 3, 1, 1, 1, 1)
    print(round(f,4))
