import numpy
numpy.set_printoptions(legacy='1.13')

# Floor
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.floor(my_array)) #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

# Ceil
print(numpy.ceil(my_array))  #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]

# Rint
print(numpy.rint(my_array))  #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]

A = numpy.array(*[input().split() for _ in range(1)], dtype=float)
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))