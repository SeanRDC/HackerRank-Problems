# ==============================================================================
# FUNDAMENTALS CURRICULUM: ANY, ALL, & SHORT-CIRCUIT EVALUATION
# ==============================================================================
# Goal: Read a list of numbers. Check if ALL numbers are positive. If they are, 
# check if ANY number is a palindrome. Output True or False in 3 lines or less.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: THE ALL() FUNCTION & GENERATORS
# ---------------------------------------------------------

# Problem 1: The Mock List (Integers)
# Concept: Create a mock list of integers.
# `nums = [12, 9, 61, 5, 14]`

# Problem 2: The Boolean Generator
# Concept: We need to know if every number is greater than zero.
# Write a generator expression: `(n > 0 for n in nums)`. 
# (Remember from our combinations challenge, generators save memory!)

# Problem 3: The all() Function
# Concept: Pass that generator directly into the `all()` function and print it.
# `print(all(n > 0 for n in nums))`
# Mock Output: True (Because every single number is positive).

# Problem 4: The False Trigger
# Concept: Change the `12` in your list to `-12`. Run Problem 3 again.
# Mock Output: False (Because `all()` immediately fails if it sees even one False).

# ---------------------------------------------------------
# CONCEPT BLOCK 2: STRING REVERSAL (THE PALINDROME TRICK)
# ---------------------------------------------------------

# Problem 5: The String Casting
# Concept: To check if a number is a palindrome (reads the same forwards and 
# backwards), it is much easier to treat it as a string!
# Create a string: `s = "12321"`

# Problem 6: The Slice Reversal
# Concept: In Python, you can reverse a string instantly using slicing syntax: 
# `[::-1]`. Print `s[::-1]`.
# Mock Output: '12321'

# Problem 7: The Equality Check
# Concept: Check if the string equals its reversed self: `print(s == s[::-1])`.
# Mock Output: True

# ---------------------------------------------------------
# CONCEPT BLOCK 3: THE ANY() FUNCTION
# ---------------------------------------------------------

# Problem 8: The Mock List (Strings)
# Concept: Let's look at HackerRank's actual input format. They provide strings!
# `str_nums = ["12", "9", "61", "5", "14"]`

# Problem 9: The Palindrome Generator
# Concept: Write a generator expression checking if each string equals its reverse.
# `(s == s[::-1] for s in str_nums)`

# Problem 10: The any() Function
# Concept: Pass that generator into `any()` and print it.
# `print(any(s == s[::-1] for s in str_nums))`
# Mock Output: True (Because "9" and "5" are palindromes. `any()` stops and 
# returns True the moment it finds a single match!)

# ---------------------------------------------------------
# CONCEPT BLOCK 4: THE BOOLEAN SHORT-CIRCUIT (CRITICAL LOGIC)
# ---------------------------------------------------------

# Problem 11: The 'AND' Operator
# Concept: HackerRank wants to know if Condition 1 AND Condition 2 are true.
# Write: `True and True`. (Evaluates to True)

# Problem 12: The Short-Circuit Rule
# Concept: If you write `False and True`, Python is smart. It sees the `False`, 
# knows the whole statement can NEVER be True, and completely skips evaluating 
# the second half! This is called "short-circuiting."

# Problem 13: Order Matters
# Concept: HackerRank says: "If all integers are positive, THEN check if any 
# is a palindrome." 
# This means your `all()` check MUST go on the left side of the `and` operator! 
# If it fails, the `any()` check never runs, saving processing power.

# ---------------------------------------------------------
# CONCEPT BLOCK 5: INPUT ARCHITECTURE (THE 3-LINE CHALLENGE)
# ---------------------------------------------------------

# Problem 14: The Throwaway Line
# Concept: Line 1 of the challenge is `N`. We don't actually need it for our logic! 
# Use the throwaway variable: `_ = input()`. (That's Line 1 of your script done).

# Problem 15: Reading the Array
# Concept: Read Line 2. Simply use `input().split()`. 
# Assign it to a variable `arr`. (That's Line 2 done).

# Problem 16: The Data Type Strategy
# Concept: Notice we did NOT use `map(int)` in Problem 15! 
# Keep the inputs as strings! It makes the palindrome check `s == s[::-1]` 
# effortless.

# ---------------------------------------------------------
# CONCEPT BLOCK 6: FINAL ASSEMBLY PREP
# ---------------------------------------------------------

# Problem 17: The First Generator (Int Casting)
# Concept: Because `arr` contains strings, your `all()` generator must cast 
# them to integers temporarily just to check if they are positive: 
# `all(int(i) > 0 for i in arr)`

# Problem 18: The Second Generator (String Slicing)
# Concept: Your `any()` generator can just use the strings directly!
# `any(i == i[::-1] for i in arr)`

# Problem 19: The Master Equation
# Concept: Combine Problem 17 and Problem 18 using the `and` operator.

# Problem 20: The One-Line Print
# Concept: Wrap the entire master equation in a single `print()` statement. 
# (That's Line 3 done. Challenge complete!)

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Input Parsing (Lines 1 & 2) ---
# _ = input() reads "5" and discards it.
# arr = input().split() reads the string and generates:
# arr = ["12", "9", "61", "5", "14"]

# --- Evaluation Step 1: all() ---
# Generator casts to int and checks > 0:
# int("12") > 0 -> True
# int("9") > 0 -> True
# int("61") > 0 -> True
# int("5") > 0 -> True
# int("14") > 0 -> True
# all() returns: True

# --- The AND Operator (Short-Circuit Check) ---
# Left side is True. The `and` operator MUST evaluate the right side to be sure.

# --- Evaluation Step 2: any() ---
# Generator checks string reversal:
# "12" == "21" -> False
# "9" == "9" -> True
# any() finds a True! It immediately stops iterating and returns: True

# --- Final Output (Line 3) ---
# True and True evaluates to: True
# Console Prints: True