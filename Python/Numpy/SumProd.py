import numpy
import math

my_array = numpy.array([ [1, 2], [3, 4] ])
print(numpy.sum(my_array, axis = 0))         #Output : [4 6]
print(numpy.sum(my_array, axis = 1))         #Output : [3 7]
print(numpy.sum(my_array, axis = None))      #Output : 10
print(numpy.sum(my_array))                   #Output : 10

print(numpy.prod(my_array, axis = 0))            #Output : [3 8]
print(numpy.prod(my_array, axis = 1))            #Output : [ 2 12]
print(numpy.prod(my_array, axis = None))         #Output : 24
print(numpy.prod(my_array))                      #Output : 24

N, M = map(int, input().split())
m = numpy.array([input().split() for _ in range(N)], int)

print(math.prod(numpy.sum(m, axis = 0)))