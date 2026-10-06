# Reads a set of integers and applies each remove, discard, or pop command to it,
# ignoring KeyErrors, then prints the sum of what is left.

n = int(input())

s = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    user_input = input().split()
    cmd = user_input[0]

    if len(user_input) > 1:
        target = int(user_input[1])
    else:
        target = None

    if cmd == 'remove':
        try:
            s.remove(target)
        except KeyError:
            pass

    elif cmd == 'discard':
        s.discard(target)

    elif cmd == 'pop':
        try:
            s.pop()
        except KeyError:
            pass

print(sum(s))
