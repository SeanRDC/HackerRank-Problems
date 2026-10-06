# Reads an N x M integer array and prints its transpose followed by its flattened form.

import numpy

N, M = map(int, input().split())
my_array = numpy.array([input().split() for _ in range(N)], int)

print(numpy.transpose(my_array))
print(my_array.flatten())
