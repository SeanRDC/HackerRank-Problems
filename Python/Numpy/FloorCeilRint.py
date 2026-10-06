# Reads a 1-D float array and prints its floor, ceil, and rint (round to nearest
# integer) versions.

import numpy
numpy.set_printoptions(legacy='1.13')

A = numpy.array(*[input().split() for _ in range(1)], dtype=float)
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))