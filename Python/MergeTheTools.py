# ==========================================
# SET 1: CHUNKING THE STRING
# ==========================================
# First, we need to break the long string into smaller substrings of size k.

# MOCK INPUT:
# s = 'AABCAAADA'
# k = 3

# Problem 1: Create the mock variables `s` and `k`.

# Problem 2: Write a loop that iterates over the indices of `s`, but instead of 
# going up by 1, it steps by `k`. (Hint: Use `range(start, stop, step)`).

# Problem 3: Inside the loop, slice the string `s` from the current index 
# to the current index plus `k`. Save this to a variable called `chunk`.

# Problem 4: Still inside the loop, print `chunk`.
# EXPECTED OUTPUT:
# AAB
# CAA
# ADA


# ==========================================
# SET 2: DEDUPLICATING (THE HARD WAY)
# ==========================================
# Now we need to remove duplicate letters from a string, but KEEP the original order.

# MOCK INPUT:
# chunk = 'AAB'

# Problem 5: Create a new mock variable `chunk` set to 'AAB'.

# Problem 6: Create an empty string variable called `unique_chunk`. 
# We will use this to build our final word letter by letter.

# Problem 7: Write a loop that iterates through every character in `chunk`.

# Problem 8: Inside the loop, write a conditional statement: check if the character 
# is NOT `in` your `unique_chunk` string.

# Problem 9: If it is not in there yet, add the character to `unique_chunk`.

# Problem 10: Outside the loop, print `unique_chunk`. 
# EXPECTED OUTPUT: AB
# (Try changing chunk to 'ADA' and running it again. It should print 'AD').


# ==========================================
# SET 3: COMBINING THE STEPS
# ==========================================
# Let's put the deduplicator inside the chunking loop.

# MOCK INPUT:
# s = 'AABCAAADA'
# k = 3

# Problem 11: Set up your `s` and `k` variables again, and write your `range` loop 
# that steps by `k` (from Set 1).

# Problem 12: Inside that loop, slice the string to get your `chunk` (from Set 1).

# Problem 13: Right below that, create your empty `unique_chunk` string, and write 
# your inner loop that checks characters and adds them if they are new (from Set 2).

# Problem 14: At the very end of the outer loop, print `unique_chunk`.
# EXPECTED OUTPUT:
# AB
# CA
# AD


# ==========================================
# SET 4: THE DICTIONARY SHORTCUT (THE EASY WAY)
# ==========================================
# Modern Python (3.7+) guarantees that dictionaries remember the order items are added.
# Because dictionary keys MUST be unique, we can use this to instantly deduplicate!
# NEW SYNTAX: `dict.fromkeys(iterable)` creates a dictionary where the keys are the 
# characters of your string, automatically dropping any duplicates!

# MOCK INPUT:
# chunk = 'AAB'

# Problem 15: Create the mock variable `chunk`.

# Problem 16: Use `dict.fromkeys(chunk)` and save it to a variable called `my_dict`.
# Print `my_dict`.
# EXPECTED OUTPUT: {'A': None, 'B': None} (Notice the extra 'A' is gone!)

# Problem 17: We just need the keys joined together as a string. 
# Use `"".join()` directly on `my_dict` and print it.
# EXPECTED OUTPUT: AB

# Problem 18: Marvel at how the 4-line inner loop from Set 3 can be replaced 
# by a single `.join(dict.fromkeys())` statement.


# ==========================================
# SET 5: THE GRAND FINALE
# ==========================================
# Let's plug this into the official HackerRank function template.

# Problem 19: Define the function exactly as HackerRank asks: 
# `def merge_the_tools(string, k):`

# Problem 20: Inside the function, write your chunking loop. Inside that loop, 
# grab the chunk, and print the deduplicated version using whichever method you prefer 
# (the manual string builder or the dictionary shortcut). 

# Test it by calling:
# merge_the_tools('AABCAAADA', 3)