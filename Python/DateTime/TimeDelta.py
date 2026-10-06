# Parses both timestamps, including their UTC offsets, with strptime and prints the
# absolute difference between them in whole seconds.

from datetime import datetime

def get_time_adiff(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    n1 = datetime.strptime(t1, format)
    n2 = datetime.strptime(t2, format)
    return int(abs(n1 - n2).total_seconds())

T = int(input())
for _ in range(T):
    string_1 = input()
    string_2 = input()
    print(get_time_adiff(string_1, string_2))