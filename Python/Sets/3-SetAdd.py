# Adds every country name to a set so duplicates collapse, then prints how many distinct
# countries there are.

n = int(input())

empty_set = set()

for i in range(n):
    N = input().lower()
    empty_set.add(N)
print(len(empty_set))