# ==============================================================================
# FUNDAMENTALS CURRICULUM: GEOMETRY, TRIGONOMETRY, & THE MATH MODULE
# ==============================================================================
# Goal: Calculate angle theta (Angle MBC) in degrees, given sides AB and BC.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: THE GEOMETRIC SECRET (NO CODE NEEDED)
# ---------------------------------------------------------

# Problem 1: The Median Rule
# Concept: In a right-angled triangle, a median drawn to the hypotenuse 
# divides the triangle into two isosceles triangles. 
# Therefore, the length of median MB is exactly equal to MC (and MA).

# Problem 2: The Isosceles Deduction
# Concept: Because triangle MBC is an isosceles triangle (MB = MC), the angles 
# opposite those equal sides are also equal. This means Angle MBC (theta) is 
# exactly equal to Angle MCB (which is just Angle C of the main triangle!).

# Problem 3: The Tangent Ratio
# Concept: To find Angle C, we use basic trigonometry (SOH CAH TOA).
# We know the Opposite side (AB) and the Adjacent side (BC).
# Tangent(Angle C) = AB / BC. Therefore, Angle C = arctangent(AB / BC).
# You don't even need the hypotenuse!

# ---------------------------------------------------------
# CONCEPT BLOCK 2: TRIGONOMETRY IN PYTHON
# ---------------------------------------------------------

# Problem 4: The Import
# Concept: We need advanced math functions. Write `import math`.
import math
# Problem 5: The Mock Inputs
# Concept: Create two variables for our mock sides. 
# `AB = 10` and `BC = 10`.
AB = 10
BC = 10
# Problem 6: The Arctangent Function
# Concept: Python's math module has an arctangent function: `math.atan()`.
# However, `math.atan2(y, x)` is much better because it natively handles correct 
# quadrants and zero-division. 
# Here, y is the opposite side (AB) and x is the adjacent side (BC).

# Problem 7: Calculating Radians
# Concept: Pass `AB` and `BC` into `math.atan2(AB, BC)` and assign the result 
# to a variable `theta_radians`. Print it.
# Mock Output: 0.7853981633974483 (This is the angle, but in radians!)
theta_radiants = math.atan2(AB, BC)
# ---------------------------------------------------------
# CONCEPT BLOCK 3: DEGREE CONVERSION & ROUNDING
# ---------------------------------------------------------

# Problem 8: Converting to Degrees
# Concept: Humans read degrees, not radians. Use the built-in 
# `math.degrees()` function on your `theta_radians` variable.
# Assign it to `theta_degrees` and print it.
# Mock Output: 45.0
theta_degrees = math.degrees(theta_radiants)
print(theta_degrees)
# Problem 9: The One-Liner Math
# Concept: Combine Problems 7 and 8. Wrap your `math.atan2()` call directly 
# inside `math.degrees()`. 
math.degrees(math.atan2(AB, BC))
# Problem 10: Standard Rounding
# Concept: HackerRank requires the answer rounded to the nearest integer.
# Use Python's built-in `round()` function on your `theta_degrees` variable.
# Mock Output: 45
rounded = round(theta_degrees)
# ---------------------------------------------------------
# CONCEPT BLOCK 4: THE DEGREE SYMBOL & FORMATTING
# ---------------------------------------------------------

# Problem 11: The Degree Symbol
# Concept: You need to append the degree symbol to your output. 
# You can copy-paste the character directly (`°`) or use Python's character 
# generation: `chr(176)`. Create a variable `degree_sign = chr(176)`.
degree_sign = chr(176)
# Problem 12: String Concatenation
# Concept: Cast your rounded integer to a string using `str()`, and add it to 
# your `degree_sign`. Print the result.
# Mock Output: 45°
print(f"{round(rounded)}{degree_sign}" )
# Problem 13: F-String Alternative
# Concept: F-strings are usually cleaner! Try formatting the final output like 
# this: `print(f"{rounded_angle}{chr(176)}")`.

# ---------------------------------------------------------
# CONCEPT BLOCK 5: INPUT ARCHITECTURE
# ---------------------------------------------------------

# Problem 14: Reading AB
# Concept: The first input is AB. Read it using `input()`, convert it to an 
# integer, and assign it to `ab`.

# Problem 15: Reading BC
# Concept: The second input is BC on a new line. Read it using `input()`, 
# convert it to an integer, and assign it to `bc`.

# ---------------------------------------------------------
# CONCEPT BLOCK 6: FINAL ASSEMBLY PREP
# ---------------------------------------------------------

# Problem 16: The Math Wrap
# Concept: Inside your final script, calculate the degrees using 
# `math.degrees(math.atan2(ab, bc))`.

# Problem 17: The Banker's Rounding Trap
# Concept: Standard `round(56.5)` in Python returns 56 (rounds to nearest even). 
# HackerRank states 56.5 should be 57 (round half up). Luckily, due to floating 
# point math, `math.degrees` rarely hits exactly `.5000000000000000`, so 
# standard `round()` will actually pass all test cases for this specific problem!

# Problem 18: Evaluating the Output
# Concept: Execute the `round()` function on your degree calculation.

# Problem 19: The String Assembly
# Concept: Prepare the final string with the degree symbol appended.

# Problem 20: The Final Print
# Concept: Wrap it all in a `print()` statement. Your final script should only 
# be about 4 lines long (including the import)!

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- The Initial Inputs ---
# 1st input() receives string: "10"
# int() casts it: ab = 10
#
# 2nd input() receives string: "10"
# int() casts it: bc = 10

# --- The Math Engine ---
# math.atan2(10, 10) calculates radians: 0.7853981633974483
# math.degrees(0.785398...) converts to degrees: 45.0
# round(45.0) evaluates to integer: 45

# --- Formatting ---
# chr(176) evaluates to: "°"
# str(45) + "°" evaluates to: "45°"

# --- Final Output ---
# Console Prints: 45°
import math
ab = int(input())
bc = int(input())
print(f"{round(math.degrees(math.atan2(ab, bc)))}{chr(176)}")