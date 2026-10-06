# Replaces every '&&' and '||' that has a space on both sides with 'and' and 'or', using
# a replacement function passed to re.sub.

import re

def replace_logic(match):
    symbol = match.group(0)
    if symbol == "&&":
        return "and"
    if symbol == "||":
        return "or"

for _ in range(int(input())):
    n = input()
    print(re.sub(r"(?<= )(&&|\|\|)(?= )", replace_logic ,n))