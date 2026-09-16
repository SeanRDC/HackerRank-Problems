import re

for _ in range(int(input())):
    match = re.search(r"^(?!.*(.).*\1)(?=(?:.*[A-Z]){2})(?=(?:.*\d){3})[a-zA-Z0-9]{10}$", input())
    print('Valid') if match else print('Invalid')