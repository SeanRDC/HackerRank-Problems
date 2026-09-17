# ==========================================
# BLOCK 1: Matrix Transposition and Zipping
# ==========================================

# ---------------------------------------------------------
# Problem 1: Row vs Column Reading
# ---------------------------------------------------------
# A matrix is just a list of strings (or a list of lists).
# Task: Create the `matrix` below. 
# Print the 1st character of the 1st string (row 0, col 0).
# Then print the 1st character of the 2nd string (row 1, col 0).
# (This simulates reading down the first column).
#
# MOCK INPUT:
matrix1 = ["Tsi", "h%x", "i #"]
#
# EXPECTED OUTPUT:
# T
# h

# Write your code for Problem 1 here:
print(matrix1[0][0])
print(matrix1[1][0])



# ---------------------------------------------------------
# Problem 2: Introduction to zip()
# ---------------------------------------------------------
# Python's `zip()` function takes multiple lists/strings and pairs up their 
# elements by index. 
# Task: Use `zip(row1, row2, row3)` on the strings below. 
# Loop through the zipped object and print each resulting tuple.
#
# MOCK INPUT:
row1 = "Tsi"
row2 = "h%x"
row3 = "i #"
#
# EXPECTED OUTPUT:
# ('T', 'h', 'i')
# ('s', '%', ' ')
# ('i', 'x', '#')

# Write your code for Problem 2 here:
zipped = zip(row1, row2, row3)
for i in zipped:
    print(i)


# ---------------------------------------------------------
# Problem 3: The Splat Operator (*)
# ---------------------------------------------------------
# Typing out `zip(matrix[0], matrix[1], ...)` is impossible if you don't know 
# how many rows there are. 
# The `*` (splat) operator unpacks a list so each element becomes a separate argument.
# Task: Call `print(*matrix3)` to see how it unpacks the list into separate strings.
#
# MOCK INPUT:
matrix3 = ["Tsi", "h%x", "i #"]
#
# EXPECTED OUTPUT:
# Tsi h%x i #

# Write your code for Problem 3 here:
print(*matrix3)



# ---------------------------------------------------------
# Problem 4: Zipping the Matrix (Transposition)
# ---------------------------------------------------------
# Let's combine Problem 2 and Problem 3. This is the ultimate Python trick 
# for reading a matrix column by column!
# Task: Use `zip(*matrix4)`. Loop through the zipped result and print each tuple.
# Notice how the output is perfectly grouped by columns!
#
# MOCK INPUT:
matrix4 = ["Tsi", "h%x", "i #"]
#
# EXPECTED OUTPUT:
# ('T', 'h', 'i')
# ('s', '%', ' ')
# ('i', 'x', '#')

# Write your code for Problem 4 here:
for i in zip(*matrix4):
    print(i)



# ---------------------------------------------------------
# Problem 5: Joining the Columns
# ---------------------------------------------------------
# Neo needs the final text as one single, continuous string.
# Task: Use `zip(*matrix5)`. Inside a loop, join the characters of each 
# column-tuple into a string, and concatenate them all into one giant string.
# Print the final giant string.
#
# MOCK INPUT:
matrix5 = ["Tsi", "h%x", "i #"]
#
# EXPECTED OUTPUT:
# This% ix#

# Write your code for Problem 5 here:
for i in zip(*matrix5):
    print(''.join(i), end="")
    
# ==========================================
# BLOCK 2: Regex Character Classes (\w and \W)
# ==========================================
import re

# ---------------------------------------------------------
# Problem 6: Finding Alphanumerics
# ---------------------------------------------------------
# In Regex, `\w` matches any "Word" character (A-Z, a-z, 0-9, and _).
# (For HackerRank's matrix cases, this perfectly represents alphanumerics).
# Task: Use `re.findall()` with the pattern r"\w" to find all 
# alphanumeric characters in the string below.
#
# MOCK INPUT:
text6 = "M@tr1x"
#
# EXPECTED OUTPUT:
# ['M', 't', 'r', '1', 'x']

# Write your code for Problem 6 here:
print(re.findall(r'\w', text6))



# ---------------------------------------------------------
# Problem 7: Finding Non-Alphanumerics (Symbols and Spaces)
# ---------------------------------------------------------
# The capital `\W` does the exact opposite: it matches anything that is 
# NOT alphanumeric (like spaces, #, %, !, etc.).
# Task: Use `re.findall()` with r"\W" to extract all symbols/spaces from `text7`.
#
# MOCK INPUT:
text7 = "Tsi h%x i #"
#
# EXPECTED OUTPUT:
# [' ', '%', ' ', ' ', '#']

# Write your code for Problem 7 here:
print(re.findall(r'\W', text7))



# ---------------------------------------------------------
# Problem 8: Grouping Symbols Together
# ---------------------------------------------------------
# Notice how Problem 7 returned single characters. If we have "$#is%", 
# we want to target "$#" as one big chunk to replace.
# Task: Add the `+` quantifier (which means "1 or more"). 
# Use `re.findall()` with r"\W+" to extract chunks of symbols.
#
# MOCK INPUT:
text8 = "This$#is% Matrix"
#
# EXPECTED OUTPUT:
# ['$#', '% ']

