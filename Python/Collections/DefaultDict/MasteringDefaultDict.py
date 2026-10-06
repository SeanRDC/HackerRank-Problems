# Stores the 1-based positions of n words in a defaultdict(list), then checks m words
# against it and prints their positions or -1.

from collections import defaultdict

n, m = map(int, input('[n]Number of words to be entered, [m]Number of times to be checked: ').split())

def_dict = defaultdict(list)

for i in range(n):
    word = input(f'{n} Words to put in the dictionary {i+1}: ')
    def_dict[word].append(i + 1)
for j in range(m):
    word = input(f'{m} Check the words {def_dict[word]} if in the dictionary {j+1}: ')
    if word in def_dict:
        print(*def_dict[word])
    else:
        print('-1')