# For each test case, reads sets A and B and prints whether A is a subset of B.

T = int(input())

for i in range(T):

    _ = input()

    A = set(input().split())

    _ = input()

    B = set(input().split())

    print(A.issubset(B))