# Write your code for Problem 8 here:
print(re.findall(r'\W+', text8))



# ---------------------------------------------------------
# Problem 9: The Basic Replacement Attempt
# ---------------------------------------------------------
# Task: Use `re.sub()` to replace chunks of non-alphanumerics (r"\W+") 
# with a single space " ". Print the result.
#
# MOCK INPUT:
text9 = "This$#is% Matrix"
#
# EXPECTED OUTPUT:
# This is Matrix

# Write your code for Problem 9 here:
print(re.sub(r'\W+', ' ', text9))



# ---------------------------------------------------------
# Problem 10: The "Between" Trap
# ---------------------------------------------------------
# Here is the big trap of this challenge!
# Neo's rule: ONLY replace symbols that are BETWEEN two alphanumeric characters.
# Task: Run your exact same `re.sub()` from Problem 9 on `text10`.
# Look closely at the output. Notice how it incorrectly deleted the symbols 
# at the very end of the string!
#
# MOCK INPUT:
text10 = "This$#is% Matrix#  %!"
#
# EXPECTED OUTPUT (Notice the trailing symbols are gone - this is bad!):
# This is Matrix 

# Write your code for Problem 10 here:
print(re.sub(r'\W+', ' ', text10))

# ==========================================
# BLOCK 3: Lookarounds Return!
# ==========================================
import re

# ---------------------------------------------------------
# Problem 11: Lookbehind for Alphanumerics
# ---------------------------------------------------------
# We want to match symbols (\W+), but ONLY if there is an alphanumeric (\w) behind them.
# Task: Use `re.sub()` with a Positive Lookbehind.
# Pattern: r"(?<=\w)\W+"
# Replace it with a space " ", and run it on `text11`.
# (Notice how it ignores the leading "$$" because there is no letter before it!)
#
# MOCK INPUT:
text11 = "$$This$#is"
#
# EXPECTED OUTPUT:
# $$This is

# Write your code for Problem 11 here:
print(re.sub(r'(?<=\w)\W+', ' ', text11))



# ---------------------------------------------------------
# Problem 12: Lookahead for Alphanumerics
# ---------------------------------------------------------
# Now we do the opposite. We want to match symbols (\W+), but ONLY if 
# there is an alphanumeric (\w) ahead of them.
# Task: Use `re.sub()` with a Positive Lookahead.
# Pattern: r"\W+(?=\w)"
# Replace with a space " ", and run it on `text12`.
# (Notice how it ignores the trailing "$$" because there is no letter after it!)
#
# MOCK INPUT:
text12 = "is% Matrix$$"
#
# EXPECTED OUTPUT:
# is Matrix$$

# Write your code for Problem 12 here:
print(re.sub(r'\W+(?=\w)', ' ', text12))



# ---------------------------------------------------------
# Problem 13: The Ultimate "Between" Solver
# ---------------------------------------------------------
# Let's combine them to perfectly satisfy Neo's condition!
# We want a word character behind, and a word character ahead.
# Pattern: r"(?<=\w)\W+(?=\w)"
# Task: Run this combined pattern using `re.sub()` on `text13`.
# Replace matches with a single space " ".
#
# MOCK INPUT:
text13 = "This$#is% Matrix#  %!"
#
# EXPECTED OUTPUT:
# This is Matrix#  %!

# Write your code for Problem 13 here:
print(re.sub(r'(?<=\w)\W+(?=\w)', ' ', text13))



# ---------------------------------------------------------
# Problem 14: Testing the Edge Cases
# ---------------------------------------------------------
# Let's make absolutely sure this regex is bulletproof. 
# It should ignore leading symbols, replace inner symbols, and ignore trailing symbols.
# Task: Run your exact `re.sub()` code from Problem 13 on `text14`.
#
# MOCK INPUT:
text14 = "!@# Neo$#is% The&*(One !@#"
#
# EXPECTED OUTPUT:
# !@# Neo is The One !@#

# Write your code for Problem 14 here:
print(re.sub(r'(?<=\w)\W+(?=\w)', ' ', text14))



# ---------------------------------------------------------
# Problem 15: Applying it to the Transposed Matrix
# ---------------------------------------------------------
# Let's simulate the end of the script. 
# 1. We transpose the matrix using your brilliant `zip(*matrix)` trick.
# 2. We join it into one giant string.
# 3. We run the final Regex lookaround substitution on that string.
# Task: Write a script that loops through the transposed matrix, joins the 
# characters into `final_string`, and then runs your `re.sub()` on `final_string`.
# Print the fully decoded string!
#
# MOCK INPUT (Variables provided):
matrix15 = [
    "Tsi",
    "h%x",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "ir!"
]

# Write your code for Problem 15 here:
new_matrix = ""
for i in zip(*matrix15):
    new_matrix += ''.join(i)

print(re.sub(r'(?<=\w)\W+(?=\w)', ' ', new_matrix))