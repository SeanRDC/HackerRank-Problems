# ==============================================================================
# FUNDAMENTALS CURRICULUM: THE REDUCE ENGINE & RATIONAL NUMBERS
# ==============================================================================
# Goal: Write a single `reduce` statement that takes a list of Fraction objects 
# and multiplies them all together continuously until only one Fraction remains.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: THE FRACTION OBJECT
# ---------------------------------------------------------
# Problem 1: Object Instantiation
# Concept: The boilerplate reads input like "3 4" and passes it to the module.
# Mock State: Fraction(3, 4) creates an object representing 3/4.

# Problem 2: Native Multiplication
# Concept: Because these are objects with overloaded operators (just like the 
# Complex numbers you built earlier!), you can multiply them natively using `*`.
# Mock Math: Fraction(1, 2) * Fraction(3, 4) 
# Mock Output: Fraction(3, 8)

# Problem 3: Automatic Simplification
# Concept: If a multiplication results in an unsimplified fraction, the object 
# automatically simplifies it using the Greatest Common Divisor (GCD).
# Mock Math: Fraction(1, 2) * Fraction(10, 6) -> Fraction(10, 12)
# Auto-Simplified Output: Fraction(5, 6)

# ---------------------------------------------------------
# CONCEPT BLOCK 2: THE REDUCE MECHANICS
# ---------------------------------------------------------

# Problem 4: The Function Signature
# Concept: `reduce()` takes two mandatory arguments: a function (usually a lambda) 
# and an iterable (your list of fractions).

# Problem 5: The Two-Argument Lambda
# Concept: Unlike `map` or `filter` which look at one item at a time, `reduce` 
# needs a function that takes TWO arguments.
# Syntax: `lambda x, y: ...`

# Problem 6: The Lambda Operation
# Concept: Inside the lambda, what mathematical operation do you want to perform 
# on `x` and `y`? (Hint: You are trying to find their product).

# Problem 7: Reduce Iteration 1
# Concept: On the first step, `reduce` grabs the first two items in the list and 
# passes them into your lambda as `x` and `y`.
# Mock State (List of 3 items): x = Fraction 1, y = Fraction 2.
# Action: Lambda returns the product of x and y.

# Problem 8: The Accumulator (Reduce Iteration 2)
# Concept: This is the magic of `reduce`. On the next step, `x` becomes the 
# *result* of the previous calculation, and `y` becomes the next item in the list!
# Mock State: x = (Product of F1 and F2), y = Fraction 3.
# Action: Lambda returns the total product.

# Problem 9: The Final Collapse
# Concept: `reduce` repeats this process until the list is completely exhausted. 
# It then returns the single final value.

# ---------------------------------------------------------
# CONCEPT BLOCK 3: BOILERPLATE INTEGRATION
# ---------------------------------------------------------

# Problem 10: Assigning the Target
# Concept: The boilerplate expects your `reduce` statement to be assigned to 
# the variable `t`.
# Syntax Setup: `t = reduce(...)`

# Problem 11: The First Argument (The Lambda)
# Concept: Drop your two-argument multiplication lambda into the first slot.

# Problem 12: The Second Argument (The Iterable)
# Concept: Pass the `fracs` variable (the list containing all the Fraction 
# objects) into the second slot.

# Problem 13: The Final Return
# Concept: The boilerplate then accesses `t.numerator` and `t.denominator` to 
# print the final simplified values. You don't need to write this part—the 
# boilerplate handles it!

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Input Stage ---
# Boilerplate reads Integer N = 3
# Loop 1: Reads "1 2" -> Appends Fraction(1, 2)
# Loop 2: Reads "3 4" -> Appends Fraction(3, 4)
# Loop 3: Reads "10 6" -> Appends Fraction(10, 6)
# fracs = [Fraction(1, 2), Fraction(3, 4), Fraction(10, 6)]

# --- Reduction Phase ---
# Evaluates Step 1: grabs index 0 and index 1.
# Lambda executes: Fraction(1, 2) * Fraction(3, 4)
# State generated: Fraction(3, 8)

# Evaluates Step 2: grabs new state and index 2.
# Lambda executes: Fraction(3, 8) * Fraction(10, 6)
# State generated: Fraction(30, 48)

# --- Simplification & Output Phase ---
# Fraction object automatically reduces Fraction(30, 48) down to Fraction(5, 8).
# Target `t` now equals Fraction(5, 8).
# Boilerplate extracts `t.numerator` (5) and `t.denominator` (8).
# Console Prints: 5 8

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)