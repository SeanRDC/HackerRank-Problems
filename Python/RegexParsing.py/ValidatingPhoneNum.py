# Prints YES for each number that is exactly ten digits long and starts with 7, 8, or 9,
# and NO otherwise.

import re

pattern = r"^[789]\d{9}$"

N = int(input())
for i in range(N):
    M = input()
    match = re.search(pattern, M)

    if match:
        print("YES")
    else:
        print("NO")