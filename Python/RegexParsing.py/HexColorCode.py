import re

pattern = r"(?<!^)(#(?:[\da-fA-F]{3}){1,2})\b"

N = int(input())

for i in range(N):
    text = input()
    match = re.findall(pattern, text)
    for j in match:
        print(j)