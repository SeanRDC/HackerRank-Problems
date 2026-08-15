# ---------------------------------------------------------
# CONCEPT BLOCK 1: COMBINATIONS vs. PERMUTATIONS
# ---------------------------------------------------------

# Problem 1: The Import
# Concept: Import the `combinations` tool from the `itertools` module.
from itertools import combinations
# Problem 2: Basic Combinations
# Concept: Use `combinations("xyz", 2)`, cast it to a list, and print it. 
# Notice that ('x', 'y') is generated, but ('y', 'x') is not. Order doesn't matter!
print(list(combinations("xyz", 2)))
# Problem 3: Combinations with Duplicates
# Concept: Pass a list with identical elements: `['a', 'a', 'b']` into combinations 
# with K=2. Print the list. Notice it treats the two 'a's as separate, unique 
# items based on their original position!
print(list(combinations(['a', 'a', 'b'], 2)))

# Problem 4: The Length of an Iterator
# Concept: `combinations()` creates an iterator, which doesn't have a length.
# Try `len(combinations("abc", 2))`. You will get a TypeError. 
# Fix it by casting the combinations to a `list()` first, then wrapping it in `len()`.
print(len(list(combinations("abc", 2))))
# ---------------------------------------------------------
# CONCEPT BLOCK 2: TUPLE MEMBERSHIP & SEARCHING
# ---------------------------------------------------------

# Problem 5: The 'in' Keyword
# Concept: Create a tuple: `combo = ('c', 'd')`. Write an expression to check 
# if the string `'a'` is in the tuple. Print the result. (It should evaluate to False).
combo = ('c', 'd')
if 'a' in combo:
    print(True)
else:
    print(False)
# Problem 6: Boolean Mapping
# Concept: Create a list of tuples: `combos = [('a', 'b'), ('c', 'd'), ('a', 'c')]`.
# Write a list comprehension that loops through `combos` and returns True if `'a'` 
# is in the tuple, and False if it isn't.
# Mock Output: [True, False, True]
combos = [('a', 'b'), ('c', 'd'), ('a', 'c')]
result = [True if 'a' in i else False for i in combos]
# Expanded form
#for i in combos:
    #if 'a' in i:
        #result.append(True)
    #else:
        #result.append(False)
print(result)
# ---------------------------------------------------------
# CONCEPT BLOCK 3: BOOLEAN MATH (THE SECRET CHEAT CODE)
# ---------------------------------------------------------

# Problem 7: Adding Booleans
# Concept: In Python, True is exactly equal to 1, and False is 0. 
# Create a list `bools = [True, False, True, True]`. Pass it into Python's built-in 
# `sum()` function and print the result. 
# Mock Output: 3

# Problem 8: The Generator Expression
# Concept: Combine Problem 6 and 7! Instead of a list comprehension (which uses brackets []), 
# use a generator expression (which has no brackets) directly inside `sum()`.
# Write: `sum('a' in c for c in combos)` using the combos list from Problem 6.

# ---------------------------------------------------------
# CONCEPT BLOCK 4: INPUT PARSING STRATEGIES
# ---------------------------------------------------------

# Problem 9: The Throwaway Variable
# Concept: HackerRank gives us the length of the list (N) on line 1. But `len(list)` 
# makes this redundant! Read an input and assign it to a single underscore `_`. 
# This tells other programmers "I have to read this, but I'm ignoring it."

# Problem 10: Reading the Target List
# Concept: Read a space-separated string `"a a c d"` using `input().split()`. 
# Assign it to a variable `letters`.

# Problem 11: Reading K
# Concept: The third line of input is K. Read it and convert it to an integer.

# ---------------------------------------------------------
# CONCEPT BLOCK 5: PROBABILITY MATH
# ---------------------------------------------------------

# Problem 12: Basic Probability
# Concept: Probability is just (Favorable Outcomes) / (Total Outcomes).
# Create `favorable = 5` and `total = 6`. Create a variable `prob = favorable / total`.

# Problem 13: The Discrepancy
# Concept: The HackerRank instructions say "correct up to 3 decimal places".
# BUT the sample output is exactly `0.8333` (4 decimal places!). Always trust the sample output.
# Write an f-string to print `prob` rounded to exactly 4 decimal places.

# Problem 14: The Division by Zero Trap (Mental Check)
# Concept: If `total` combinations could theoretically be 0, dividing by it crashes your code. 
# However, look at the constraints: K <= N. You will always have at least 1 combination!

# ---------------------------------------------------------
# CONCEPT BLOCK 6: ADVANCED ALTERNATIVES (OPTIONAL MIND EXPANSION)
# ---------------------------------------------------------

# Problem 15: Index Combinations vs Value Combinations
# Concept: The problem asks to "select any K indices". 
# What if we did `combinations(range(4), 2)`? This gives us combinations of indices: 
# (0, 1), (0, 2), etc. 

# Problem 16: Checking Indices
# Concept: If we have an index tuple `(0, 2)`, how do we check the letters?
# We would have to do: `letters[0] == 'a' or letters[2] == 'a'`. 

# Problem 17: Why Values are Easier
# Concept: Compare Problem 16 to what we learned in Problem 5. 
# Isn't `'a' in ('a', 'c')` much easier to write? Because Python's `combinations` 
# treats identical items at different positions as unique anyway, passing the values 
# directly is vastly superior to passing the indices!

# Problem 18: The Complement Rule (Math Theory)
# Concept: Sometimes it's faster to find the combinations that do NOT have 'a'.
# If 1 out of 6 combinations has no 'a', then the probability of AT LEAST ONE 'a' is:
# 1.0 - (1 / 6). 

# Problem 19: Counting without 'a'
# Concept: Using the complement rule, write a generator expression inside `sum()` 
# that counts combinations where `'a'` is NOT in `c`. 

# Problem 20: The Final Blueprint
# Concept: You now have the tools. Read the throwaway N, read the letters, read K.
# Generate the combinations and cast to a list. Find the length (Total). 
# Sum the booleans (Favorable). Divide and format to 4 decimal places!

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- The Initial Inputs ---
# Line 1 input() receives: "4"
# (We assign this to `_` because we don't actually need it)

# Line 2 input() receives: "a a c d"
# The string is split, so `letters` becomes: ['a', 'a', 'c', 'd']

# Line 3 input() receives: "2"
# K is cast to int: 2

# --- Generating Combinations ---
# We pass `letters` and `K` into `combinations()` and cast to `list`.
# combos list becomes: 
# [
#   ('a', 'a'), 
#   ('a', 'c'), 
#   ('a', 'd'), 
#   ('a', 'c'), 
#   ('a', 'd'), 
#   ('c', 'd')
# ]

# --- The Math ---
# total_outcomes = len(combos)  --> evaluates to 6

# favorable_outcomes evaluates:
# 'a' in ('a', 'a') --> True (1)
# 'a' in ('a', 'c') --> True (1)
# 'a' in ('a', 'd') --> True (1)
# 'a' in ('a', 'c') --> True (1)
# 'a' in ('a', 'd') --> True (1)
# 'a' in ('c', 'd') --> False (0)
# favorable_outcomes = sum(...) --> evaluates to 5

# --- Final Output ---
# Math performed: 5 / 6 = 0.8333333333333334
# Formatted and printed to console: 0.8333