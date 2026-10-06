# Uses a backreference to find the first alphanumeric character that repeats
# consecutively and prints it, or -1 when there is none.

import re

S = input()

n = re.search(r"([a-zA-Z0-9])\1", S)
if n:
    print(n.group(1))
else:
    print(-1)