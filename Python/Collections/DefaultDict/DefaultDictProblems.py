# Ten defaultdict practice problems covering counting, grouping, sets, lambda defaults,
# nested defaultdicts, and a recursive tree.

from collections import defaultdict

votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Alice', 'Bob']

voters_list = defaultdict(int)
for voters in votes:
    voters_list[voters] += 1

print("Problem 1: ", dict(voters_list))

grades = [('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A'), ('David', 'C'), ('Eve', 'B')]

student_grades = defaultdict(list)

for student, grade in grades:
    student_grades[grade].append(student)

print("Problem 2: ", dict(student_grades))

page_visits = [
    ('home', 'user1'), ('about', 'user2'), 
    ('home', 'user1'), ('home', 'user3')
]

visitors = defaultdict(set)
for page, guests in page_visits:
    visitors[page].add(guests)

print("Problem 3: ", dict(visitors))

dictionary_data = [('hello', 'hola'), ('world', 'mundo')]

data = defaultdict(lambda: "NOT FOUND")

for word, translation in dictionary_data:
    data[word] = translation
    data[translation] = word

print("Problem 4: ", data['hello'], data['world'], data['apple'])

cart_adds = [
    ('laptop', 1, 1000.0), 
    ('mouse', 2, 25.0), 
    ('laptop', 1, 1000.0)
]

cart_items = defaultdict(lambda: {'qty': 0, 'cost': 0.0})

for item, quantity, price in cart_adds:
    cost = quantity * price
    cart_items[item]['qty'] += quantity
    cart_items[item]['cost'] += cost

print("Problem 5: ", dict(cart_items))

follows = [("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David"), ("Charlie", "David")]

heads = defaultdict(list)

for follower, followed in follows:
    heads[follower].append(followed)

print("Problem 6: ", dict(heads))

vocab = ["cat", "dog", "elephant", "mouse", "rat", "bat"]

bylength = defaultdict(list)

for animals in vocab:
    length_of_word = len(animals)
    bylength[length_of_word].append(animals)

print("Problem 7: ", dict(bylength))

paints = [(0, 0, "red"), (1, 2, "blue"), (0, 0, "black"), (2, 4, "purple")]

canvas = defaultdict(lambda: defaultdict(lambda: "white"))

for x, y, z in paints:
    canvas[x][y] = z

print("Problem 8: ", canvas[0][0], canvas[1][2], canvas[2][4], canvas[5][5])

logs = [
    ("Server_A", 404), ("Server_A", 500), 
    ("Server_B", 404), ("Server_A", 404)
]

error_codes = defaultdict(lambda: defaultdict(int))

for server, log in logs:
    error_codes[server][log] += 1

print("Problem 9: ", dict(error_codes))

def tree():
    return defaultdict(tree)

file_system = tree()

file_system['var']['log']['syslog'] = '2MB'
file_system['home']['user']['documents']['resune.pdf'] = '500KB' 

print(file_system['var']['log']['syslog'])
