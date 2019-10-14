import numpy as np

a = np.random.randint(0,9,size=(3,3))
gx = np.array([
    [-1,0,1],
    [-2,0,2],
    [-1,0,1]
])
gy = gx.transpose()
gx = gx*a
gy = gy*a
gx = np.sum(gx)
gy = np.sum(gy)
print(a)
print(gx)
print(gy)

def GSqrt(x, y):
    g = np.sqrt(x**2+y**2)
    print("\nGSqrt:\n", g)

def GAbs(x, y):
    g = abs(x) + abs(y)
    print("\nGAbs:\n", g)

def GP(a):
    p = a.reshape(-1)
    p = np.concatenate(([0], p), axis=0)
    g1 = abs((p[1] + 2 * p[2] + p[3]) - (p[7] + 2 * p[8] + p[9]))
    g2 = abs((p[3] + 2 * p[6] + p[9]) - (p[1] + 2 * p[4] + p[7]))
    g = g1 + g2
    print("\nGP:\n", g)




GSqrt(gx, gy)
GAbs(gx, gy)
GP(a)
