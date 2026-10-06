# Walks through the array adding 1 to happiness for every element in set A and
# subtracting 1 for every element in set B, then prints the total.

_ = input().split()

array = list(input().split())

A = set(input().split())

B = set(input().split())

happiness = 0

for item in array:

    if item in A:
        happiness += 1

    elif item in B:
        happiness -= 1

print(happiness)