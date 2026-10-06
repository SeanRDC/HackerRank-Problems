# Prints the number of students subscribed only to the first newspaper using the
# difference of the two sets.

N = int(input())
n = set(map(int, input().split()))
B = int(input())
b = set(map(int, input().split()))

print(len(n - b))