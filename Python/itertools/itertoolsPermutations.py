# Sorts the string and prints every size-k permutation of its characters in
# lexicographic order.

from itertools import permutations

S, k = input().split()
k = int(k)

perms = permutations(sorted(S), k)
for i in perms:
    print(''.join(i))