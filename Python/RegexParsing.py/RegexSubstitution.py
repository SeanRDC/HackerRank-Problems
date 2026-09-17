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

# ==========================================
# BLOCK 2: Lookarounds and Overlap Solutions
# ==========================================
import re

# ---------------------------------------------------------
# Problem 6: Positive Lookbehind
# ---------------------------------------------------------
# A Positive Lookbehind looks like this: (?<=...)
# It checks if something is BEFORE your match, but doesn't consume it.
# Task: Use `re.sub()` to replace `&&` with `and`, but ONLY if preceded by a space.
# Pattern: r"(?<= )&&"
# Replacement: "and" (Notice we do NOT put spaces in the replacement anymore!)
#
# MOCK INPUT:
text6 = "a && b"
#
# EXPECTED OUTPUT:
# a and b

# Write your code for Problem 6 here:
print(re.sub(r'(?<= )&&', 'and', text6))



# ---------------------------------------------------------
# Problem 7: Positive Lookahead
# ---------------------------------------------------------
# A Positive Lookahead looks like this: (?=...)
# It checks if something is AFTER your match, but doesn't consume it.
# Task: Use `re.sub()` to replace `&&` with `and`, but ONLY if followed by a space.
# Pattern: r"&&(?= )"
#
# MOCK INPUT:
text7 = "a && b"
#
# EXPECTED OUTPUT:
# a and b

# Write your code for Problem 7 here:
print(re.sub(r'&&(?= )', 'and', text7))



# ---------------------------------------------------------
# Problem 8: The Ultimate Overlap Solver
# ---------------------------------------------------------
# Now let's combine them! We want a space behind, and a space ahead.
# Pattern: r"(?<= )&&(?= )"
# Task: Apply this combined regex pattern to the exact same string from Problem 5 
# that tripped up the naive approach.
#
# MOCK INPUT:
text8 = "a && && b"
#
# EXPECTED OUTPUT:
# a and and b

# Write your code for Problem 8 here:
print(re.sub(r'(?<= )&&(?= )', 'and', text8))



# ---------------------------------------------------------
# Problem 9: Handling the OR Operator (||)
# ---------------------------------------------------------
# We need to do the exact same thing for the `||` operator.
# Remember from Problem 3 that you must escape the pipes `\|\|`.
# Task: Combine the lookbehind, the escaped pipes, and the lookahead into one pattern.
# Use `re.sub()` to replace it with `or`.
#
# MOCK INPUT:
text9 = "a || || b"
#
# EXPECTED OUTPUT:
# a or or b

# Write your code for Problem 9 here:
print(re.sub(r'(?<= )\|\|(?= )', 'or', text9))



# ---------------------------------------------------------
# Problem 10: Sequential Replacements
# ---------------------------------------------------------
# In HackerRank, a single line of text might contain BOTH `&&` and `||`.
# You can just run `re.sub()` twice! First save the result of the `&&` replacement, 
# then run the `||` replacement on that new string.
# Task: Write a function `modify_line(line)` that performs BOTH substitutions 
# (using your lookaround patterns) and returns the final modified string.
#
# MOCK INPUT / EXECUTION:
# print(modify_line("if a > 0 && b < 0 || c == 0:"))
#
# EXPECTED OUTPUT:
# if a > 0 and b < 0 or c == 0:

# Write your code for Problem 10 here:
def modify_line(line):
    and_mod = re.sub(r'(?<= )&&(?= )', 'and', line)
    return re.sub(r'(?<= )\|\|(?= )', 'or', and_mod)

print(modify_line("if a > 0 && b < 0 || c == 0:"))

# ==========================================
# BLOCK 3: Function Replacements & Final Assembly
# ==========================================
import re

