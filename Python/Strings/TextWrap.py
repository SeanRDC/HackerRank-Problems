# wrap breaks the string into lines of at most max_width characters using textwrap.fill.

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))