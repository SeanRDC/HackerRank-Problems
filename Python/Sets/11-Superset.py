# Checks set A against each of the N other sets and prints True only if A is a strict
# superset of every one of them.

A = set(input().split())

N = int(input())

is_strict = True

for _ in range(N):

    B = set(input().split())

    if not (A > B):

        is_strict = False

        break

print(is_strict)