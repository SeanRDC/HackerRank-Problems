# Prints the number of students subscribed to at least one newspaper using the union of
# the two sets.

N = int(input())
n = set(map(int, input().split()))
B = int(input())
b = set(map(int, input().split()))

print(len(n | b))