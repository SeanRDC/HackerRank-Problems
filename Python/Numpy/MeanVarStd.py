import numpy

# Mean
my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.mean(my_array, axis = 0)) 
print(numpy.mean(my_array, axis = 1)) 
print(numpy.mean(my_array, axis = None))
print(numpy.mean(my_array))

# Var
my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.var(my_array, axis = 0))  
print(numpy.var(my_array, axis = 1))        
print(numpy.var(my_array, axis = None))      
print(numpy.var(my_array))         

# Std
my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.std(my_array, axis = 0))
print(numpy.std(my_array, axis = 1))
print(numpy.std(my_array, axis = None))
print(numpy.std(my_array))

N, M = map(int, input().split())

my_arr = numpy.array([input().split() for _ in range(N)], int)

print(numpy.mean(my_arr, axis=1))
print(numpy.var(my_arr, axis=0))
std = numpy.std(my_arr, axis=None)

print(round(std, 11))