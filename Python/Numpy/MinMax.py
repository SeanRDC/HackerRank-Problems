# Takes the minimum along axis 1 of the N x M array, then prints the maximum of those
# row minimums.

import numpy

N, M = map(int, input().split())

my_array = numpy.array([input().split() for _ in range(N)], int)
minimum = numpy.min(my_array, axis=1)
maximum = numpy.max(minimum)
print(maximum)