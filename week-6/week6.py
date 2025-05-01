# ## What is NumPy?

# - NumPy is a Python library used for working with arrays.
# - It has functions for working in domain of linear algebra, fourier transform, and matrices.
# - NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.

# ## Why Use NumPy?

# - In Python we have lists that serve the purpose of arrays, but they are slow to process.
# - NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
# - The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

# ## Import NumPy
# Once NumPy is installed, import it in your applications by adding the import keyword:

import numpy as np

# ## NumPy as np
# - NumPy is usually imported under the np alias.
# - Create an alias with the as keyword while importing:

import numpy as np

# ## Checking NumPy Version
# The version string is stored under __version__ attribute.

import numpy as np

print(np.__version__)

# ## Create a NumPy ndarray Object
# - NumPy is used to work with arrays.
# - The array object in NumPy is called ndarray.
# - We can create a NumPy ndarray object by using the array() function.

import numpy as np

arr_ = np.array([101, 201, 301, 401, 501])

print(arr_)

print(type(arr_))

# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:

import numpy as np

name_list = ['Angel', "Shemi", "Marvel", "Linda"]

age_tuple = (41, 32, 21, 19)

grade_dict = {"CSC102": 89, "MTH 102": 77, "CHM 102": 69, "GST 102": 99}

arr_nameList = np.array(name_list)

arr_ageTuple = np.array(age_tuple)

arr_gradeDict = np.array(grade_dict)

print(arr_nameList)
print(arr_ageTuple)
print(arr_gradeDict)

# ## Dimensions in Array
# A dimension in arrays is one level of array depth (nested arrays).

# ### 0-Dimension
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

import numpy as np

class_num = int(input("How many students are in the CSC 102 class?"))

class_arr = np.array(class_num)

if (class_arr == 1):
    print("There is only ", class_arr, "student in CSC 102 class" )
else:
    print("There are", class_arr, "students in CSC 102 class" )

# ### 1-D Arrays
# - An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
# - These are the most common and basic arrays.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

# ### 2-D Arrays
# - An array that has 1-D arrays as its elements is called a 2-D array.
# - These are often used to represent matrix or 2nd order tensors.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr_)

# ### 3-D arrays
# - An array that has 2-D arrays (matrices) as its elements is called 3-D array.
# - These are often used to represent a 3rd order tensor.

import numpy as np

arr = np.arrayarr = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]]
])

print(arr)

# ## Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have

import numpy as np

a = np.array(42)
b = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]]
]) 
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([1, 2, 3, 4, 5])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# ## Higher Dimensional Arrays
# - An array can have any number of dimensions.
# - When the array is created, you can define the number of dimensions by using the ndmin argument.
# - In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a ...
