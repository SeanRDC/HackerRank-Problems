# Reads two N x N integer matrices and prints their matrix product.

import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], dtype=int)
b = numpy.array([input().split() for _ in range(n)], dtype=int)

print(numpy.matmul(a, b))