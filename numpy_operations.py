# -*- coding: utf-8 -*-
"""Numpy_Operations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17ZXdTBymHWyk5tzSdQvndVeTlq_NA7fL
"""

# Phep cong
import numpy as np
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
print('data x \n', x)
print('data y \n', y)

print('Cach 1 \n', x+y)
print('Cach 2 \n', np.add(x,y))

# Phep tru
import numpy as np
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
print('data x \n', x)
print('data y \n', y)

print('Cach 1 \n', y - x)
print('Cach 2 \n', np.subtract(y, x))

# Phep nhan
import numpy as np
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
print('data x \n', x)
print('data y \n', y)

print('Cach 1 \n', x*y)
print('Cach 2 \n', np.multiply(x, y))

# Phep chia
import numpy as np
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
print('data x \n', x)
print('data y \n', y)

print('Cach 1 \n', y/x)
print('Cach 2 \n', y//x)
print('Cach 3 \n', np.divide(y, x))

# Can bac 2
import numpy as np
x = np.array([1,2,3,4])
print('data x \n', x)

print('sqrt \n', np.sqrt(x))

# Inner - Dot
import numpy as np
v = np.array([1,2])
w = np.array([3,4])

print('Cach 1 \n', v.dot(w))
print('Cach 2 \n', np.dot(v, w))