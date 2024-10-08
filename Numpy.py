# -*- coding: utf-8 -*-
"""Numpy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pZORhdFEo9ArTGKW_YVRm7jupd1DH8tU
"""

# list
print([1,2,3])
# one dimentional array
# array([1,2,3])

#list of lists
print([[1,2,3],[4,5,6]])
# two diemntional array
# array([[1,2,3],[4,5,6]])

# To install Numpy
# pip install numpy

import numpy as np

# 1_D array
a = np.array([1,2,3])
print(a)

# 2_D array
a = np.array([[1,2,3],[4,5,6]])
print(a)

# Creating an array filled with zeros
a = np.zeros(5)
print(a)

# Creating an array filled with ones
a = np.ones(5)
print(a)

# Creating an array of random values (shown as 2x3 matrix)
a = np.random.random((2,3))
print(a)

# Creating an array filled with given value (dimensions, value)
a = np.full(3,10)
print(a)
a = np.full((2,3),10)
print(a)

# Creating an empty array (fills with arbitrary, un-initialized values)
a = np.empty(2)
print(a)
a = np.empty((2,3))
print(a)

# Creating an array of evenly spaced values (start, stop, step)
# no include stop value
a = np.arange(1,10,1)
print(a)

# Creating an array of evenly spaced values (low, high, num-values)
# include stop value
a = np.linspace(1,10,10)
print(a)

# Creating an array of random integers (low, high, size)
a = np.random.randint(1,10,10)
print(a)

my_1d_array = np.arange(0,20,1)
print(my_1d_array)

print("Max" , my_1d_array.max())

print("Min", my_1d_array.min())

print("Mean", my_1d_array.mean())

print("Sum", my_1d_array.sum())

print("Std", my_1d_array.std())

a = my_1d_array + 10
print(a)

a = my_1d_array - 10
print(a)

a = my_1d_array * 10
print(a)

a = my_1d_array / 10
print(a)

a = np.square(my_1d_array)
print(a)

a = np.sqrt(my_1d_array)
print(a)

a = np.sin(my_1d_array)
print(a)

a = np.cos(my_1d_array)
print(a)

a = np.tan(my_1d_array)
print(a)

a = np.sign(my_1d_array)
print(a)

a = my_1d_array[0]
print(a)

a = my_1d_array[0:6]  # not include the last one
print(a)

a = my_1d_array[-1]
print(a)

a = my_1d_array.reshape(1,my_1d_array.size)
print(a)

a = my_1d_array.reshape(my_1d_array.size,1)
print(a)

my_2d_array = np.random.randint(1,10,(2,3))

print(my_2d_array)

print("Max" , my_2d_array.max())

print("Max in column" , my_2d_array.max(axis = 0))

print("Max in row" , my_2d_array.max(axis = 1))

print("Sum of coulmn" , my_2d_array.sum(axis = 0))

print("Sum of rows" , my_2d_array.sum(axis = 1))

print("Min", my_2d_array.min())

print("Mean", my_2d_array.mean())

print("Sum", my_2d_array.sum())

print("Std", my_2d_array.std())

a = my_2d_array[0]
print(a)

a = my_2d_array[0][1]
print(a)

# Re-shape (here to 3 rows & 2 columns)
a = my_2d_array.reshape(3,2)
print(my_2d_array)
print(a)

# Re-shape (here to a 1-Dimensional array)
a = my_2d_array.flatten()
print(a)

a = my_2d_array.reshape(6)
print(a)

a = my_2d_array.ravel()
print(a)

# Array Shape (length of each dimension)
a = my_2d_array.shape
print(a)

# Number of dimensions
a = my_2d_array.ndim
print(a)

# Number of elements
a = my_2d_array.size
print(a)

a = my_2d_array.dtype
print(a)

b = np.array([1,2,3])
c = np.array([4,2,6])
print("b", b)
print("c", c)

a = np.add(b,c)
print(a)

a = np.subtract(b,c)
print(a)

a = np.multiply(b,c)
print(a)

a = np.divide(b,c)
print(a)

a = np.dot(b,c)
print(a)

a = (b == c)
print(a)

a = np.array_equal(a,b)
print(a)

