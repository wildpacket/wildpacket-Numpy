number-array.py

import numpy as np
a = np.arange (1,10).reshape (3,3)
b = np.arange (1,10).reshape (3,3)
c = np.vstack((a,b))
print(c)
sum = np.sum(c)
print(sum)
d = np.dot(a,b)
print(d)