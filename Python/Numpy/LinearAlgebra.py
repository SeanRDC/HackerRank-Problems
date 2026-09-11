import numpy

# linalg.det
print(numpy.linalg.det([[1 , 2], [2, 1]]))

# linalg.eig
vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
print(vals)
print(vecs)

# linalg.inv
print(numpy.linalg.inv([[1 , 2], [2, 1]]))

N = int(input())
A = numpy.array([input().split() for _ in range(N)], float)

print(round(numpy.linalg.det(A),2))
