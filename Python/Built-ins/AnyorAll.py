# Prints True only when all of the integers are positive and at least one of them is a
# palindrome.

_ = int(input())
arr = input().split()
print(all(int(i) > 0 for i in arr) and any(j == j[::-1] for j in arr))