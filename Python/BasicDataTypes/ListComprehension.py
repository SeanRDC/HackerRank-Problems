# Builds every [i, j, k] coordinate within the x, y, z bounds whose sum is not n, first
# with a list comprehension and then with equivalent nested loops.

x = int(input())
y = int(input())
z = int(input())
n = int(input())

coords = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i + j + k) !=n]
print(coords)

coords2 = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            total = i + j + k
            if total != n:
                coords2.append([i, j, k])
print(coords2)