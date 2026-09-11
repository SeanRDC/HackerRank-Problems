# Using shape to get array dimensions

import numpy

my_1D_array = numpy.array([1, 2, 3, 4, 5])
print(my_1D_array.shape)     #(5,) -> 1 row and 5 columns

my_2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print(my_2D_array.shape)     #(3, 2) -> 3 rows and 2 columns 

# Using shape to change array dimension

import numpy

change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print(change_array)

#  Reshape

my_array = numpy.array([1,2,3,4,5,6])
print(numpy.reshape(my_array,(3,2)))

N = numpy.array([input().split()], int)
print(numpy.reshape(N,(3,3)))

