# Splits the input on commas and dots that are followed by a digit and prints each piece
# on its own line.

regex_pattern = r"[,.]+(?=\d)"

import re
print("\n".join(re.split(regex_pattern, input())))