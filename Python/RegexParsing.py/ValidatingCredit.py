# Validates each card number with one regex: it must start with 4, 5, or 6, have 16
# digits optionally grouped in fours by hyphens, and never repeat a digit four times in
# a row.

import re

for _ in range(int(input())):
    match = re.search(r"^(?!.*(\d)(?:-?\1){3})[456](?:\d{15}|\d{3}-\d{4}-\d{4}-\d{4})$", input())
    print('Valid') if match else print('Invalid')