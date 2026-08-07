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