# Sorts the string and prints all of its combinations from size 1 up to size k in
# lexicographic order.

from itertools import combinations
S, k = input().split()
k = int(k)

sorted_S = sorted(S)
for i in range(1, k + 1):
    for j in list(combinations(sorted_S, i)):
        print(''.join(j))