import re

T = int(input())

for _ in range(T):
    s = input()

    pattern = r"^[+-]?\d*\.\d+$"
    print(bool(re.match(pattern, s)))