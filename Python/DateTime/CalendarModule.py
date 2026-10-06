# Reads a date as month, day, and year, builds a datetime from it, and prints the
# weekday name in uppercase.

from datetime import datetime

n = list(map(int, input().split()))
d = n[1]
m = n[0]
y = n[2]
def day_fndr(d, m, y):
    dt_obj = datetime(y, m, d)
    return dt_obj.strftime("%A").upper()
print(day_fndr(d, m, y))