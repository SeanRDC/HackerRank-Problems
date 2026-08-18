# ==============================================================================
# FUNDAMENTALS CURRICULUM: EXCEPTION HANDLING & ERROR CATCHING
# ==============================================================================
# Goal: Parse paired string inputs, convert them to integers, and perform integer 
# division. If the conversion fails (ValueError) or the division attempts to 
# divide by zero (ZeroDivisionError), catch the crash and print the error code.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: INTEGER DIVISION
# ---------------------------------------------------------

# Problem 1: The Mock Variables
# Concept: Create two integer variables: `num1 = 3` and `num2 = 1`.

# Problem 2: Python 3 Integer Division
# Concept: In Python 3, a single slash `/` returns a float (3.0). 
# A double slash `//` forces integer division (3). 
# Print the result of `num1` integer divided by `num2`.
# Mock Output: 3

# ---------------------------------------------------------
# CONCEPT BLOCK 2: THE ZERODIVISIONERROR
# ---------------------------------------------------------

# Problem 3: The Crash
# Concept: Change `num2` to `0`. Try to print `num1 // num2` again.
# Mock Output: ZeroDivisionError: integer division or modulo by zero
# Notice how the entire script instantly crashes and stops running!

# Problem 4: The Safety Net (Try/Except)
# Concept: Wrap your division code inside a `try:` block. 
# Directly below it, write an `except ZeroDivisionError:` block that simply 
# prints the string "Math failed!". Run it. 
# Mock Output: Math failed! (Notice the script didn't crash this time!)

# Problem 5: The Exception Object
# Concept: We need the exact error message provided by Python. 
# Modify your except line to read: `except ZeroDivisionError as e:`
# Inside the except block, print the variable `e`.
# Mock Output: integer division or modulo by zero

# ---------------------------------------------------------
# CONCEPT BLOCK 3: THE VALUEERROR (THE MAPPING TRAP)
# ---------------------------------------------------------

# Problem 6: The String Input
# Concept: HackerRank provides inputs as strings. 
# Create mock string variables: `str1 = "2"` and `str2 = "$"`.

# Problem 7: The Conversion Crash
# Concept: Try to convert `str2` using `int()`. 
# Mock Output: ValueError: invalid literal for int() with base 10: '$'
# Notice this crashes before any math even happens!

# Problem 8: The Parsing Safety Net
# Concept: Wrap the `int()` conversion of `str1` and `str2` inside a new `try:` 
# block. Catch it with `except ValueError as e:` and print `e`.
# Mock Output: invalid literal for int() with base 10: '$'

# ---------------------------------------------------------
# CONCEPT BLOCK 4: STACKING EXCEPTIONS
# ---------------------------------------------------------

# Problem 9: The Unified Block
# Concept: You can stack multiple `except` blocks under a single `try` block!
# Write one `try:` block. Inside it, convert `str1` and `str2` to integers, 
# then print their integer division.

# Problem 10: Adding the Handlers
# Concept: Below the `try` block from Problem 9, add BOTH of your except 
# blocks: `except ZeroDivisionError as e:` AND `except ValueError as e:`. 
# Have them both print `e`.

# Problem 11: Testing the Zero Trap
# Concept: Set your mock strings to `"1"` and `"0"`. Run your unified block.
# Mock Output: integer division or modulo by zero

# Problem 12: Testing the Value Trap
# Concept: Set your mock strings to `"2"` and `"$"`. Run your unified block.
# Mock Output: invalid literal for int() with base 10: '$'

# ---------------------------------------------------------
# CONCEPT BLOCK 5: OUTPUT FORMATTING
# ---------------------------------------------------------

# Problem 13: The Custom Error String
# Concept: HackerRank wants the output to explicitly say "Error Code: " before 
# the actual error message. Inside your except blocks, print an f-string or 
# concatenated string that matches this exact format.
# Mock Output: Error Code: integer division or modulo by zero

# ---------------------------------------------------------
# CONCEPT BLOCK 6: INPUT ARCHITECTURE
# ---------------------------------------------------------

# Problem 14: Reading T
# Concept: The first input is the number of test cases. Read it and convert 
# it to an integer `T`.

# Problem 15: The Outer Loop
# Concept: Write a `for` loop that iterates `T` times.

# Problem 16: Reading the Row
# Concept: Inside the loop, read the next line using `input().split()`. 
# Assign the result to a list called `elements`.
# Why not `map(int)` right away? Because if you map to an integer outside the 
# `try` block, a ValueError will crash your script instantly! 

# Problem 17: Extracting Variables
# Concept: Assign `elements[0]` to a variable `a`, and `elements[1]` to `b`. 
# (They are still strings at this point).

# ---------------------------------------------------------
# CONCEPT BLOCK 7: FINAL ASSEMBLY PREP
# ---------------------------------------------------------

# Problem 18: Entering the Danger Zone
# Concept: Inside your loop, open your `try:` block.

# Problem 19: Safe Conversion & Execution
# Concept: Inside the `try` block, safely convert `a` and `b` to integers 
# and immediately print their integer division.

# Problem 20: The Dual Catch
# Concept: Add your two `except` blocks (ZeroDivisionError and ValueError) 
# underneath, ensuring they print the formatted "Error Code:" message!

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- The Initial Input ---
# input() receives: "3"
# T evaluates to: 3

# --- Test Case Loop 1 ---
# input().split() receives: "1 0"
# Variables extracted: a = "1", b = "0" (Both Strings)
# 
# ENTER TRY BLOCK:
#   Conversion: "1" -> 1, "0" -> 0 (Success!)
#   Math: 1 // 0 (CRASH! ZeroDivisionError triggered)
# 
# ENTER EXCEPT BLOCK (ZeroDivisionError):
#   Catches error object 'e'
#   Console Prints: Error Code: integer division or modulo by zero

# --- Test Case Loop 2 ---
# input().split() receives: "2 $"
# Variables extracted: a = "2", b = "$" (Both Strings)
#
# ENTER TRY BLOCK:
#   Conversion: "2" -> 2, "$" -> int("$") (CRASH! ValueError triggered)
#   Math: Skipped entirely due to early crash.
#
# ENTER EXCEPT BLOCK (ValueError):
#   Catches error object 'e'
#   Console Prints: Error Code: invalid literal for int() with base 10: '$'

# --- Test Case Loop 3 ---
# input().split() receives: "3 1"
# Variables extracted: a = "3", b = "1" (Both Strings)
#
# ENTER TRY BLOCK:
#   Conversion: "3" -> 3, "1" -> 1 (Success!)
#   Math: 3 // 1 -> evaluates to 3 (Success!)
#   Console Prints: 3
#
# EXCEPT BLOCKS: Skipped entirely.