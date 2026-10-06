# Prints a growing number of '.|.' patterns centered with dashes for the top half,
# 'WELCOME' in the middle, and then the same rows in reverse for the bottom half.

N, M = map(int, input().split())
pattern = ".|."
word = "WELCOME"

for i in range(1, N, 2):
    print((pattern * i).center(M, '-'))

print(word.center(M, '-'))

for j in range(N - 2, 0, -2):
    print((pattern * j).center(M, '-'))