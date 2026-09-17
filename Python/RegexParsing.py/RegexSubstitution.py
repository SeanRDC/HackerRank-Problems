# ==========================================
# BLOCK 1: Regex Basics and The Overlap Trap
# ==========================================
import re

# ---------------------------------------------------------
# Problem 1: Basic Substitution
# ---------------------------------------------------------
# `re.sub(pattern, replacement, string)` searches a string for a regex pattern 
# and replaces it.
# Task: Use `re.sub()` to replace the word "cat" with "dog" in the text below.
# Print the result.
#  
# MOCK INPUT:
text1 = "I have a cat. The cat is sleeping."
#
# EXPECTED OUTPUT:
# I have a dog. The dog is sleeping.

# Write your code for Problem 1 here:
print(re.sub('cat', 'dog', text1))



# ---------------------------------------------------------
# Problem 2: Escaping Special Characters
# ---------------------------------------------------------
# In Regex, some characters have special meanings (like ., +, *, ?, |, &).
# To search for the ACTUAL character, you must "escape" it with a backslash (\).
# Task: Use `re.sub()` to replace the literal question mark `\?` with an 
# exclamation mark `!`. Print the result.
#
# MOCK INPUT:
text2 = "How are you? I am fine?"
#
# EXPECTED OUTPUT:
# How are you! I am fine!

# Write your code for Problem 2 here:
print(re.sub('\?', '!', text2))



# ---------------------------------------------------------
# Problem 3: Escaping the OR and AND operators
# ---------------------------------------------------------
# The pipe `|` means "OR" in Regex. The `&` can sometimes act weird too.
# Task: Write TWO `re.sub()` statements. 
# 1. Replace `&&` with `and` (regex: r"&&")
# 2. Replace `||` with `or` (regex: r"\|\|" -> notice the escape slashes!)
# Print both results.
#
# MOCK INPUT:
text3_a = "True && False"
text3_b = "True || False"
#
# EXPECTED OUTPUT:
# True and False
# True or False

# Write your code for Problem 3 here:
print(re.sub(r'&&', 'and', text3_a))
print(re.sub(r'\|\|', 'or', text3_b))



# ---------------------------------------------------------
# Problem 4: The "Space on Both Sides" Attempt
# ---------------------------------------------------------
# HackerRank requires a space on both sides. The naive approach is to just 
# include the spaces in the pattern and the replacement.
# Task: Use `re.sub()` to replace ` && ` (with spaces) with ` and ` (with spaces).
#
# MOCK INPUT:
text4 = "a && b"
#
# EXPECTED OUTPUT:
# a and b

# Write your code for Problem 4 here:
print(re.sub(r' && ', ' and ', text4))



# ---------------------------------------------------------
# Problem 5: The Overlap Trap
# ---------------------------------------------------------
# Here is why the naive approach from Problem 4 FAILS on HackerRank!
# If you have multiple `&&` separated by a single space, the first match 
# "eats" the shared space, so the second `&&` no longer has a space before it!
# Task: Run the exact same code you wrote for Problem 4, but on `text5`.
# Notice how the second `&&` gets completely ignored!
#
# MOCK INPUT:
text5 = "a && && b"
#
# EXPECTED OUTPUT:
# a and && b

# Write your code for Problem 5 here:
print(re.sub(r' && ', ' and ', text5))