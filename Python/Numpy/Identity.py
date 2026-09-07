import numpy
numpy.set_printoptions(legacy='1.13')

# Identity
print(numpy.identity(3)) #3 is for  dimension 3 X 3

# Eye
print(numpy.eye(8, 7, k = 1))    # 8 X 7 Dimensional array with first upper diagonal 1.

# N rows, M columns

N, M = map(int, input().split())
print(numpy.eye(N, M, k = 0))
