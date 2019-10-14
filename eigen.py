import numpy as np
from numpy import linalg as LA

# w, v = LA.eig(np.diag((1, 2, 3)))

a = np.array([
    [7, 3],
    [3, -1]
])
w, v = LA.eig(a)

print(w)
print(v)


