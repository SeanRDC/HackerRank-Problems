# Sums the N x M array along axis 0, then prints the product of those column sums.

import numpy
import math

N, M = map(int, input().split())
m = numpy.array([input().split() for _ in range(N)], int)

print(math.prod(numpy.sum(m, axis = 0)))