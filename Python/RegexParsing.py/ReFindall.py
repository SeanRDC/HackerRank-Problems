# Finds every run of two or more vowels that sits between two consonants using
# lookbehind and lookahead, printing each match or -1 if there are none.

import re

S = "rabcdeefgyYhFjkIoomnpOeorteeeeet"
m = re.findall(r"(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])", S)

if m:
    for i in m:
        print(i)
else:
    print(-1)