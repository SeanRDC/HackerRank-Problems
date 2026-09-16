import re

# findall
print(re.findall(r'\w','http://www.hackerrank.com/'))
# result: ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

# finditer
print(re.finditer(r'\w','http://www.hackerrank.com/'))

print(map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/')))
# result: ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

S = "rabcdeefgyYhFjkIoomnpOeorteeeeet"
m = re.findall(r"(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])", S)

if m:
    for i in m:
        print(i)
else:
    print(-1)