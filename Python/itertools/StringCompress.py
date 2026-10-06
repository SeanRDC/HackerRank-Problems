# Groups consecutive identical characters with groupby and prints a (count, digit) tuple
# for each group.

from itertools import groupby

S = input()

compressed = []
for i, group in groupby(S):
    count = len(list(group))
    number = int(i)
    compressed.append((count, number))

print(*compressed)