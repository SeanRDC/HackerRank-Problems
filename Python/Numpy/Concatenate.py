# Reads an N x P array and an M x P array and joins them along axis 0 with
# numpy.concatenate.

import numpy
n, m, p = map(int, input().split())

N1 = numpy.array([input().split() for _ in range(n)], int)
M1 = numpy.array([input().split() for _ in range(m)], int)

concat = numpy.concatenate((N1, M1))
print(concat)