# ==============================================================================
# CHALLENGE: REGULAR EXPRESSIONS (GMAIL ACCOUNTS)
# ==============================================================================
# Goal: 
# You are given a list of names and email addresses. Your task is to filter 
# out only the people who have an email address ending in "@gmail.com". 
# Then, you must sort their first names alphabetically and print them one per line.
#
# Test Input Breakdown:
# Line 1: `6` (The number of rows/users to process)
# Line 2: `riya riya@gmail.com` (Valid, keep "riya")
# Line 3: `julia julia@julia.me` (Invalid, ignore)
# Line 4: `julia sjulia@gmail.com` (Valid, keep "julia")
# Line 5: `julia julia@gmail.com` (Valid, keep "julia")
# Line 6: `samantha samantha@gmail.com` (Valid, keep "samantha")
# Line 7: `tanya tanya@gmail.com` (Valid, keep "tanya")
#
# Constraints & Nuances:
# You must use Regular Expressions (Regex) to evaluate the email.
# The filtered names must be sorted alphabetically before printing.
# Duplicate names are allowed and should be printed as many times as they appear.
# ==============================================================================

# ---------------------------------------------------------
# PHASE 1: REGULAR EXPRESSION FUNDAMENTALS
# ---------------------------------------------------------

# Problem 1: The Import
# Regex requires a specific module in Python. Write the code to import the `re` module.

# Problem 2: The Literal String
# We are looking for emails that end with "@gmail.com". In regex, a period "." 
# is a special character that means "any character". To match a literal period, 
# you must escape it with a backslash. 
# Concept: How do you write "@gmail.com" so that the period is treated as a literal dot?

# Problem 3: The End-of-String Anchor
# If an email is "user@gmail.com.org", it contains "@gmail.com" but does not END with it.
# In regex, the dollar sign "$" asserts that the match must happen at the very end of the string.
# Concept: Combine your escaped string from Problem 2 with the end-of-string anchor.

# Problem 4: Defining the Pattern
# Create a variable named `regex_pattern`.
# Assign it a raw string (prefix the string with an 'r', like r"pattern") containing 
# the combined regex logic you figured out in Problem 3.

# Problem 5: The Match Function
# Python's `re.search(pattern, string)` scans through a string looking for a match.
# Create a mock email: `test_email_1 = "alice@gmail.com"`
# Use `re.search()` to check `test_email_1` against your `regex_pattern`.
# Mock Output: A Match object (e.g., <re.Match object; span=(5, 15), match='@gmail.com'>)

# Problem 6: Testing Invalid Domains
# Create another mock email: `test_email_2 = "bob@yahoo.com"`
# Use `re.search()` on this email. 
# Mock Output: None

# Problem 7: Testing the Anchor
# Create a tricky mock email: `test_email_3 = "charlie@gmail.com.uk"`
# Use `re.search()` on this email. Because of your "$" anchor, it should reject it.
# Mock Output: None

# ---------------------------------------------------------
# PHASE 2: DATA STRUCTURES & FILTERING
# ---------------------------------------------------------

# Problem 8: The Storage Container
# You will be reading multiple rows of data and need to save the valid names.
# Create an empty list named `valid_names`.

# Problem 9: Mock Extraction
# Imagine you just processed a line of input.
# Set `mock_name = "samantha"` and `mock_email = "samantha@gmail.com"`.

# Problem 10: Conditional Regex
# Write an `if` statement that checks if `re.search()` finds a match in `mock_email` 
# using your `regex_pattern`. 

# Problem 11: Appending to the List
# Inside that `if` block, append the `mock_name` to your `valid_names` list.
# Mock Output of valid_names: ['samantha']

# Problem 12: Invalid Extraction Test
# Repeat problems 9-11 mentally with `mock_name = "julia"` and `mock_email = "julia@julia.me"`.
# The regex will return None, the `if` block will not trigger, and the list won't change.

# ---------------------------------------------------------
# PHASE 3: SORTING & OUTPUTTING
# ---------------------------------------------------------

# Problem 13: The Unsorted List
# Create a hardcoded list of names to simulate a completed extraction process.
# `unsorted_names = ["tanya", "julia", "samantha", "julia", "riya"]`

# Problem 14: Alphabetical Sorting
# Use Python's built-in sorting method or function to sort `unsorted_names` 
# in standard alphabetical order. Save or modify it to be sorted.
# Mock Output: ['julia', 'julia', 'riya', 'samantha', 'tanya']

# Problem 15: The Output Loop
# Write a `for` loop that iterates over your newly sorted list of names.

# Problem 16: Printing Line by Line
# Inside the loop, print each name. Since standard `print()` adds a newline automatically, 
# this will correctly print one name per line.

# ---------------------------------------------------------
# PHASE 4: INTEGRATING WITH HACKERRANK'S PRECODE
# ---------------------------------------------------------

# Problem 17: Analyzing the N-Loop
# Look at the precode provided: `for N_itr in range(N):`
# This loop handles reading the data row by row. 
# Concept: Should your `valid_names` list be created INSIDE or OUTSIDE this loop? 
# (Hint: If it's inside, it will overwrite itself on every row).

# Problem 18: Placement of Regex Check
# The variables `firstName` and `emailID` are generated INSIDE the precode's loop.
# Concept: Your `re.search()` and `.append()` logic must go inside this loop 
# so it can evaluate every single row as it comes in.

# Problem 19: Placement of the Sort
# You cannot sort the list until ALL rows have been processed.
# Concept: Your sorting logic must be placed OUTSIDE and AFTER the `N` loop.

# Problem 20: Placement of the Print Loop
# You must print the names after they are fully gathered and sorted.
# Concept: Your `for` loop that prints the names must also be placed OUTSIDE 
# and AFTER the `N` loop.

# ==============================================================================
# FINAL SUBMISSION
# ==============================================================================
# Summary:
# By defining a regex pattern with an escaped literal dot and an end-of-string 
# anchor, you can accurately filter the incoming emails. Storing the valid names 
# in a list outside the main input loop allows you to sort and print them 
# sequentially once all input has been fully parsed.
#
# Mock Input (Stdin):
# 6
# riya riya@gmail.com
# julia julia@julia.me
# julia sjulia@gmail.com
# julia julia@gmail.com
# samantha samantha@gmail.com
# tanya tanya@gmail.com
#
# Expected Output:
# julia
# julia
# riya
# samantha
# tanya
# ==============================================================================