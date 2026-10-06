# Prints the number of students subscribed to both newspapers using the intersection of
# the two sets.

N = int(input())
n = set(map(int, input().split()))
B = int(input())
b = set(map(int, input().split()))

print(len(n & b))