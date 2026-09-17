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
    

