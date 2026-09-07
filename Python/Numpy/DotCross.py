import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print(numpy.dot(A, B)) # Dot
# print(numpy.cross(A, B)) # Cross

n = int(input())
a = numpy.array([input().split() for _ in range(n)], dtype=int)
b = numpy.array([input().split() for _ in range(n)], dtype=int)

print(numpy.matmul(a, b))