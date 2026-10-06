# Reads the array dimensions and prints an integer array of zeros and then one of ones
# with that shape.

import numpy

shape_dims = tuple(map(int, input().split()))

print(numpy.zeros(shape_dims, dtype=int))
print(numpy.ones(shape_dims, dtype=int))