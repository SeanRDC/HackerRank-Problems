# Finds every 3 or 6 digit hex color code in each CSS line, using a lookbehind so that
# selectors starting the line are not matched.

import re

pattern = r"(?<!^)(#(?:[\da-fA-F]{3}){1,2})\b"

N = int(input())

for i in range(N):
    text = input()
    match = re.findall(pattern, text)
    for j in match:
        print(j)