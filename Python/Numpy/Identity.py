# Reads N and M and prints an N x M array with ones on the main diagonal and zeros
# elsewhere using numpy.eye.

import numpy
numpy.set_printoptions(legacy='1.13')

N, M = map(int, input().split())
print(numpy.eye(N, M, k = 0))
