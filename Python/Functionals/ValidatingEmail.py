# fun validates an address by splitting it into username, website, and extension and
# checking each part's allowed characters and length. filter keeps the valid emails,
# which are printed sorted.

def fun(s):
    if len(s.split('@')) == 2:
        username = s.split('@')[0]
        clean = username.replace("_","").replace("-","")
        if len(username) == 0:
            return False
        if not clean.isalnum():
            return False

        domain_str = s.split('@')[1]
        if len(domain_str.split('.')) == 2:
            website = domain_str.split('.')[0]
            if len(website) == 0:
                return False
            if not website.isalnum():
                return False

            extension = domain_str.split('.')[1]
            if len(extension) == 0 or len(extension) > 3:
                return False

            if not extension.isalpha():
                return False
            return True
        else:
            return False
    else:
        return False


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)