# ==============================================================================
# FUNDAMENTALS CURRICULUM: REGEX VALIDATION & MODULE EXCEPTIONS
# ==============================================================================
# Goal: Take a raw string and test if it is a mathematically valid Regular 
# Expression. We will do this by attempting to compile it using the `re` module, 
# catching the specific module error if it fails, and outputting True or False.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: THE RE MODULE & COMPILATION
# ---------------------------------------------------------

# Problem 1: The Import
# Concept: We need Python's built-in regular expression module. 
# Write the statement to import `re`.
import re
# Problem 2: The Valid Mock String
# Concept: Create a mock string representing a valid regex pattern.
# `valid_pattern = ".*\+"`
valid_pattern = r".*\+"
# Problem 3: Compiling the Pattern
# Concept: The engine checks if a regex is valid by "compiling" it. 
# Pass `valid_pattern` into `re.compile()` and assign it to `compiled_obj`. 
# Print it. 
# Mock Output: re.compile('.*\\+') (It successfully built an object!)
compiled_obj = re.compile(valid_pattern)
print(compiled_obj)
# ---------------------------------------------------------
# CONCEPT BLOCK 2: THE RE.ERROR EXCEPTION
# ---------------------------------------------------------

# Problem 4: The Invalid Mock String
# Concept: Create a mock string representing an invalid pattern.
# `invalid_pattern = ".*+"`

# Problem 5: The Crash
# Concept: Try to pass `invalid_pattern` into `re.compile()`. 
# Mock Output: re.error: multiple repeat at position 2
# Notice how the compilation immediately crashes because the math makes no sense!

# Problem 6: The Specific Exception
# Concept: Just like ZeroDivisionError, the `re` module has its own specific 
# crash object called `re.error`. We need to use this for our safety net.

# ---------------------------------------------------------
# CONCEPT BLOCK 3: BOOLEAN ERROR CATCHING
# ---------------------------------------------------------

# Problem 7: The Try Block
# Concept: Open a `try:` block. Inside, attempt to compile `invalid_pattern`.

# Problem 8: The Success State
# Concept: If `re.compile()` succeeds, the pattern is valid! 
# Directly underneath your compile statement inside the try block, print `True`.

# Problem 9: The Except Block
# Concept: Create your `except` block specifically targeting `re.error`.

# Problem 10: The Failure State
# Concept: If the `except` block triggers, the pattern is mathematically broken.
# Inside the except block, print `False`.
# Run this entire block against `invalid_pattern`.
# Mock Output: False

# Problem 11: Testing the Success State
# Concept: Swap the variable in your try block to `valid_pattern` and run it again.
# Mock Output: True

# ---------------------------------------------------------
# CONCEPT BLOCK 4: INPUT ARCHITECTURE & EDGE CASES
# ---------------------------------------------------------

# Problem 12: Reading T
# Concept: The first input is the number of test cases. Read it and convert 
# it to an integer `T`.

# Problem 13: The Outer Loop
# Concept: Write a `for` loop that iterates `T` times using the throwaway `_`.

# Problem 14: The Trailing Space Danger
# Concept: Should we use `input().split()` here? NO! 
# Regular expressions can intentionally contain spaces! If you split it, you 
# will destroy the pattern. 

# Problem 15: Reading the Raw Pattern
# Concept: Inside your loop, simply use `input()` to read the exact raw string, 
# spaces and all. Assign it to a variable called `pattern`.

# ---------------------------------------------------------
# CONCEPT BLOCK 5: FINAL ASSEMBLY PREP
# ---------------------------------------------------------

# Problem 16: The Verification Function (Clean Code Practice)
# Concept: Create a function called `is_valid_regex(pattern)` to house your logic.

# Problem 17: Moving the Logic
# Concept: Move your `try`/`except` block from Problems 7-10 inside this function.

# Problem 18: Return vs Print
# Concept: Inside the function, change `print(True)` to `return True`, and 
# `print(False)` to `return False`. 

# Problem 19: The Execution
# Concept: Inside your `T` loop, call your function, passing in the `pattern` 
# you just read from `input()`.

# Problem 20: The Final Output
# Concept: Wrap your function call in a `print()` statement so the boolean 
# result gets printed to the HackerRank console!

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- The Initial Input ---
# input() receives: "2"
# T evaluates to: 2

# --- Test Case Loop 1 ---
# input() receives raw string: ".*\+"
# Variable `pattern` evaluates to: ".*\+"
# 
# Function `is_valid_regex()` receives ".*\+"
# ENTER TRY BLOCK:
#   Compilation: re.compile(".*\+") (Success! Object created)
#   Returns: True
# 
# Console Prints: True

# --- Test Case Loop 2 ---
# input() receives raw string: ".*+"
# Variable `pattern` evaluates to: ".*+"
#
# Function `is_valid_regex()` receives ".*+"
# ENTER TRY BLOCK:
#   Compilation: re.compile(".*+") (CRASH! re.error triggered by multiple repeats)
#   Return True is skipped.
#
# ENTER EXCEPT BLOCK (re.error):
#   Catches the module-specific error.
#   Returns: False
#
# Console Prints: False