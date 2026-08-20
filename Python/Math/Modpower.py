# ==============================================================================
# FUNDAMENTALS CURRICULUM: POWERS & MODULAR EXPONENTIATION
# ==============================================================================
# Goal: Read three integers a, b, and m on separate lines. Output the result of 
# a to the power of b on the first line, and (a^b) modulo m on the second line.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: BASIC EXPONENTIATION
# ---------------------------------------------------------

# Problem 1: The Mock Variables
# Concept: Create three integer variables representing the HackerRank sample data.
# `a = 3`, `b = 4`, and `m = 5`.
a = 3
b = 4
m = 5
# Problem 2: The Double Asterisk Operator
# Concept: In Python, you can calculate powers using the `**` operator.
# Calculate `a ** b` and print the result.
# Mock Output: 81
print(a ** b)
# Problem 3: The Built-in 2-Argument pow()
# Concept: Python also provides a built-in function `pow()`. 
# Pass `a` and `b` as two arguments to `pow()` and print the result.
# Mock Output: 81
# (For two arguments, `a ** b` and `pow(a, b)` do the exact same thing!)
print(pow(a, b))
# ---------------------------------------------------------
# CONCEPT BLOCK 2: THE MATH MODULE TRAP
# ---------------------------------------------------------

# Problem 4: The Import
# Concept: Python has a separate `math` module that also contains a power function.
# Write `import math`.
import math
# Problem 5: math.pow()
# Concept: Use `math.pow(a, b)` and print the result.
# Mock Output: 81.0
print(math.pow(a, b))
# Problem 6: The Float Difference
# Concept: Notice the decimal? The `math.pow()` function converts inputs to 
# floats and returns a float. The built-in `pow()` strictly returns integers 
# if the inputs are integers. We need integers here, so we will NOT use `math`.

# ---------------------------------------------------------
# CONCEPT BLOCK 3: MODULAR EXPONENTIATION (THE NAIVE WAY)
# ---------------------------------------------------------

# Problem 7: The Modulo Refresher
# Concept: We need the remainder of our power divided by `m`.
# Calculate the power of `a` and `b` using `**`, then modulo the whole thing 
# by `m`. Example: `(a ** b) % m`. Print the result.
# Mock Output: 1 (Because 81 % 5 leaves a remainder of 1).

# Problem 8: The Hidden Memory Trap
# Concept: What if `a` was 10000 and `b` was 50000? 
# `10000 ** 50000` is a number with 200,000 zeros! Calculating that massive 
# integer in memory just to find its modulo will crash your program or hit a 
# Time Limit Exceeded (TLE) error on HackerRank.

# ---------------------------------------------------------
# CONCEPT BLOCK 4: THE 3-ARGUMENT POW() MAGIC
# ---------------------------------------------------------

# Problem 9: The Optimized Built-in
# Concept: The built-in `pow()` function actually accepts an optional 3rd argument!
# When you provide `pow(a, b, m)`, Python does NOT calculate the massive integer 
# first. Instead, it performs the modulo operation step-by-step during the 
# exponentiation. It uses a fraction of the memory and is lightning fast.

# Problem 10: Testing the 3-Argument pow()
# Concept: Pass `a`, `b`, and `m` into `pow()` and print the result.
# Mock Output: 1

# Problem 11: The Constraint Check
# Concept: The 3-argument `pow()` has a strict rule: if the third argument is 
# present, the power (`b`) CANNOT be negative. Try `pow(3, -4, 5)`.
# Mock Output: ValueError: pow() 2nd argument cannot be negative when 3rd argument specified

# ---------------------------------------------------------
# CONCEPT BLOCK 5: INPUT ARCHITECTURE
# ---------------------------------------------------------

# Problem 12: Reading the First Line
# Concept: Call `input()`, wrap it in `int()`, and assign it to `a`.

# Problem 13: Reading the Second Line
# Concept: Call `input()`, wrap it in `int()`, and assign it to `b`.

# Problem 14: Reading the Third Line
# Concept: Call `input()`, wrap it in `int()`, and assign it to `m`.
# (No need for `split()` since they are on three entirely separate lines).

# ---------------------------------------------------------
# CONCEPT BLOCK 6: FINAL ASSEMBLY PREP
# ---------------------------------------------------------

# Problem 15: The First Output Line
# Concept: You need to print the result of `a` to the power of `b`.
# Use either `**` or the 2-argument `pow()`.

# Problem 16: The Second Output Line
# Concept: You need to print the result of `a` to the power of `b`, modulo `m`.
# Do NOT use `(a ** b) % m`. Use the optimized 3-argument `pow()` function!

# Problem 17-20: Clean Code Optimization
# Concept: Assemble your final 5-line script. Three lines for reading inputs, 
# and two lines for printing the mathematical results.

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- The Initial Inputs ---
# 1st input() receives string: "3"
# int() casts it: a = 3
#
# 2nd input() receives string: "4"
# int() casts it: b = 4
#
# 3rd input() receives string: "5"
# int() casts it: m = 5

# --- Output Line 1 (Standard Power) ---
# Evaluates: pow(3, 4)
# Console Prints: 81

# --- Output Line 2 (Modular Exponentiation) ---
# Evaluates: pow(3, 4, 5) 
# Note: Calculates (3*3 % 5 * 3 % 5 * 3 % 5) internally under the hood.
# Console Prints: 1