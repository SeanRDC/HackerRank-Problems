# Collects the first name of every row whose email matches the regex '@gmail\.com$',
# then prints those names in alphabetical order.

import re

if __name__ == '__main__':
    N = int(input().strip())
    included_names = []

    for N_itr in range(N):

        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        if re.search(r"@gmail\.com$", emailID):
            included_names.append(firstName)

    for names in sorted(included_names):
        print(names)
