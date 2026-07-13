# =====================================================================
# SET 1: MASTERING THE FIRST LINE (n, m = map(int, input().split()))
# =====================================================================

# PROBLEM 1: The Raw Input
# Concept: `input()` grabs an entire line of text as a single string.
# Task: Ask the user for input and print exactly what they typed.
# Mock Input to type: 5 2
# Expected Output: '5 2'

# --- WRITE YOUR CODE HERE ---



# PROBLEM 2: The Split
# Concept: `.split()` breaks a string into a list of strings based on spaces.
# Task: Take the string "5 2" and split it into a list. Print the list.
# Expected Output: ['5', '2']

# --- WRITE YOUR CODE HERE ---



# PROBLEM 3: The Map
# Concept: `map(int, ...)` applies the `int` function to every item in a list.
# Task: Use `map` to turn the list ['5', '2'] into integers, convert it 
# back to a list, and print it.
# Expected Output: [5, 2]

# --- WRITE YOUR CODE HERE ---



# PROBLEM 4: Tuple Unpacking
# Concept: You can assign multiple variables at once from a list/iterable.
# Task: Given the list [5, 2], assign the first number to `n` and the 
# second to `m` in a single line. Print `n` and `m`.
# Expected Output: n is 5, m is 2

# --- WRITE YOUR CODE HERE ---



# PROBLEM 5: SYNTHESIS (The First Line)
# Task: Combine Problems 1-4 into a SINGLE line of code. 
# Prompt the user for input. When they type "5 2", your code should 
# instantly store 5 in `n` and 2 in `m`. Print them to verify.
# Mock Input to type: 5 2
# Expected Output: 5 2

# --- WRITE YOUR CODE HERE ---





# =====================================================================
# SET 2: LOOPING AND 1-BASED INDEXING
# =====================================================================

# PROBLEM 6: The Basic Loop
# Concept: `for i in range(n)` loops `n` times, starting at 0.
# Task: Hardcode `n = 3`. Write a loop that prints `i` on each turn.
# Expected Output: 
# 0
# 1
# 2

# --- WRITE YOUR CODE HERE ---



# PROBLEM 7: The +1 Shift
# Concept: The problem requires 1-based indexing, not 0-based.
# Task: Hardcode `n = 3`. Write a loop, but print `i + 1` instead of `i`.
# Expected Output:
# 1
# 2
# 3

# --- WRITE YOUR CODE HERE ---



# PROBLEM 8: Looped Inputs
# Concept: You can call `input()` inside a loop to read multiple lines.
# Task: Hardcode `n = 2`. Write a loop that runs `n` times. Inside, ask 
# for a `word` using `input()`, and immediately print that word.
# Mock Inputs to type: apple, banana

# --- WRITE YOUR CODE HERE ---



# PROBLEM 9: Appending to Defaultdict
# Concept: `group_a[word].append(value)`
# Task: Import defaultdict. Create `group_a = defaultdict(list)`. 
# Hardcode `word = 'cat'`. Append the number 1 to `group_a[word]`. Print the dict.
# Expected Output: {'cat': [1]}

# --- WRITE YOUR CODE HERE ---



# PROBLEM 10: SYNTHESIS (Building Group A)
# Task: Combine Problems 6-9. 
# 1. Hardcode `n = 3`. 
# 2. Create `group_a = defaultdict(list)`.
# 3. Loop `n` times. 
# 4. Each loop, grab a `word` via `input()`.
# 5. Append `i + 1` to that word's list in `group_a`. 
# 6. Print `group_a`.
# Mock Inputs to type: cat, dog, cat
# Expected Output: {'cat': [1, 3], 'dog': [2]}

# --- WRITE YOUR CODE HERE ---





# =====================================================================
# SET 3: SAFE LOOKUPS (if word in group_a)
# =====================================================================

# PROBLEM 11: The Second Loop
# Concept: We need to process Group B now. 
# Task: Hardcode `m = 2`. Write a loop that asks for a `word` via `input()` 
# `m` times. Print "Searching for [word]".
# Mock Inputs to type: dog, bird

# --- WRITE YOUR CODE HERE ---



# PROBLEM 12: The 'in' Keyword
# Concept: Checking if a key exists WITHOUT triggering the defaultdict factory.
# Task: Hardcode `my_dict = {'apple': [1]}`. 
# Write an `if` statement checking if 'apple' is in `my_dict`. If so, print "Found!".
# Expected Output: Found!

# --- WRITE YOUR CODE HERE ---



# PROBLEM 13: The 'else' Fallback
# Concept: Handling the missing words.
# Task: Using the same `my_dict` from Problem 12, write an `if/else` 
# statement for the word 'banana'. If it's in the dict, print "Found!". 
# Else, print "-1".
# Expected Output: -1

# --- WRITE YOUR CODE HERE ---



# PROBLEM 14: Printing the Value
# Concept: If the key is found, we want the list, not just the word "Found".
# Task: Using `my_dict = {'apple': [1, 5]}`, write an if statement. 
# If 'apple' is in the dict, print its value (the list).
# Expected Output: [1, 5]

# --- WRITE YOUR CODE HERE ---



# PROBLEM 15: SYNTHESIS (Processing Group B safely)
# Task: Combine 11-14. 
# 1. Hardcode `m = 2` and `group_a = {'cat': [1, 3]}`.
# 2. Loop `m` times.
# 3. Grab a `word` via `input()`.
# 4. If the word is in `group_a`, print the list. Else, print '-1'.
# Mock Inputs to type: cat, mouse
# Expected Output for cat: [1, 3]
# Expected Output for mouse: -1

# --- WRITE YOUR CODE HERE ---





# =====================================================================
# SET 4: UNPACKING AND FINAL ASSEMBLY
# =====================================================================

# PROBLEM 16: The List Problem
# Concept: `print([1, 2, 3])` prints brackets and commas. HackerRank hates that.
# Task: Create `my_list = [1, 2, 3]`. Print it normally just to see the brackets.
# Expected Output: [1, 2, 3]

# --- WRITE YOUR CODE HERE ---



# PROBLEM 17: The Asterisk (*) Unpacker
# Concept: Putting `*` before a list in a print statement unpacks it 
# into space-separated arguments.
# Task: Take `my_list = [1, 2, 3]` and print it using `*my_list`.
# Expected Output: 1 2 3

# --- WRITE YOUR CODE HERE ---



# PROBLEM 18: Fixing Problem 15's Output
# Task: Hardcode `group_a = {'cat': [1, 3]}` and `word = 'cat'`.
# Write the `if word in group_a:` check again, but this time use the 
# asterisk `*` so it prints without brackets!
# Expected Output: 1 3

# --- WRITE YOUR CODE HERE ---



# PROBLEM 19: The Skeleton (Mental Prep)
# Task: Do NOT write any code here. Just read and understand the flow:
# 1. Get n and m from input.
# 2. Setup defaultdict(list)
# 3. Loop n times -> get word -> append (i + 1) to dict
# 4. Loop m times -> get word -> if in dict, print with * -> else print -1
# (Just type "Understood" in a comment when you are ready).

# --- WRITE YOUR CODE HERE ---



# PROBLEM 20: THE FINAL EXAM
# Task: Write the ENTIRE script from scratch, memory, and understanding. 
# Do not look at the top of the page.
# Use this exact Mock Data to test it:
# Input 1 (n m): 5 2
# Input 2-6 (Group A): a, a, b, a, b
# Input 7-8 (Group B): a, c
# Expected Final Output in terminal:
# 1 2 4
# -1

# --- WRITE YOUR CODE HERE ---