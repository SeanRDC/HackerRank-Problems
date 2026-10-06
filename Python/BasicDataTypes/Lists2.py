# Parses each command into a method name and integer arguments, then calls that list
# method dynamically with getattr, printing the list on 'print'.

N = int(input())
ans = []

for i in range(N):
    command = input().lower()
    split_values = command.split()
    cmd = split_values[0]
    args = list(map(int, split_values[1:]))

    if cmd == 'print':
        print(ans)
    else:
        getattr(ans, cmd)(*args)
