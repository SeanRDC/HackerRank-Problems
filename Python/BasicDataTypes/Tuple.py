# Reads n space-separated integers, packs them into a tuple, and prints the tuple's
# hash.

n = int(input())
m = input()
t = tuple(map(int, m.split()))
print(hash(t))