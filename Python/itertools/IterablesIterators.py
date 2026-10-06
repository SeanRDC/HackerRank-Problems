# Generates every K-sized combination of the letters and prints the fraction of them
# that contain 'a', to four decimal places.

from itertools import combinations

_ = input()
letters = input().split()
K = int(input())
combos = list(combinations(letters, K))
result = sum('a' in c for c in combos) / len(combos)
print(f"{result:.4f}")