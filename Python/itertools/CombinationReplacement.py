# Sorts the string and prints every size-k combination with replacement of its
# characters in lexicographic order.

from itertools import combinations_with_replacement

S, k = input().split()
k = int(k)
for c in combinations_with_replacement(sorted(S), k):
    print(''.join(c))