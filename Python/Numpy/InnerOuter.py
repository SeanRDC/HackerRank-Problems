import numpy 

A = numpy.array([0, 1])
B = numpy.array([3, 4])
print(numpy.inner(A, B)) # Inner
print(numpy.outer(A, B)) # Outer

a = numpy.array(input().split(), dtype=int)
b = numpy.array(input().split(), dtype=int)

print(numpy.inner(a,b))
print(numpy.outer(a,b))