# -*- coding: utf-8 -*-
"""Numpy_introduce.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ommaJVt4gfJjYGXkNp23bpxREeXefKO2
"""

#Ex1:
import numpy as np
l = list(range(1, 4))
data = np.array(l)
print(data)
print(data[0])
print(data[1])

#Ex2
import numpy as np
l_1D = [1,2,3]
data = np.array(l_1D)
print(data)
print(data.shape)

#Ex3
import numpy as np
l_2D = [[1,2],[3,4],[5,6]]
data = np.array(l_2D)
print(data)
print(data.shape)

#Ex4
import numpy as np
l_3D = [
          [[1,2],[3,4],[5,6]],
          [[2,3],[4,5],[6,7]],
          [[3,4],[5,6],[7,8]]
        ]
data = np.array(l_3D)
print(data)
print(data.shape)

#Ex5
import numpy as np
data1 = np.array([1,2,3])
print(data1.dtype)
data2 = np.array([1.,2.,3.])
print(data2.dtype)
data3 = np.array([1,2,3], dtype = np.int32)
print(data3.dtype)

# Update an Element
import numpy as np
l = list(range(1, 4))
data = np.array(l)
print(data)
data[0] = 8
print(data)

# Zeros array
import numpy as np

arr = np.zeros((2,3))
print(arr)

# Ones array
import numpy as np

arr = np.ones((2,3))
print(arr)

# Full array
import numpy as np

arr = np.full((2,3), 8)
print(arr)

# Arange function
import numpy as np
arr1 = np.arange(5)
print(arr1)
arr2 = np.arange(0, 5, 2)
print(arr2)

# eye() function
import numpy as np
arr = np.eye(3)
print(arr)

# Random() function
import numpy as np
arr = np.random.random((2,3))
print(arr)

#Where() function
import numpy as np
arr = np.arange(5)
print(arr)
dk =  arr < 3
out = np.where(dk, arr, arr*2)
print(dk)
print(out)

#Flatten() function
import numpy as np
arr = np.array([[1,2],[3,4]])
out = arr.flatten()
print(arr)
print(out)

#Reshape() function
import numpy as np
l = [[1,2,3],
     [4,5,6]]

data = np.array(l)
print('data\n', data)
print('data shape\n', data.shape)

data_rs = np.reshape(data, (3,2))
print('data_rs\n', data_rs)
print('data_rs shape\n', data_rs.shape)