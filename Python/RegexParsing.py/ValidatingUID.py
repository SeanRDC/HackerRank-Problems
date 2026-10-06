# Validates each UID with lookaheads: 10 alphanumeric characters, no repeats, at least
# two uppercase letters, and at least three digits.

import re

for _ in range(int(input())):
    match = re.search(r"^(?!.*(.).*\1)(?=(?:.*[A-Z]){2})(?=(?:.*\d){3})[a-zA-Z0-9]{10}$", input())
    print('Valid') if match else print('Invalid')