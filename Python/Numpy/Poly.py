import numpy

# Poly 
print(numpy.poly([-1, 1, 1, 10]))

# Roots
print(numpy.roots([1, 0, -1]))

# Polyint
print(numpy.polyint([1, 1, 1]))

# Polyder
print(numpy.polyder([1, 1, 1, 1]))

# Polyval
print(numpy.polyval([1, -2, 0, 2], 4))

# Polyfit
print(numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2))

p = list(map(float, input().split()))
x = int(input())

print(numpy.polyval(p, x))
