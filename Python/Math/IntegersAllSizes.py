# Reads four integers and prints a^b + c^d, relying on Python's arbitrary-precision
# integers to hold the result.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(pow(a, b) + pow(c, d))