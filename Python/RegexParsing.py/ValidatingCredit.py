import re

for _ in range(int(input())):
    match = re.search(r"^(?!.*(\d)(?:-?\1){3})[456](?:\d{15}|\d{3}-\d{4}-\d{4}-\d{4})$", input())
    print('Valid') if match else print('Invalid')