# ==============================================================================
# FUNDAMENTALS CURRICULUM: PALINDROMIC MATH & DEMLO NUMBERS
# ==============================================================================
# Goal: Print a palindromic number sequence (1, 121, 12321) dependent on a loop 
# variable 'i', without using ANY strings, in a single line of code.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: REVERSE-ENGINEERING THE PALINDROMES
# ---------------------------------------------------------

# Problem 1: The Outputs
# Concept: Let's look at the desired sequence for i=1, 2, 3, and 4.
# Outputs: 1, 121, 12321, 1234321.

# Problem 2: Factoring the Second Step
# Concept: Mathematically factor the second output (121). What times itself 
# equals 121? (Hint: Find its square root).
# 11 * 11 = 121.

# Problem 3: Factoring the Third Step
# Concept: Mathematically factor the third output (12321). What times itself 
# equals 12321? 
# 111 * 111 = 12321.

# Problem 4: The Demlo Number Rule
# Concept: We have discovered a famous mathematical sequence! These are known 
# as Demlo numbers. The output for any step `i` is simply a sequence of ones 
# (of length `i`) multiplied by itself!
# Formula so far: Output = (Sequence of Ones) ** 2

# ---------------------------------------------------------
# CONCEPT BLOCK 2: THE RETURN OF THE ONES
# ---------------------------------------------------------

# Problem 5: The Callback
# Concept: In the previous challenge, we figured out how to generate a sequence 
# of ones (1, 11, 111) mathematically.

# Problem 6: The Powers of 10 Refresher
# Concept: Remember that `10 ** i` gives us 10, 100, 1000.

# Problem 7: The Python Floor Division Magic
# Concept: Remember that dividing those powers of 10 by 9 using Python's `//` 
# operator magically dropped the remainder and gave us our ones!

# Problem 8: Testing i=1
# Concept: (10 ** 1) // 9 evaluates to 10 // 9. 
# Result: 1.

# Problem 9: Testing i=2
# Concept: (10 ** 2) // 9 evaluates to 100 // 9. 
# Result: 11.

# Problem 10: The Reused Formula
# Concept: The expression to generate the ones is exactly the same as before: 
# `(10 ** i) // 9`.

# ---------------------------------------------------------
# CONCEPT BLOCK 3: ASSEMBLING THE NEW MATH
# ---------------------------------------------------------

# Problem 11: Putting it Together
# Concept: Take your universal rule from Problem 4, and swap in the Python 
# expression from Problem 10. 
# Equation: `((10 ** i) // 9) ** 2`

# Problem 12: The Parentheses Warning
# Concept: Order of operations matters immensely here! If you wrote 
# `(10 ** i) // 9 ** 2`, Python would calculate 9 squared first (81). 
# You MUST wrap the entire sequence generation in parentheses before squaring it.

# Problem 13: The Final Desk Check (i = 3)
# Concept: Test your full equation manually for i = 3.
# 10 ** 3 = 1000.
# 1000 // 9 = 111.
# 111 ** 2 = 12321. It works perfectly!

# Problem 14: The Final Desk Check (i = 4)
# Concept: Test it manually for i = 4.
# 10 ** 4 = 10000.
# 10000 // 9 = 1111.
# 1111 ** 2 = 1234321. Flawless!

# ---------------------------------------------------------
# CONCEPT BLOCK 4: HACKERRANK INTEGRATION
# ---------------------------------------------------------

# Problem 15: The Provided Boilerplate
# Concept: Just like before, HackerRank locks the first line: 
# `for i in range(1, int(input())+1):`
# Note the `+1` here—HackerRank adjusts the range bounds slightly differently 
# in this problem compared to the last, but the logic remains identical!

# Problem 16: The Constraints Checklist
# Concept: Did we use strings? No. Did we use more than one for-loop? No. 
# Did we use pure arithmetic? Yes.

# Problem 17: The Single Line Execution
# Concept: We are only allowed ONE line inside this loop. 

# Problem 18: The Print Function
# Concept: Wrap your entire mathematical equation from Problem 11 directly 
# inside a `print()` function.

# Problem 19: Formatting Check
# Concept: Ensure your `print()` statement is properly indented inside the loop.

# Problem 20: Victory
# Concept: You have successfully solved a complex string manipulation problem 
# using nothing but the raw power of mathematics!

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Loop Setup ---
# Locked boilerplate receives string "5".
# int() casts it: 5
# range(1, 5+1) generates loop variables: 1, 2, 3, 4, 5.

# --- Loop Iteration 1 (i=1) ---
# Generates Ones: (10 ** 1) // 9 -> 1
# Squares Sequence: 1 ** 2
# Console Prints: 1

# --- Loop Iteration 2 (i=2) ---
# Generates Ones: (10 ** 2) // 9 -> 11
# Squares Sequence: 11 ** 2
# Console Prints: 121

# --- Loop Iteration 3 (i=3) ---
# Generates Ones: (10 ** 3) // 9 -> 111
# Squares Sequence: 111 ** 2
# Console Prints: 12321

# --- Loop Iteration 4 (i=4) ---
# Generates Ones: (10 ** 4) // 9 -> 1111
# Squares Sequence: 1111 ** 2
# Console Prints: 1234321

# --- Loop Iteration 5 (i=5) ---
# Generates Ones: (10 ** 5) // 9 -> 11111
# Squares Sequence: 11111 ** 2
# Console Prints: 123454321

for i in range(1, int(input())):
    print(((10 ** i) // 9) ** 2)