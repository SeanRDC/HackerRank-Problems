# Prints the number of students subscribed to exactly one newspaper using the symmetric
# difference of the two sets.

N = int(input())
n = set(map(int, input().split()))
M = int(input())
m = set(map(int, input().split()))

print(len(n.symmetric_difference(m)))