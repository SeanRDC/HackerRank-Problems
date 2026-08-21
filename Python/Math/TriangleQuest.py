# ==============================================================================
# FUNDAMENTALS CURRICULUM: PURE ARITHMETIC PATTERNS
# ==============================================================================
# Goal: Print a repeating number sequence (1, 22, 333) dependent on a loop 
# variable 'i', without using ANY string manipulation, in a single line of code.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: REVERSE-ENGINEERING THE PATTERN
# ---------------------------------------------------------

# Problem 1: The Outputs
# Concept: Let's look at the desired sequence for i=1, 2, 3, and 4.
# Outputs: 1, 22, 333, 4444. 

# Problem 2: Factoring the Second Step
# Concept: Mathematically factor the second output (22) using the variable `i` (2).
# 22 = 2 * 11.

# Problem 3: Factoring the Third Step
# Concept: Factor the third output (333) using the variable `i` (3).
# 333 = 3 * 111.

# Problem 4: The Universal Rule
# Concept: We can see a pattern emerging. The output for any step `i` is simply 
# `i` multiplied by a sequence of ones (1, 11, 111, 1111).
# Formula so far: Output = i * (Sequence of Ones)

# ---------------------------------------------------------
# CONCEPT BLOCK 2: GENERATING THE ONES (THE 9s METHOD)
# ---------------------------------------------------------

# Problem 5: The Challenge
# Concept: How do we generate 1, 11, 111 mathematically using `i`? 
# It's difficult to jump straight to 1s. Let's aim for 9s first: 9, 99, 999.

# Problem 6: Powers of 10
# Concept: How do 9, 99, and 999 relate to powers of 10?
# 10^1 = 10. 10^2 = 100. 10^3 = 1000.

# Problem 7: Subtracting 1
# Concept: If we take 10 to the power of `i`, and subtract 1, what happens?
# i=1: 10 - 1 = 9
# i=2: 100 - 1 = 99
# i=3: 1000 - 1 = 999

# Problem 8: Converting 9s to 1s
# Concept: Now that we have 9, 99, and 999, how do we turn them into 1s?
# Divide them by 9! 
# (9 / 9 = 1), (99 / 9 = 11), (999 / 9 = 111).

# Problem 9: The Pure Math Formula
# Concept: Combine Problems 7 and 8 into a mathematical formula.
# Sequence of Ones = (10^i - 1) / 9.

# ---------------------------------------------------------
# CONCEPT BLOCK 3: THE PYTHON OPTIMIZATION
# ---------------------------------------------------------

# Problem 10: Floor Division Magic
# Concept: Python's integer division (`//`) automatically drops decimals. 
# Do we actually need to subtract 1 first? Let's test it.

# Problem 11: Testing i=1
# Concept: Calculate 10^1 // 9. 
# 10 // 9 = 1. (It drops the .111... remainder).

# Problem 12: Testing i=2
# Concept: Calculate 10^2 // 9.
# 100 // 9 = 11. (It drops the .111... remainder).

# Problem 13: Testing i=3
# Concept: Calculate 10^3 // 9.
# 1000 // 9 = 111. 

# Problem 14: The Simplified Expression
# Concept: Thanks to integer division, we don't even need to subtract 1! 
# The Python expression to generate the ones is simply: `(10 ** i) // 9`.

# ---------------------------------------------------------
# CONCEPT BLOCK 4: ASSEMBLING THE MATH
# ---------------------------------------------------------

# Problem 15: Putting it Together
# Concept: Take your universal rule from Problem 4, and swap in the Python 
# expression from Problem 14. 
# Equation: `((10 ** i) // 9) * i`

# Problem 16: The Final Desk Check
# Concept: Test your full equation manually for i = 4.
# 10 ** 4 = 10000.
# 10000 // 9 = 1111.
# 1111 * 4 = 4444. It is flawless!

# ---------------------------------------------------------
# CONCEPT BLOCK 5: HACKERRANK INTEGRATION
# ---------------------------------------------------------

# Problem 17: The Provided Boilerplate
# Concept: HackerRank locks the first line: `for i in range(1, int(input())):`
# This handles reading the input and setting up the loop for you.

# Problem 18: The Single Line Constraint
# Concept: You are only allowed ONE line inside this loop. 
# You cannot declare intermediate variables. 

# Problem 19: The Print Function
# Concept: Wrap your entire mathematical equation from Problem 15 directly 
# inside a `print()` function.

# Problem 20: Execution
# Concept: Add your single `print()` statement beneath the locked `for` loop, 
# ensuring it is properly indented. You have just solved a complex pattern 
# using zero strings!

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Loop Setup ---
# Locked boilerplate receives string "5".
# int() casts it: 5
# range(1, 5) generates loop variables: 1, 2, 3, 4.

# --- Loop Iteration 1 (i=1) ---
# Evaluates: (10 ** 1) // 9 * 1
# Becomes: 10 // 9 * 1
# Becomes: 1 * 1
# Console Prints: 1

# --- Loop Iteration 2 (i=2) ---
# Evaluates: (10 ** 2) // 9 * 2
# Becomes: 100 // 9 * 2
# Becomes: 11 * 2
# Console Prints: 22

# --- Loop Iteration 3 (i=3) ---
# Evaluates: (10 ** 3) // 9 * 3
# Becomes: 1000 // 9 * 3
# Becomes: 111 * 3
# Console Prints: 333

# --- Loop Iteration 4 (i=4) ---
# Evaluates: (10 ** 4) // 9 * 4
# Becomes: 10000 // 9 * 4
# Becomes: 1111 * 4
# Console Prints: 4444
for i in range(1, int(input())):
    print(((10 ** i) // 9) * i)