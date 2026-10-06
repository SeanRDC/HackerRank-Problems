# Reads an N x N float matrix and prints its determinant rounded to two decimal places.

import numpy

N = int(input())
A = numpy.array([input().split() for _ in range(N)], float)

print(round(numpy.linalg.det(A),2))
