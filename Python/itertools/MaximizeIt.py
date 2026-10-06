# Uses itertools.product to try one element from every list, scores each combination as
# the sum of squares modulo M, and prints the highest score.

from itertools import product

K, M = map(int, input().split())

def math_engine(combo, M):
    return sum([x ** 2 for x in combo]) % M

all_list = []
for _ in range(K):
    all_list.append(map(int, input().split()[1:]))

max_score = 0
for i in product(*all_list):
    current_num = math_engine(i, M)
    if current_num > max_score:
        max_score = current_num

print(max_score)