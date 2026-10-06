# Reads a and b and prints the integer quotient, the remainder, and the divmod tuple
# containing both.

a = int(input())
b = int(input())

print(a // b)
print(a % b)
print(divmod(a, b))