M = int(input())
m = set(map(int, input().split()))
N = int(input())
n = set(map(int, input().split()))

a = list(n.difference(m))
b = list(m.difference(n))
new_list = sorted(a+b)

print(*new_list, sep="\n")
