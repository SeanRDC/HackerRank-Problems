import numpy
# Transpose
my_array = numpy.array([[1,2,3],
                        [4,5,6]])

print(numpy.transpose(my_array))
# Flatten
my_array = numpy.array([[1,2,3],
                        [4,5,6]])

print(my_array.flatten())

N, M = map(int, input().split())
my_array = numpy.array([input().split() for _ in range(N)], int)

print(numpy.transpose(my_array))
print(my_array.flatten())
