# ==============================================================================
# FUNDAMENTALS CURRICULUM: ARBITRARY-PRECISION INTEGERS
# ==============================================================================
# Goal: Read four integers a, b, c, and d on separate lines. Output the result  
# of (a to the power of b) added to (c to the power of d).
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: THE C++ LIMITATION VS PYTHON
# ---------------------------------------------------------

# Problem 1: The Mock Variables
# Concept: Create four integer variables representing the HackerRank sample data.
# `a = 9`, `b = 29`, `c = 7`, and `d = 27`.
a = 9
b = 29
c = 7
d = 27
# Problem 2: The 64-bit Limit
# Concept: In C++, the absolute maximum value for an unsigned 64-bit integer 
# is 18,446,744,073,709,551,615. Keep this number in mind!

# ---------------------------------------------------------
# CONCEPT BLOCK 2: THE FIRST POWER (a^b)
# ---------------------------------------------------------

# Problem 3: Calculating a^b
# Concept: We need to calculate `a` to the power of `b`.
# You can use either `a ** b` or `pow(a, b)`. Assign this to a variable `power1`.
power1 = pow(a, b)
# Problem 4: Printing the First Power
# Concept: Print `power1`.
# Mock Output: 717897987691852588770249
# Notice that this number ALREADY exceeds the 64-bit C++ limit mentioned in 
# Problem 2, yet Python handled it instantly without throwing an OverflowError!
print(power1)
# ---------------------------------------------------------
# CONCEPT BLOCK 3: THE SECOND POWER (c^d)
# ---------------------------------------------------------

# Problem 5: Calculating c^d
# Concept: We need to calculate `c` to the power of `d`.
# Assign the result of `c ** d` (or `pow(c, d)`) to a variable `power2`.
power2 = pow(c, d)
# Problem 6: Printing the Second Power
# Concept: Print `power2`.
# Mock Output: 3991196420839079204482643
# Another massive number processed flawlessly.
print(power2)
# ---------------------------------------------------------
# CONCEPT BLOCK 4: COMBINING MASSIVE INTEGERS
# ---------------------------------------------------------

# Problem 7: The Addition
# Concept: We need to add our two massive integers together.
# Create a variable `total` and set it equal to `power1 + power2`.
total = power1 + power2
# Problem 8: The Final Output
# Concept: Print the `total` variable.
# Mock Output: 4710194409608608369201743232
# You just performed math on a 28-digit integer natively. 
print(total)
# ---------------------------------------------------------
# CONCEPT BLOCK 5: INPUT ARCHITECTURE
# ---------------------------------------------------------

# Problem 9: The Input Trap (Revisited)
# Concept: Look at the HackerRank "Sample Input". 
# 9, 29, 7, and 27 are all on completely separate lines.
# This means `input().split()` will fail.

# Problem 10: Reading 'a'
# Concept: Call `input()` by itself, wrap it in `int()`, and assign it to `a`.
a = int(input())
# Problem 11: Reading 'b'
# Concept: Call `input()` by itself, wrap it in `int()`, and assign it to `b`.
b = int(input())
# Problem 12: Reading 'c'
# Concept: Call `input()` by itself, wrap it in `int()`, and assign it to `c`.
c = int(input())
# Problem 13: Reading 'd'
# Concept: Call `input()` by itself, wrap it in `int()`, and assign it to `d`.
d = int(input())
# ---------------------------------------------------------
# CONCEPT BLOCK 6: FINAL ASSEMBLY PREP
# ---------------------------------------------------------

# Problem 14: The One-Liner Calculation
# Concept: You do not need intermediate variables for `power1`, `power2`, or `total`.
# You can write the entire math equation directly inside your print statement!

# Problem 15: Executing the Print
# Concept: Write `print()` and inside the parentheses, calculate `a` to the 
# power of `b`, plus `c` to the power of `d`.
print(pow(a, b) + pow(c, d))
# Problem 16-20: Clean Code Optimization
# Concept: Assemble your final script. It should be exactly 5 lines long.
# Four lines sequentially reading inputs into variables, and one line printing 
# the evaluated math expression.

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- The Initial Inputs ---
# 1st input() receives string: "9"
# int() casts it: a = 9
#
# 2nd input() receives string: "29"
# int() casts it: b = 29
#
# 3rd input() receives string: "7"
# int() casts it: c = 7
#
# 4th input() receives string: "27"
# int() casts it: d = 27

# --- The Math Engine ---
# Evaluates left side: 9 ** 29 -> 717897987691852588770249
# Evaluates right side: 7 ** 27 -> 3991196420839079204482643
# Evaluates addition: 717897987691852588770249 + 3991196420839079204482643

# --- Final Output ---
# Console Prints: 4710194409608608369201743232
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(pow(a, b) + pow(c, d))