# Group
import re
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print(m.group(0))       # The entire group
print(m.group(1))       # The first parenthesized subgroup.
print(m.group(2))       # The second parenthesized subgroup.
print(m.group(3))       # The third parenthesized subgroup.
print(m.group(1,2,3))   # Multiple arguments give us a tuple.

# Groups
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print(m.groups())

# Groupdict
m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
print(m.groupdict())

S = input()

n = re.search(r"([a-zA-Z0-9])\1", S)
if n:
    print(n.group(1))
else:
    print(-1)