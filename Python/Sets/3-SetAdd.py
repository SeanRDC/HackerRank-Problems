n = int(input())

empty_set = set()

for i in range(n):
    N = input().lower()
    empty_set.add(N)
print(len(empty_set))