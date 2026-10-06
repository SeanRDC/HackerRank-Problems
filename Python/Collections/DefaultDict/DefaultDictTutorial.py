# Ten worked defaultdict examples, from int, list, and set defaults through lambda
# defaults, nested defaultdicts, and a recursive tree printed as JSON.

from collections import defaultdict

d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")

for i in d.items():
    print (i)

from collections import defaultdict

fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

fruit_counts = defaultdict(int)

for fruit in fruits:
    fruit_counts[fruit] += 1  

print("Problem 1:", dict(fruit_counts)) 

words = ['ant', 'bear', 'bat', 'cat', 'crab', 'ape']

word_groups = defaultdict(list)

for word in words:
    first_letter = word[0]
    word_groups[first_letter].append(word)

print("Problem 2:", dict(word_groups))

user_tags = [
    ('alice', 'python'), ('bob', 'java'), 
    ('alice', 'python'), ('alice', 'c++')
]

unique_tags = defaultdict(set)

for user, tag in user_tags:
    unique_tags[user].add(tag)

print("Problem 3:", dict(unique_tags))

employee_names = defaultdict(lambda: "Guest")
employee_names[101] = "Sarah"
employee_names[102] = "John"

print("Problem 4 (Exists):", employee_names[101])
print("Problem 4 (Missing):", employee_names[999])

match_results = [('Alice', 'win'), ('Bob', 'loss'), ('Alice', 'win')]

player_stats = defaultdict(lambda: {'wins': 0, 'losses': 0})

for player, result in match_results:
    if result == 'win':
        player_stats[player]['wins'] += 1
    else:
        player_stats[player]['losses'] += 1

print("Problem 5:", dict(player_stats))

edges = [("NY", "LA"), ("NY", "Chicago"), ("LA", "SF"), ("Chicago", "Denver")]

graph = defaultdict(list)

for start, end in edges:
    graph[start].append(end)

print("Problem 6:", dict(graph))

word_list = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = defaultdict(list)

for w in word_list:
    sorted_letters = tuple(sorted(w)) 
    anagrams[sorted_letters].append(w)

print("Problem 7:", list(anagrams.values()))

clicks = [(0, 0), (5, 5), (0, 0), (1, 2)]

grid = defaultdict(lambda: defaultdict(int))

for x, y in clicks:
    grid[x][y] += 1

print("Problem 8 (Click at 0,0):", grid[0][0])
print("Problem 8 (Click at 9,9):", grid[9][9])

sales_data = [
    ("2023-10-01", "Food", 15.50),
    ("2023-10-01", "Books", 20.00),
    ("2023-10-01", "Food", 5.00),
    ("2023-10-02", "Books", 10.00)
]

daily_sales = defaultdict(lambda: defaultdict(float))

for date, category, amount in sales_data:
    daily_sales[date][category] += amount

print("Problem 9:", {k: dict(v) for k, v in daily_sales.items()})

def tree():
    return defaultdict(tree)

my_tree = tree()

my_tree['animal']['mammal']['canine']['dog'] = "Golden Retriever"
my_tree['animal']['reptile']['snake'] = "Python"

import json
def dicts(t): 
    return {k: dicts(t[k]) if isinstance(t[k], defaultdict) else t[k] for k in t}

print("Problem 10:\n", json.dumps(dicts(my_tree), indent=2))