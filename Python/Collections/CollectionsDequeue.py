# Runs N append, appendleft, pop, and popleft commands on a deque and prints what
# remains. The second version dispatches each command with getattr instead of if/elif
# checks.

from collections import deque

de = deque()
N = int(input())
for _ in range(N):
    raw_cmd = input().split()
    if len(raw_cmd) == 2:
        command = raw_cmd[0]
        val = raw_cmd[1]
        if command == 'append':
            de.append(val)
        elif command == 'appendleft':
            de.appendleft(val)
    if len(raw_cmd) == 1:
        commands = raw_cmd[0]
        if commands == 'pop':
            de.pop()
        elif commands == 'popleft':
            de.popleft()
print(*de)

di = deque()
n = int(input())
for _ in range(n):
    cmd = input().split()
    if len(cmd) == 2:
        act = cmd[0]
        num = cmd[1]
        getattr(di, act)(num)
    elif len(cmd) == 1:
        acts = cmd[0]
        getattr(di, acts)()
print(*di)