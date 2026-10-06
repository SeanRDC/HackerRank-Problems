# Reads two lists of integers and prints their cartesian product as space-separated
# tuples.

from itertools import product

lsit_A = list(map(int, input().split()))

list_B = list(map(int, input().split()))

result = list(product(list_A, list_B))

print(*result)