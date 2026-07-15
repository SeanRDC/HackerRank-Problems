# ==========================================
# SET 1: TUPLE BASICS (THE LOCKED LIST)
# ==========================================

# Problem 1: Create a tuple of numbers using parentheses `()` instead of square brackets `[]`. Print it.
# Expected Output: (1, 2, 3)
my_tuple = (1, 2, 3)
print(my_tuple)

# Problem 2: Tuples act just like lists when reading data. Print the item at index 1 of your tuple.
# Mock Input: my_tup = (1, 2, 3)
# Expected Output: 2
print(my_tuple[1])

# Problem 3: Try to change index 0 of your tuple to the number 99 (e.g., `my_tup[0] = 99`). 
# Run it, watch it crash with a TypeError, and then comment out the line so your code works again. 
# (This proves tuples are IMMUTABLE!)
# my_tuple[0] = 99

# Problem 4: You can convert a standard list into a tuple using the `tuple()` function. 
# Convert `my_list` into a tuple and print it.
my_list = [7, 8, 9]
# Expected Output: (7, 8, 9)
print(tuple(my_list))

# Problem 5 (MINI-BOSS: COMBINE 1-4):
# Create a standard list `boss_list = [4, 5, 6]`. Convert it to a tuple called `boss_tup`.
# Print the length of `boss_tup` using `len()`.
# Expected Output: 3
boss_list = [4, 5, 6]
boss_tup = tuple(boss_list)
print(len(boss_tup))

# ==========================================
# SET 2: MAPPING DIRECTLY TO TUPLES
# ==========================================

# Problem 6: Given a raw input string, split it into a list of strings. Print the list.
raw_input = "10 20 30"
# Expected Output: ['10', '20', '30']
new_list = raw_input.split()
print(new_list)

# Problem 7: Wrap your split string inside `map(int, ...)`. Save it to `mapped_data` and print it.
# (Notice how it doesn't print the numbers? It prints a weird memory object like `<map object at 0x...>`)
raw_input = "10 20 30"
mapped_data = map(int, raw_input.split())
print(mapped_data)

# Problem 8: Convert `mapped_data` into a list using `list()` and print it.
# Expected Output: [10, 20, 30]
my_list = list(mapped_data)
print(my_list)

# Problem 9: Wait, we don't want a list! Run the map function again, but this time, 
# wrap it in `tuple()` instead of `list()`. Print the tuple.
# Expected Output: (10, 20, 30)
my_tup = tuple(map(int, raw_input.split()))
print(my_tup)

# Problem 10 (MINI-BOSS: COMBINE 6-9):
# Write a 1-line converter! Take `boss_input`, split it, map it to integers, 
# and convert it directly into a tuple called `boss_tup`. Print `boss_tup`.
boss_input = "99 88 77"
# Expected Output: (99, 88, 77)
boss_tup = tuple(map(int, boss_input.split()))
print(boss_tup)

# ==========================================
# SET 3: THE HASH() FUNCTION
# ==========================================
# A "hash" is a fixed-size integer that Python generates to uniquely identify a piece of data. 

# Problem 11: Print the hash of an integer. (Surprise: the hash of a small integer is just itself!)
num = 5
# Expected Output: 5
print(hash(num))

# Problem 12: Print the hash of a string. 
my_string = "Hello"
# Expected Output: (A giant random number, e.g., 65123985123...)
print(hash(my_string))

# Problem 13: Print the hash of a tuple.
my_tup1 = (1, 2)
# Expected Output: 3713081631934410656 
print(hash(my_tup1))

# Problem 14: Try to print the hash of a list: `hash([1, 2])`. 
# Run it, watch it crash with a TypeError, and comment it out. 
# (Why? Because lists can change! Python refuses to fingerprint something that might change later).
# print(hash[1, 2])

# Problem 15 (MINI-BOSS: COMBINE 11-14):
# Create a tuple containing the strings "Hacker" and "Rank". 
# Save it to `word_tup`. Print `hash(word_tup)`.
word_tup = ('Hacker', 'Rank')
print(hash(word_tup))

# ==========================================
# SET 4: THE GRAND FINALE (HACKERRANK READY)
# ==========================================

# Problem 16: Read the integer `n` (the number of elements in the tuple). 
# Once again, we just capture it so it doesn't mess up our input stream.
# Mock Input: n = int("2")

# Problem 17: Take the second line of input as a string.
# Mock Input: raw = "1 2"

# Problem 18: Split the string and map it to integers.
# Mock Input: mapped = map(int, raw.split())

# Problem 19: Convert that mapped data directly into a tuple called `t`.
# Expected Output of t: (1, 2)

# Problem 20 (THE GRAND FINALE):
# Put it all together! Read `n`, take the next input, convert it straight into a tuple of integers `t`, 
# and print `hash(t)`. Test it against HackerRank's Sample Input!
# Mock Input: 
# 2
# 1 2
# Expected Output: 3713081631934410656