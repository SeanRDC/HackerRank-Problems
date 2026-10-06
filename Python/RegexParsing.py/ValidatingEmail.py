# Parses each 'name <email>' line with email.utils and prints it back only when the
# address matches the required username, domain, and extension pattern.

import re
import email.utils

pattern = r"^[a-zA-Z][a-zA-Z0-9\-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"

for i in range(int(input())):
    n = input()
    name, email_n = email.utils.parseaddr(n)

    match = re.search(pattern, email_n)

    if match:
        print(email.utils.formataddr((name, email_n)))