# ---------------------------------------------------------
# Problem 11: The Combined Regex OR
# ---------------------------------------------------------
# You can match MULTIPLE patterns at once using the regex OR operator `|` 
# inside a group `()`. 
# Pattern: r"(?<= )(&&|\|\|)(?= )" 
# This means: "A space behind, THEN (either && OR ||), THEN a space ahead".
# Task: Use `re.findall()` with this pattern to extract all matches from `text11`.
# Print the result.
#
# MOCK INPUT:
text11 = "if a && b || c:"
#
# EXPECTED OUTPUT:
# ['&&', '||']

# Write your code for Problem 11 here:
print(re.findall(r"(?<= )(&&|\|\|)(?= )", text11))



# ---------------------------------------------------------
# Problem 12: The Replacement Function
# ---------------------------------------------------------
# When you pass a function into `re.sub`, it gives that function a "match object".
# You can get the matched string using `match.group(0)`.
# Task: Write a function `replace_logic(match)`.
# Inside it, get the string: `symbol = match.group(0)`
# If `symbol` is "&&", return "and".
# If `symbol` is "||", return "or".
#
# MOCK INPUT / EXECUTION (Simulating match objects):
# class MockMatch:
#     def __init__(self, s): self.s = s
#     def group(self, n): return self.s
#
# print(replace_logic(MockMatch("&&")))
# print(replace_logic(MockMatch("||")))
#
# EXPECTED OUTPUT:
# and
# or

# Write your code for Problem 12 here:
class MockMatch:
    def __init__(self, s): self.s = s
    def group(self, n): return self.s

def replace_logic(match):
    symbol = match.group(0)
    if symbol == "&&":
        return "and"
    if symbol == "||":
        return "or"
    
print(replace_logic(MockMatch("&&")))
print(replace_logic(MockMatch("||")))


# ---------------------------------------------------------
# Problem 13: Putting the Function in re.sub()
# ---------------------------------------------------------
# Now, let's use them together!
# Task: Use `re.sub()`. 
# Argument 1: Your combined pattern from Problem 11.
# Argument 2: Your `replace_logic` function from Problem 12 (do NOT use parenthesis!).
# Argument 3: `text13`.
# Print the result.
#
# MOCK INPUT:
text13 = "a && b || c && d"
#
# EXPECTED OUTPUT:
# a and b or c and d

# Write your code for Problem 13 here:
print(re.sub(r"(?<= )(&&|\|\|)(?= )", replace_logic ,text13))



# ---------------------------------------------------------
# Problem 14: The HackerRank Edge Case Test
# ---------------------------------------------------------
# HackerRank warns: "Note do not change &&& or ||| or & or |".
# Good news: Your lookaround pattern naturally solves this! 
# A `&&&` doesn't have a space on both sides of a `&&`.
# Task: Run your exact `re.sub()` code from Problem 13 on `text14` to prove 
# that it completely ignores `&&&` and `&`.
#
# MOCK INPUT:
text14 = "a &&& b & c ||| d && e"
#
# EXPECTED OUTPUT:
# a &&& b & c ||| d and e

# Write your code for Problem 14 here:
print(re.sub(r"(?<= )(&&|\|\|)(?= )", replace_logic ,text14))



# ---------------------------------------------------------
# Problem 15: The Final Blueprint
# ---------------------------------------------------------
# You are ready for the final HackerRank submission!
# Task: 
# 1. Copy your `replace_logic` function here.
# 2. Write a loop to read `N` lines (using `int(input())`).
# 3. Inside the loop, read each line, run your `re.sub()` using the combined 
#    pattern and the `replace_logic` function, and print the modified line.
#
# MOCK INPUT:
# 2
# if a + b > 0 && a - b < 0:
# elif a*b > 10 || a/b < 1:
#
# EXPECTED OUTPUT:
# if a + b > 0 and a - b < 0:
# elif a*b > 10 or a/b < 1:

# Write your final complete code for Problem 15 here:
def replace_logic(match):
    symbol = match.group(0)
    if symbol == "&&":
        return "and"
    if symbol == "||":
        return "or"

for _ in range(int(input())):
    n = input()
    print(re.sub(r"(?<= )(&&|\|\|)(?= )", replace_logic ,n))