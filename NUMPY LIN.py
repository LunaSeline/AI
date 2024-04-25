import numpy as np
# NumPy
"""
WHAT IS NUMPY
-->NumPy is a Python library used for working with arrays.
-->It also has functions for working in domain of linear algebra, fourier transform, and matrices.
-->NumPy stands for Numerical Python.
"""

"""
WHY USE NUMPY?
-->In Python we have lists that serve the purpose of arrays, but they are slow to process.
-->NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
-->The array object in NumPy is called ndarray.
-->It provides a lot of supporting functions that make working with ndarray very easy.
"""

"""
WHY IS NUMPY FASTER THAN LISTS
-->NumPy arrays are stored at one continuous place in memory unlike lists.
-->Processes can access and manipulate them very efficiently.
-->This behavior is called locality of reference in computer science.
-->This is the main reason why NumPy is faster than lists. 
-->It is optimized to work with latest CPU architectures.
"""

print(np.__version__)

# NumPy ndarray object by using the array() function.
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# USING TUPLE TO CREATE NUMPY ARRAY
Arr = np.array((2, 3, 4, 5))
print(Arr)

# DIMENSIONS IN ARRAY: one level of array depth (nested arrays).
# NESTED ARRAY: are arrays that have arrays as their elements.

# 0-D ARRAYS
"""
-->0-D arrays, or Scalars, are the elements in an array. 
-->Each value in an array is a 0-D array.
"""
a = np.array(35)
print(a)

# 1-D ARRAY: An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

b = np.array([1, 2, 3, 4])
print(b)

# 2-D ARRAY:
"""
-->An array that has 1-D arrays as its elements is called a 2-D array.
-->These are often used to represent matrix or 2nd order tensors.
"""
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(c)

# 3-D ARRAY
""" 
-->An array that has 2-D arrays (matrices) as its elements is called 3-D array.
-->These are often used to represent a 3rd order tensor.
"""
A = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("\n")
print(A)

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(A.ndim)
