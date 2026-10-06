# Reads a, b, and m and prints a^b followed by a^b mod m using the three-argument form
# of pow.

a = int(input())
b = int(input())
m = int(input())

print(pow(a, b))
print(pow(a, b, m))