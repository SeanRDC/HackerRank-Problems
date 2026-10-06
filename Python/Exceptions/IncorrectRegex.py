# Tries to compile each input string with re.compile and prints True if it is a valid
# regex, or False when re.error is raised.

import re

def is_valid_re(user_ipt):
    try:
        re.compile(user_ipt)
        return True
    except re.error:
        return False

T = int(input())
for _ in range(T):
    print(is_valid_re(input()))