# ==============================================================================
# CHALLENGE: COMPANY LOGO
# ==============================================================================
# Goal: 
# Given a string of lowercase letters, find the three most common characters.
# You must output the characters and their occurrence count, sorted in 
# descending order of count. If two characters have the same count, they must 
# be sorted in ascending alphabetical order.
#
# Test Input Breakdown:
# String: "aabbbccde"
# Counts: a=2, b=3, c=2, d=1, e=1
# Sorting Logic: 
#   - 'b' has 3 (Highest count, goes first)
#   - 'a' and 'c' both have 2 (Count is tied)
#   - 'a' comes before 'c' alphabetically (Tie broken, 'a' goes second)
#
# Constraints & Nuances:
# The string will have at least 3 distinct characters.
# Standard descending sorts usually ruin alphabetical tie-breakers, so you 
# need a specific complex sorting strategy to handle both simultaneously.
# ==============================================================================

# ---------------------------------------------------------
# PHASE 1: COUNTING CHARACTERS
# ---------------------------------------------------------

# Problem 1: The Import
# We need a highly efficient way to count items in an iterable. Write the code 
# to import the `Counter` class from the built-in `collections` module.
from collections import Counter
# Problem 2: Mock Input
# Create a variable named `mock_string` and assign it the string value "google".
mock_string = "google"
# Problem 3: Initialization
# Pass `mock_string` into the `Counter` class you imported and save the resulting 
# object to a variable named `char_counts`.
char_counts = Counter(mock_string)

# Problem 4: Extracting Items
# A Counter behaves similarly to a dictionary. Use a built-in dictionary method 
# to extract the keys and values from `char_counts` as a list-like object of tuples.
# Save this to a variable named `items_list`.
# Mock Output: dict_items([('g', 2), ('o', 2), ('l', 1), ('e', 1)])
items_list = char_counts.items()

# ---------------------------------------------------------
# PHASE 2: SORTING MECHANICS (THE TIE-BREAKER PROBLEM)
# ---------------------------------------------------------

# Problem 5: Mock Tuples
# Create a hardcoded list of tuples named `mock_tuples` to test sorting.
# Mock Input: [('c', 2), ('a', 2), ('b', 3)]
mock_tuples = [('c', 2), ('a', 2), ('b', 3)]
# Problem 6: Native Sorting
# Use Python's built-in `sorted()` function on `mock_tuples` and save it to `sorted_1`.
# What happens? Python sorts tuples by checking the first element (the letter).
# Mock Output: [('a', 2), ('b', 3), ('c', 2)] 
sorted_1 = sorted(mock_tuples)

# Problem 7: Lambda Introduction
# To sort by the count (the number), we need a custom sorting key. 
# Write a simple anonymous `lambda` function named `get_count` that takes a single 
# tuple `t` as an argument and returns the item at index 1 (the number).
get_count = lambda t: t[1]
# Problem 8: Sorting by Count
# Use `sorted()` on `mock_tuples` again, but this time pass `key=get_count`.
# Save it to `sorted_2`. Note that this sorts in ascending order (2, 2, 3).
# Mock Output: [('c', 2), ('a', 2), ('b', 3)]
sorted_2 = sorted(mock_tuples, key=get_count)

# Problem 9: The Reverse Trap
# Try sorting `mock_tuples` using `key=get_count` AND `reverse=True`. 
# Save it to `sorted_3`. 
# Notice the problem? The counts are descending (3, 2, 2), but because the whole 
# list was flipped, 'c' comes before 'a' for the tied counts! 
# Mock Output: [('b', 3), ('a', 2), ('c', 2)] (Wait, 'a' and 'c' might flip depending on initial order).
sorted_3 = sorted(mock_tuples, key=get_count, reverse=True)

# Problem 10: The Negative Math Trick
# How do we force the numbers to sort descending without using `reverse=True`? 
# We make them negative! Write a new lambda named `get_neg_count` that takes 
# tuple `t` and returns the item at index 1 multiplied by -1 (or just `-t[1]`).
get_neg_count = lambda t: t[1] * -1

