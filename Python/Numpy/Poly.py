# Reads the polynomial coefficients and a value x, then prints the polynomial evaluated
# at x with numpy.polyval.

import numpy

p = list(map(float, input().split()))
x = int(input())

print(numpy.polyval(p, x))
