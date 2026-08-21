# ==============================================================================
# FUNDAMENTALS CURRICULUM: COMPLEX NUMBERS & THE CMATH MODULE
# ==============================================================================
# Goal: Read a complex number as a string, convert it to a complex object, 
# and use Python's built-in tools to calculate its modulus (r) and phase (phi).
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: THE COMPLEX DATA TYPE
# ---------------------------------------------------------

# Problem 1: The Mock String
# Concept: Create a mock string representing the HackerRank sample data.
# `z_str = "1+2j"`
z_str = "1+2j"
# Problem 2: The Complex Casting
# Concept: Just like `int()` and `float()`, Python has a `complex()` built-in 
# function that parses standard complex number strings. 
# Pass `z_str` into `complex()` and assign it to a variable `z`.
z = complex(z_str)
print(z)
# Problem 3: Viewing the Real Part
# Concept: Complex objects have built-in attributes. Print `z.real`.
# Mock Output: 1.0
print(z.real)
# Problem 4: Viewing the Imaginary Part
# Concept: Print `z.imag`.
# Mock Output: 2.0 (Notice how Python stripped the 'j' and gave you the float!)
print(z.imag)
# ---------------------------------------------------------
# CONCEPT BLOCK 2: THE MODULUS (DISTANCE 'r')
# ---------------------------------------------------------

# Problem 5: The Manual Pythagorean Math
# Concept: As shown in image_40ec86.png, the distance 'r' is just the hypotenuse! 
# Using the `**` operator, calculate the square root of (real^2 + imag^2). 
# (Hint: taking something to the power of 0.5 is a square root).
sqrt = (pow(z.real, 2) + pow(z.imag, 2)) ** 0.5
print(sqrt)
# Problem 6: The Absolute Shortcut
# Concept: Python's built-in `abs()` function doesn't just make negative numbers 
# positive; when given a complex number, it automatically calculates the modulus!
# Call `abs(z)` and assign it to a variable `r`.
r = abs(z)
# Problem 7: Verifying the Modulus
# Concept: Print `r`. 
# Mock Output: 2.23606797749979
# (Notice how this perfectly matches the Pythagorean math from Problem 5!)
print(r)
# ---------------------------------------------------------
# CONCEPT BLOCK 3: THE PHASE (ANGLE 'phi')
# ---------------------------------------------------------

# Problem 8: The Cmath Import
# Concept: To get the phase, we need the complex math module. 
# Write `import cmath`.
import cmath
import math
# Problem 9: The Manual Angle
# Concept: In the last challenge, you used `math.atan2(y, x)` to find the angle. 
# You could import `math` and run `math.atan2(z.imag, z.real)`. 
print(math.atan2(z.imag, z.real))
# Problem 10: The Cmath Shortcut
# Concept: The `cmath` module makes this even easier. It has a built-in function 
# called `phase()` that accepts a complex number object directly.
# Pass `z` into `cmath.phase()` and assign it to a variable `phi`.
phi = cmath.phase(z)
# Problem 11: Verifying the Phase
# Concept: Print `phi`.
# Mock Output: 1.1071487177940904 (This is the angle in radians!)
print(phi)
# ---------------------------------------------------------
# CONCEPT BLOCK 4: THE ULTIMATE CMATH SHORTCUT (OPTIONAL)
# ---------------------------------------------------------

# Problem 12: The Polar Function
# Concept: The `cmath` module is so well-designed that it actually has a single 
# function that calculates BOTH the modulus and the phase at the same time.
# Pass `z` into `cmath.polar()` and print the result.
print(cmath.polar(z))
# Problem 13: Analyzing the Output
# Concept: Notice the output is a tuple containing `(r, phi)`. 
# This perfectly mimics the `divmod` behavior we learned earlier!

# Problem 14: Tuple Unpacking
# Concept: Use tuple unpacking to extract both variables on a single line:
# `r_shortcut, phi_shortcut = cmath.polar(z)`. 
r_shortcut, phi_shortcut = cmath.polar(z)
# ---------------------------------------------------------
# CONCEPT BLOCK 5: INPUT ARCHITECTURE & ASSEMBLY
# ---------------------------------------------------------

# Problem 15: Reading the Input
# Concept: Call `input()` to read the raw string from HackerRank.

# Problem 16: Casting the Input
# Concept: Wrap your `input()` call directly inside the `complex()` function 
# to immediately build your complex object. Assign it to `z`.
z = complex()
# Problem 17: Calculating r
# Concept: Using either `abs()` or `cmath.polar()`, find the modulus.
r = cmath.polar(z)
# Problem 18: Calculating phi
# Concept: Using either `cmath.phase()` or `cmath.polar()`, find the phase.
phi = cmath.polar(z)
# Problem 19: The First Output Line
# Concept: Print the modulus `r`. 
# (Note: HackerRank says "correct up to 3 decimal places" but their sample 
# output shows the full float. Printing the raw float is usually safest first).
print(r)
print(phi)
# Problem 20: The Second Output Line
# Concept: Print the phase `phi` on the very next line.

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- The Initial Inputs ---
# input() receives string: "1+2j"
# complex() casts it to object: z = (1+2j)

# --- The Math Engine ---
# abs(1+2j) calculates the distance to origin.
# Modulus evaluates to: 2.23606797749979
#
# cmath.phase(1+2j) calculates the counter-clockwise angle in radians.
# Phase evaluates to: 1.1071487177940904

# --- Final Output ---
# Console Prints Line 1: 2.23606797749979
# Console Prints Line 2: 1.1071487177940904
import cmath
z = complex(input())
r = cmath.polar(z)[0]
phi = cmath.phase(z)
print(r)
print(phi)