# Records the 1-based positions of every word in group A with a defaultdict(list), then
# prints the positions for each word in group B or -1 if it never appeared.

from collections import defaultdict

n, m = map(int, input().split())

group_a = defaultdict(list)

for i in range(n):
    word = input()
    group_a[word].append(i + 1)

for j in range(m):
    word = input()
    if word in group_a:
        print(*group_a[word])
    else:
        print('-1')