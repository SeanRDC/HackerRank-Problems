# The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
from collections import defaultdict

d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")

for i in d.items():
    print (i)
    
from collections import defaultdict

# =====================================================================
# LEVEL 1: THE BASICS (Built-in Types)
# =====================================================================

# PROBLEM 1: The Counter
# Concept: Passing `int` to defaultdict means any missing key gets a default of 0.
# Task: Count how many times each fruit appears in the list.
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# --- TEACHING ---
# Without defaultdict, you'd need if/else checks. 
# With defaultdict(int), if 'apple' is missing, it runs int() which returns 0.
fruit_counts = defaultdict(int)

for fruit in fruits:
    fruit_counts[fruit] += 1  

print("Problem 1:", dict(fruit_counts)) 
# Output: {'apple': 3, 'banana': 2, 'orange': 1}


# PROBLEM 2: The Grouper
# Concept: Passing `list` gives missing keys a default of an empty list [].
# Task: Group the following words by their starting letter.
words = ['ant', 'bear', 'bat', 'cat', 'crab', 'ape']

# --- TEACHING ---
# We want to append to a list for each letter. 
word_groups = defaultdict(list)

for word in words:
    first_letter = word[0]
    word_groups[first_letter].append(word) # No need to check if the list exists!

print("Problem 2:", dict(word_groups))
# Output: {'a': ['ant', 'ape'], 'b': ['bear', 'bat'], 'c': ['cat', 'crab']}


# PROBLEM 3: The Unique Grouper
# Concept: Passing `set` gives missing keys an empty set(), automatically removing duplicates.
# Task: Track the UNIQUE tags used by each user.
user_tags = [
    ('alice', 'python'), ('bob', 'java'), 
    ('alice', 'python'), ('alice', 'c++')
]

# --- TEACHING ---
# If we used a list, 'alice' would have 'python' twice. A set fixes this.
unique_tags = defaultdict(set)

for user, tag in user_tags:
    unique_tags[user].add(tag) # sets use .add() instead of .append()

print("Problem 3:", dict(unique_tags))
# Output: {'alice': {'c++', 'python'}, 'bob': {'java'}}


# =====================================================================
# LEVEL 2: CUSTOM DEFAULTS WITH LAMBDA
# =====================================================================
# What if you don't want 0, [], or set()? What if you want a specific string or a complex object? 
# You can use a lambda (an anonymous, inline function) to define exactly what is returned.

# PROBLEM 4: Custom String Defaults
# Concept: Using `lambda: "Unknown"` for missing data.
# Task: You have a dictionary of employee IDs to names. If an ID is missing, return "Guest".

employee_names = defaultdict(lambda: "Guest")
employee_names[101] = "Sarah"
employee_names[102] = "John"

# --- TEACHING ---
# We ask for a key that exists, and a key that doesn't.
print("Problem 4 (Exists):", employee_names[101]) # Sarah
print("Problem 4 (Missing):", employee_names[999]) # Guest


# PROBLEM 5: Complex Default Values
# Concept: Defaulting to a dictionary with pre-filled keys.
# Task: Track wins and losses for players in a game. If a player is new, 
# their stats should start as {'wins': 0, 'losses': 0}.
match_results = [('Alice', 'win'), ('Bob', 'loss'), ('Alice', 'win')]

# --- TEACHING ---
# The lambda returns a fresh dictionary every time a new key is found.
player_stats = defaultdict(lambda: {'wins': 0, 'losses': 0})

for player, result in match_results:
    if result == 'win':
        player_stats[player]['wins'] += 1
    else:
        player_stats[player]['losses'] += 1

print("Problem 5:", dict(player_stats))
# Output: {'Alice': {'wins': 2, 'losses': 0}, 'Bob': {'wins': 0, 'losses': 1}}


# =====================================================================
# LEVEL 3: PRACTICAL ALGORITHMS
# =====================================================================

# PROBLEM 6: Graph Adjacency List
# Concept: Using `defaultdict(list)` is the standard way to map out connections (graphs).
# Task: Given a list of connected cities (edges), build a graph showing all 
# destinations you can reach from a given city.
edges = [("NY", "LA"), ("NY", "Chicago"), ("LA", "SF"), ("Chicago", "Denver")]

