import re
import email.utils

pattern = r"^[a-zA-Z][a-zA-Z0-9\-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"

for i in range(int(input())):
    n = input()
    name, email_n = email.utils.parseaddr(n)
    
    match = re.search(pattern, email_n)
    
    if match:
        print(email.utils.formataddr((name, email_n)))
