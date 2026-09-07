import numpy

myarray = numpy.array([[2, 5], [3, 7], [1, 3], [4, 0]])
print(numpy.min(myarray, axis=0))
print(numpy.max(myarray, axis=0))

N, M = map(int, input().split())
    
my_array = numpy.array([input().split() for _ in range(N)], int)
# Compute the min along axis  and then print the max of that result.
minimum = numpy.min(my_array, axis=1)
maximum = numpy.max(minimum)
print(maximum)

    
# Sample input:
# 4 2
# 2 5
# 3 7
# 1 3
# 4 0
# Sample output: 3