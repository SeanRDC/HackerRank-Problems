# Converts the integer to a binary string, splits it on '0', and prints the length of
# the longest remaining run of consecutive 1s.

n = int(input().strip())
binary_str = bin(n)[2:]
print(len(max(binary_str.split('0'))))
