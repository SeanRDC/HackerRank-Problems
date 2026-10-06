# A postal code is valid when it lies between 100000 and 999999 and contains fewer than
# two alternating repetitive digit pairs, which are found with a lookahead.

regex_integer_in_range = r"^[1-9]\d{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)