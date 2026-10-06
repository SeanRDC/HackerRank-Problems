# Checks each test string against a regex requiring an optional sign, optional leading
# digits, one dot, and at least one digit after it.

import re

T = int(input())

for _ in range(T):
    s = input()

    pattern = r"^[+-]?\d*\.\d+$"
    print(bool(re.match(pattern, s)))