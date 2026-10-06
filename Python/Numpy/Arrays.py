# Converts the input list into a NumPy float array and returns it reversed.

import numpy

def array(arr):
    numpy_arr = numpy.array(arr,float)
    return numpy_arr[::-1]

arr = input().strip().split(' ')
result = array(arr)
print(result)