# Horizontal Stack
# hstack concatenates arrays along axis 1
a = np.hstack((b,c))
print(a)
print()
a = np.concatenate((b,c))
print(a)

# Vertical Stack
# vstack concatenates arrays along axis 0
a = np.vstack((b,c))
print(a)
print()

x = np.array([[1,2],[3,4]])
y = np.array([[5,6]])
a = np.concatenate((x,y), axis = 0)
a1 = np.vstack((x,y))
print(a)
print(a1)

p = np.pi
print(p)

a = np.array([1,2,3], dtype = np.float32)
print(a)

#Return a 2-D array with ones on the diagonal and zero elsewhere
a = np.eye(3) # with 3 column
print(a)

a = np.arange(12).reshape(2,2,3)
print(a)

# Arrays can be transposed using the .T attribute
a = my_1d_array.T
a1 = my_1d_array.transpose()
print(a)
print(a1)

#Numpy also provides a set of element-wise functions that can be applied to all elements of an array, creating a new array
a = np.array([[1,2,3],[4,5,6]])
a1 = np.exp(a)
print(a1)
a2 = np.log(a)
print(a2)

# execution time
s = 0
N = 10000000
x = np.arange(N)
for i in x:
  s += i

# execution time
N = 10000000
x = np.arange(N)
s = x.sum()

x = np.arange(15).reshape(3,5)
print(x)

print()
a = x[1, 0:3]
print(a)

print()
a = x[0:2, 0:2]
print(a)

print()
idx = np.array([0, 0, 2])
#means "select the rows of x indexed by idx and all columns (: means all columns)."
a = x[idx, :]
print(a)

print()
#means "select all rows (:) and the columns of x indexed by idx."
a = x[ :,idx]
print(a)

print()
idx = np.array([0,2]) # rows
jdx = np.array([1,3]) # columns
a = x[idx, :][:,jdx]
print(a)

print()
#_ix allows you to create a 2D array by selecting all combinations of rows in idx and columns in jdx
a = x[np.ix_(idx, jdx)] # generates two 2D arrays that can be used to index the original array x:
print(a)

print()
xMask = x > 5
print(xMask)

print()
a = x[xMask]
print(a)

print()
z = np.array([1,0,1], dtype= np.bool_)
print(z)
a = x[z] # z = [True, False, True] -> x[z] = first row and second row
print(a)

x = np.zeros(6)
print(x)
x[::2] = 3
print(x)

x[np.array([True, False, True, True, True, False],dtype=np.bool_)] = np.arange(4)
# [0,2,3,4] = [1,2,3,4]
print(x)

# copy of the data
x = np.arange(6)
a = x.flags.owndata
print(a)

# view of the data
a = x[:3]
print(a.flags.owndata)

#Array m is broadcasted to a shape (1, 4), and then replicated along axis 0
x = np.zeros((3,4))
print(x)
print()

m = np.arange(4)
print(m)
print()

a = x + m
print(a)

# Array m already has the same number of dimensions as x, and gets replicated along axis 0
x = np.zeros((3,4))
print(x)
print()

m = np.arange(4).reshape((1,4))
print(m)
print()

a = x + m
print(a)

#Array m already has the same number of dimensions as x, and gets replicated along axis 1
x = np.zeros((3,4))
print(x)
print()

m = np.arange(3).reshape((3,1))
print(m)
print()

a = x + m
print(a)

# linear algebra functions
# compute the eigenvalue decomposition of a 2-D array
x = np.arange(9).reshape(3,3)
a = np.linalg.eig(x)
print(a)

x = np.array([99,1,109,-1])
print(x)
print()

a = np.argsort(x) # index of the sorted array
print(a)
print()

a = np.sort(x)
print(a)
print()

x = np.array([99,2,109,-1])
print(x[x>100])
print(x[(x>100) | (x < 0)])
print(x[(x % 2) == 0 ])

x = np.array([99,2,109,-1])
print(x)
a = np.flip(x)
print(a)

x = np.array([[1,2,3],[4,5,6]])
print(x)
print()

a = np.flip(x)
print(a)
print()

a1 = np.flip(x, axis=0) #column
print(a1)
print()

a2 = np.flip(x, axis=1) #row
print(a2)
print()

#save array in a file
#np.save('filename' , array)

#load file
#np.load('filename.py')

