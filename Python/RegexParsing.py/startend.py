# Wraps the substring k in a lookahead so overlapping matches are found, then prints the
# start and end index of each occurrence in S or (-1, -1).

import re

S = input()
k = input()

pattern = re.compile(rf'(?=({re.escape(k)}))')

matches = list(pattern.finditer(S))

if matches:
    for match in matches:
        start_index = match.start()
        end_index = start_index + len(k) - 1
        print(f"({start_index}, {end_index})")
else:
    print("(-1, -1)")
