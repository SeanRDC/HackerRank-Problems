# Counts each word's occurrences in an OrderedDict, then prints the number of distinct
# words followed by their counts in order of first appearance.

from collections import OrderedDict
counter = OrderedDict()

N = int(input())

for _ in range(N):
    word = input().strip()
    if word not in counter:
        counter[word] = 1
    else:
        counter[word] += 1
print((len(counter.keys())))

for values in counter.values():
    print(values, end=" ")