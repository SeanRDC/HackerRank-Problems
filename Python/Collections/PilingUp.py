# For each test case, repeatedly takes the larger block from either end of the deque. It
# prints 'No' as soon as a block is bigger than the one below it, otherwise 'Yes'.

from collections import deque

T = int(input())
for _ in range(T):

    n = int(input())
    blocks = deque(map(int, input().strip().split()))
    top_of_pile = float('inf')
    while blocks:
        if blocks[0] >= blocks[-1]:
            popped = blocks.popleft()
        elif blocks[-1] > blocks[0]:
            popped = blocks.pop()

        if popped <= top_of_pile:
            top_of_pile = popped
        else:
            print('No')
            break 
    else:
        print('Yes')        