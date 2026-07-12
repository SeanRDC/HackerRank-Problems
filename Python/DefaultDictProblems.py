from collections import defaultdict

# =====================================================================
# LEVEL 1: THE BASICS (Built-in Types)
# =====================================================================

# PROBLEM 1: The Vote Counter
votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Alice', 'Bob']

# ### GUIDANCE ###
# 1. Create a defaultdict. Think about what data type represents a "count". 
#    Pass that type (without parentheses) into defaultdict.
# 2. Write a `for` loop to iterate through the `votes` list.
# 3. For each candidate in the list, increment their value in the dictionary by 1.
# 4. Print your dictionary.
# Expected Output: {'Alice': 3, 'Bob': 2, 'Charlie': 1}

# --- WRITE YOUR CODE HERE ---
voters_list = defaultdict(int)
for voters in votes:
    voters_list[voters] += 1

print("Problem 1: ", dict(voters_list))
    
# PROBLEM 2: The Grade Grouper
grades = [('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A'), ('David', 'C'), ('Eve', 'B')]

# ### GUIDANCE ###
# 1. You want to group names together under a specific grade. What data type 
#    holds a collection of items in order? Pass that to defaultdict.
# 2. Loop through the `grades` list. Since it's a list of tuples, you can 
#    unpack them directly in the loop (e.g., `for student, grade in ...`).
# 3. Use the grade as your key, and add the student to that key's collection.
# Expected Output: {'A': ['Alice', 'Charlie'], 'B': ['Bob', 'Eve'], 'C': ['David']}

# --- WRITE YOUR CODE HERE ---
student_grades = defaultdict(list)

for student, grade in grades:
    student_grades[grade].append(student)

print("Problem 2: ", dict(student_grades))

# PROBLEM 3: Unique Page Visitors
page_visits = [
    ('home', 'user1'), ('about', 'user2'), 
    ('home', 'user1'), ('home', 'user3')
]

# ### GUIDANCE ###
# 1. Notice 'user1' visited 'home' twice. We only want UNIQUE visitors. 
#    What data type automatically removes duplicates? Use that as your factory.
# 2. Loop through `page_visits`. Unpack the page and the user.
# 3. Add the user to the collection for that page. Remember, this specific 
#    data type uses `.add()`, not `.append()`!
# Expected Output: {'home': {'user1', 'user3'}, 'about': {'user2'}}

# --- WRITE YOUR CODE HERE ---
visitors = defaultdict(set)
for page, guests in page_visits:
    visitors[page].add(guests)

print("Problem 3: ", dict(visitors))


# =====================================================================
# LEVEL 2: CUSTOM DEFAULTS WITH LAMBDA
# =====================================================================

# PROBLEM 4: The Missing Translator
dictionary_data = [('hello', 'hola'), ('world', 'mundo')]

# ### GUIDANCE ###
# 1. We want missing words to default to the exact string "NOT FOUND".
#    Built-in types can't do this. You need a lambda function: `lambda: "your string"`.
# 2. Loop through `dictionary_data` and populate your defaultdict so 'hello' 
#    maps to 'hola', etc.
# 3. Try to print the value for the key 'hello'.
# 4. Try to print the value for the key 'apple'.
# Expected Output for 'apple': NOT FOUND

# --- WRITE YOUR CODE HERE ---
data = defaultdict(lambda: "NOT FOUND")

for word, translation in dictionary_data:
    data[word] = translation
    data[translation] = word

print("Problem 4: ", data['hello'], data['world'], data['apple'])

# PROBLEM 5: E-commerce Cart
cart_adds = [
    ('laptop', 1, 1000.0), 
    ('mouse', 2, 25.0), 
    ('laptop', 1, 1000.0)
]

# ### GUIDANCE ###
# 1. We want each item to default to a dictionary containing its stats: 
#    `{'qty': 0, 'cost': 0.0}`. Use a lambda to return this dictionary.
# 2. Loop through `cart_adds`. Unpack the item, quantity, and price.
# 3. For each item, add the quantity to the 'qty' key, and add 
#    (quantity * price) to the 'cost' key.
# Expected Output: {'laptop': {'qty': 2, 'cost': 2000.0}, 'mouse': {'qty': 2, 'cost': 50.0}}

# --- WRITE YOUR CODE HERE ---
cart_items = defaultdict(lambda: {'qty': 0, 'cost': 0.0})

for item, quantity, price in cart_adds:
    cost = quantity * price
    cart_items[item]['qty'] += quantity
    cart_items[item]['cost'] += cost

