# Reads two integer arrays and prints their inner product followed by their outer
# product.

import numpy 

a = numpy.array(input().split(), dtype=int)
b = numpy.array(input().split(), dtype=int)

print(numpy.inner(a,b))
print(numpy.outer(a,b))