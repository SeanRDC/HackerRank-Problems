# Reads nine space-separated integers and reshapes them into a 3 x 3 array.

import numpy

N = numpy.array([input().split()], int)
print(numpy.reshape(N,(3,3)))