graph = defaultdict(list)

# --- TEACHING ---
# A graph is just a dictionary where keys are nodes, and values are lists of connected nodes.
for start, end in edges:
    graph[start].append(end)

print("Problem 6:", dict(graph))
# Output: {'NY': ['LA', 'Chicago'], 'LA': ['SF'], 'Chicago': ['Denver']}


# PROBLEM 7: Grouping Anagrams
# Concept: Using a tuple as a key in a defaultdict(list)
# Task: Group words that are anagrams of each other.
word_list = ["eat", "tea", "tan", "ate", "nat", "bat"]

# --- TEACHING ---
# Dictionaries can't use lists as keys, but they CAN use tuples.
# If we sort the letters of an anagram, they will always match (e.g., 'eat' -> 'aet').
anagrams = defaultdict(list)

for w in word_list:
    sorted_letters = tuple(sorted(w)) 
    anagrams[sorted_letters].append(w)

# We just print the values (the grouped lists)
print("Problem 7:", list(anagrams.values()))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


# =====================================================================
# LEVEL 4: NESTED DEFAULTDICTS (Mind-Benders)
# =====================================================================

# PROBLEM 8: The 2D Grid / Matrix
# Concept: A defaultdict whose default value is... another defaultdict!
# Task: Track the number of times a coordinate (x, y) is clicked on a screen.
clicks = [(0, 0), (5, 5), (0, 0), (1, 2)]

# --- TEACHING ---
# We want to access grid[x][y]. 
# So the outer dict needs a default of `defaultdict(int)` to handle the `y` layer.
grid = defaultdict(lambda: defaultdict(int))

for x, y in clicks:
    grid[x][y] += 1

print("Problem 8 (Click at 0,0):", grid[0][0]) # Output: 2
print("Problem 8 (Click at 9,9):", grid[9][9]) # Output: 0 (Automatically handled!)


# PROBLEM 9: Aggregating Multi-Level Data
# Concept: Grouping by Date, then by Category, and summing the amounts.
# Task: Summarize sales data.
sales_data = [
    ("2023-10-01", "Food", 15.50),
    ("2023-10-01", "Books", 20.00),
    ("2023-10-01", "Food", 5.00),
    ("2023-10-02", "Books", 10.00)
]

# --- TEACHING ---
# Outer key: Date. Inner key: Category. Inner value: float (running total).
daily_sales = defaultdict(lambda: defaultdict(float))

for date, category, amount in sales_data:
    daily_sales[date][category] += amount

# Just showing how cleanly nested data gets built:
print("Problem 9:", {k: dict(v) for k, v in daily_sales.items()})
# Output: {'2023-10-01': {'Food': 20.5, 'Books': 20.0}, '2023-10-02': {'Books': 10.0}}


# =====================================================================
# LEVEL 5: MASTERY
# =====================================================================

# PROBLEM 10: The "Autovivification" Tree (Infinite Nesting)
# Concept: A defaultdict that returns a copy of itself.
# Task: Create a deeply nested JSON-like structure without ever having to 
# initialize any intermediate dictionaries. 

# --- TEACHING ---
# We define a function `tree` that returns a defaultdict which calls `tree`.
# This means if a key is missing, it generates a new dict, which can generate a new dict...
def tree():
    return defaultdict(tree)

my_tree = tree()

# Watch this magic. None of these keys exist yet!
my_tree['animal']['mammal']['canine']['dog'] = "Golden Retriever"
my_tree['animal']['reptile']['snake'] = "Python"

# To print it cleanly, we convert it back to a normal dict using a quick helper:
import json
def dicts(t): 
    return {k: dicts(t[k]) if isinstance(t[k], defaultdict) else t[k] for k in t}

print("Problem 10:\n", json.dumps(dicts(my_tree), indent=2))
# Output:
# {
#   "animal": {
#     "mammal": {
#       "canine": {
#         "dog": "Golden Retriever"
#       }
#     },
#     "reptile": {
#       "snake": "Python"
#     }
#   }
# }