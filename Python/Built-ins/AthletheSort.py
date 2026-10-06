# Reads the table of athletes and prints its rows sorted by the k-th attribute, using a
# lambda as the sort key.

arr = [list(map(int, input().split())) for i in range(1, 6)]
k = int(input())
[print(*j) for j in sorted(arr, key=lambda row: row[k])]