print("Problem 5: ", dict(cart_items))



# =====================================================================
# LEVEL 3: PRACTICAL ALGORITHMS
# =====================================================================

# PROBLEM 6: Social Network Followers
follows = [("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David"), ("Charlie", "David")]

# ### GUIDANCE ###
# 1. This is a graph adjacency list! We want to map a person to a list of 
#    everyone they follow. 
# 2. Initialize a defaultdict that creates empty lists.
# 3. Loop through `follows`. The first item in the tuple is the follower (the key), 
#    the second is who they followed (the value to append).
# Expected Output: {'Alice': ['Bob', 'Charlie'], 'Bob': ['David'], 'Charlie': ['David']}

# --- WRITE YOUR CODE HERE ---
heads = defaultdict(list)

for follower, followed in follows:
    heads[follower].append(followed)

print("Problem 6: ", dict(heads))


# PROBLEM 7: Grouping by Word Length
vocab = ["cat", "dog", "elephant", "mouse", "rat", "bat"]

# ### GUIDANCE ###
# 1. You are grouping words, so your defaultdict should use lists.
# 2. Loop through the `vocab` list.
# 3. The key for your dictionary should be the LENGTH of the word (an integer). 
#    You will need to calculate this inside the loop before appending the word.
# Expected Output: {3: ['cat', 'dog', 'rat', 'bat'], 8: ['elephant'], 5: ['mouse']}

# --- WRITE YOUR CODE HERE ---
bylength = defaultdict(list)

for animals in vocab:
    length_of_word = len(animals)
    bylength[length_of_word].append(animals)

print("Problem 7: ", dict(bylength))

# =====================================================================
# LEVEL 4: NESTED DEFAULTDICTS (Mind-Benders)
# =====================================================================

# PROBLEM 8: The Pixel Canvas
paints = [(0, 0, "red"), (1, 2, "blue"), (0, 0, "black"), (2, 4, "purple")]

# ### GUIDANCE ###
# 1. You are building a 2D grid: `canvas[x][y] = color`. 
# 2. The default value for ANY missing coordinate should be the string "white".
# 3. You need a nested defaultdict: the outer one uses a lambda to return an 
#    inner defaultdict. The inner defaultdict uses a lambda to return "white".
# 4. Loop through `paints`. Overwrite `canvas[x][y]` with the new color.
# 5. Print `canvas[0][0]` (should be "black") and `canvas[5][5]` (should be "white").

# --- WRITE YOUR CODE HERE ---
canvas = defaultdict(lambda: defaultdict(lambda: "white"))

for x, y, z in paints:
    canvas[x][y] = z

print("Problem 8: ", canvas[0][0], canvas[1][2], canvas[2][4], canvas[5][5])

# PROBLEM 9: Server Log Aggregation
logs = [
    ("Server_A", 404), ("Server_A", 500), 
    ("Server_B", 404), ("Server_A", 404)
]

# ### GUIDANCE ###
# 1. You want to track counts of error codes per server. 
#    Format: `logs_dict[server_name][error_code] += 1`
# 2. Set up a nested defaultdict. The outer lambda should return a 
#    defaultdict set up for counting (using `int`).
# 3. Loop through `logs`, unpack, and increment the nested keys.
# Expected Output: {'Server_A': {404: 2, 500: 1}, 'Server_B': {404: 1}}

# --- WRITE YOUR CODE HERE ---
error_codes = defaultdict(lambda: defaultdict(int))

for server, log in logs:
    error_codes[server][log] += 1

print("Problem 9: ", dict(error_codes))


# =====================================================================
# LEVEL 5: MASTERY
# =====================================================================

# PROBLEM 10: Building a File System
# ### GUIDANCE ###
# 1. Define a standard Python function called `tree`. 
# 2. Inside `tree`, return a new `defaultdict` that passes `tree` as its factory.
# 3. Create your `file_system` variable by calling `tree()`.
# 4. Without creating any intermediate dictionaries, directly assign:
#    - '500KB' to the path: home -> user -> documents -> resume.pdf
#    - '2MB' to the path: var -> log -> syslog
# 5. To verify it worked, print `file_system['var']['log']['syslog']`.

# --- WRITE YOUR CODE HERE ---
def tree():
    return defaultdict(tree)

file_system = tree()

file_system['var']['log']['syslog'] = '2MB'
file_system['home']['user']['documents']['resune.pdf'] = '500KB' 

print(file_system['var']['log']['syslog'])