# Problem 11: Sorting by Negative Count
# Use `sorted()` on `mock_tuples` with `key=get_neg_count`. Save to `sorted_4`.
# Now the counts act descending (-3 comes before -2). 
# Mock Output: [('b', 3), ('c', 2), ('a', 2)]
sorted_4 = sorted(mock_tuples, key=get_neg_count)

# Problem 12: Complex Tuple Keys
# We solved the numbers, but how do we guarantee alphabetical order for ties?
# Python sorts tuples element by element. If the first element ties, it looks at the second.
# Write a lambda named `complex_key` that takes a tuple `t` and returns a NEW tuple: 
# The first element is the negative count (`-t[1]`).
# The second element is the character itself (`t[0]`).
complex_key = lambda t: (-t[1], t[0])
# Problem 13: Applying the Master Sort
# Use `sorted()` on `mock_tuples` using your `complex_key` lambda. Save to `sorted_5`.
# The sorting engine will now sort counts descending (via negative math) and 
# immediately fall back to standard alphabetical order for ties!
# Expected Output: [('b', 3), ('a', 2), ('c', 2)]
sorted_5 = sorted(mock_tuples, key=complex_key)
print(sorted_5)
# ---------------------------------------------------------
# PHASE 3: EXTRACTION & FORMATTING
# ---------------------------------------------------------

# Problem 14: Mock Slicing List
# Create a standard list of integers named `numbers` containing 1 through 5.
numbers = [1, 2, 3, 4, 5]
# Problem 15: Slicing Syntax
# We only want the top 3 items. Use list slicing syntax on `numbers` to extract 
# from the beginning of the list up to (but not including) index 3. Save to `top_nums`.
# Mock Output: [1, 2, 3]
top_nums = numbers[:3]

# Problem 16: Looping over Iterables
# Write a `for` loop that iterates over your `mock_tuples` list. 
# Temporarily assign the looping variable as `item`.

# for item in mock_tuples:

# Problem 17: Unpacking in the Loop
# Instead of using a single variable `item`, modify your `for` loop definition 
# to directly unpack the tuple into two variables: `char` and `count`.
for char, count in mock_tuples:
# Problem 18: String Formatting
# Inside the loop, use an f-string (or standard string formatting) to print 
# the `char` and the `count` separated by a space.
    print(f"{char} {count}")
# ---------------------------------------------------------
# PHASE 4: PREPARING THE FINAL LOGIC
# ---------------------------------------------------------

# Problem 19: Standard Input
# Imagine moving to standard input. Read a string from input, strip it of whitespace, 
# and save it to a variable `s`.
s = input().strip()
# Problem 20: Bringing it all together mentally
# If you combine Phase 1 (generating items from a string), Phase 2 (sorting those 
# items with a complex tuple key), and Phase 3 (slicing the top 3 and printing), 
# you will have solved the entire challenge!
count = Counter(s)
counted = count.items()
sorting_key = lambda t: (t[1] * -1, t[0])
sorted_mech = sorted(counted, key=sorting_key)
cut_chars = sorted_mech[:3]
for char, value in cut_chars:
    print(f"{char} {value}")
# ==============================================================================
# FINAL SUBMISSION
# ==============================================================================
# Summary:
# By passing a lambda function that returns a tuple `(-count, char)` to the `key` 
# argument of `sorted()`, you force Python's native sorting engine to handle 
# descending numerical checks and ascending alphabetical tie-breakers simultaneously.
#
# Mock Input (Stdin):
# aabbbccde
#
# Expected Output:
# b 3
# a 2
# c 2
# ==============================================================================
s = input().strip()

count = Counter(s).items()
sorting_key = lambda t: (-t[1], t[0])
sorted_mech = sorted(count, key=sorting_key)[:3]
for char, value in sorted_mech:
    print(f"{char} {value}")