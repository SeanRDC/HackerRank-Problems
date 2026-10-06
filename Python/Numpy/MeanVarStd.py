# Reads an N x M array and prints the mean along axis 1, the variance along axis 0, and
# the standard deviation of the whole array.

import numpy

N, M = map(int, input().split())

my_arr = numpy.array([input().split() for _ in range(N)], int)

print(numpy.mean(my_arr, axis=1))
print(numpy.var(my_arr, axis=0))
std = numpy.std(my_arr, axis=None)

print(round(std, 11))