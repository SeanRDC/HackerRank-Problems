# Reads x and k, evaluates the polynomial expression typed on the next line with eval,
# and prints whether it equals k.

x, k = map(int, input().split())
poly_str = input()
p = eval(poly_str)
print(p == k)