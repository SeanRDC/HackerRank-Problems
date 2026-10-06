# Sorts the string with a custom key that orders lowercase letters first, then uppercase
# letters, then odd digits, then even digits.

s = input()
def get_prio(s):
    if s.isupper():
        return(1, s)
    elif s.islower():
        return(0, s)
    elif s.isdigit() and int(s) % 2 == 1:
        return(2, s)
    elif s.isdigit() and int(s) % 2 == 0:
        return(3, s)

print(''.join(sorted(s, key=get_prio)))