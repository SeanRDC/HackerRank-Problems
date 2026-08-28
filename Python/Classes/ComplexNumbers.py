# ==============================================================================
# FUNDAMENTALS CURRICULUM: COMPLEX NUMBERS & OPERATOR OVERLOADING
# ==============================================================================
# Goal: Build a custom Complex number class that can mathematically add, 
# subtract, multiply, and divide itself against other Complex objects, 
# returning new instantiated objects for each operation.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: STATE & INITIALIZATION
# ---------------------------------------------------------
import math
# Problem 1: The Constructor 
# Concept: Just like your 3D points, the boilerplate passes data into the 
# `__init__` method. Bind the passed `real` argument to an instance variable.

# Problem 2: The Imaginary State
# Concept: Bind the passed `imaginary` argument to an instance variable.
# Mock Input: Complex(2.0, 1.0)
# Mock State: self holds real=2.0, imaginary=1.0
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
# ---------------------------------------------------------
# CONCEPT BLOCK 2: LINEAR ARITHMETIC (+ and -)
# ---------------------------------------------------------

# Problem 3: The Addition Overload (__add__)
# Concept: When you evaluate `x + y`, Python calls `x.__add__(y)`.
# Add `self`'s real part to `no`'s real part.
# Add `self`'s imaginary part to `no`'s imaginary part.

# Problem 4: Returning the Sum
# Concept: Return a brand new `Complex` object passing in the new real and 
# imaginary sums.
# Mock Input: self=(2.0, 1.0), no=(5.0, 6.0)
# Mock Output: Complex(7.0, 7.0)

# Problem 5: The Subtraction Overload (__sub__)
# Concept: Overload the `-` operator. Subtract `no`'s real part from `self`'s 
# real part, and `no`'s imaginary part from `self`'s imaginary part.

# Problem 6: Returning the Difference
# Concept: Return a brand new `Complex` object with the differences.
# Mock Input: self=(2.0, 1.0), no=(5.0, 6.0)
# Mock Output: Complex(-3.0, -5.0)
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
    
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
# ---------------------------------------------------------
# CONCEPT BLOCK 3: MULTIPLICATION (__mul__)
# ---------------------------------------------------------

# Problem 7: The Math Theory (FOIL)
# Concept: Multiplying complex numbers $C_1 = a + bi$ and $C_2 = c + di$ 
# requires the FOIL method. Remember that $i^2 = -1$.
# The formula resolves to: $(ac - bd) + (ad + bc)i$

# Problem 8: The Real Part Calculation
# Concept: Using the variables `self.real` (a), `self.imaginary` (b), 
# `no.real` (c), and `no.imaginary` (d), calculate the new real part: $(ac - bd)$.

# Problem 9: The Imaginary Part Calculation
# Concept: Calculate the new imaginary part using the formula: $(ad + bc)$.

# Problem 10: Returning the Product
# Concept: Return a brand new `Complex` object using these calculated parts.
# Mock Input: self=(2.0, 1.0), no=(5.0, 6.0)
# Mock Output: Complex(4.0, 17.0)
    def __mul__(self, no):
        real = (self.real * no.real) - (self.imaginary * no.imaginary)
        imaginary = (self.real * no.imaginary) + (self.imaginary * no.real)
        return Complex(real, imaginary)
# ---------------------------------------------------------
# CONCEPT BLOCK 4: DIVISION (__truediv__)
# ---------------------------------------------------------

# Problem 11: The Math Theory (The Conjugate)
# Concept: To divide $\frac{a + bi}{c + di}$, you multiply the top and bottom 
# by the denominator's conjugate $(c - di)$. 

# Problem 12: The Divisor (Denominator)
# Concept: The denominator formula simplifies beautifully to a single scalar 
# float: $c^2 + d^2$. Calculate this using `no.real` and `no.imaginary`.

# Problem 13: The New Real Numerator
# Concept: The formula for the real part of the numerator is: $(ac + bd)$.

# Problem 14: The New Imaginary Numerator
# Concept: The formula for the imaginary part of the numerator is: $(bc - ad)$.

# Problem 15: Returning the Quotient
# Concept: Return a new `Complex` object. The new real argument is the real 
# numerator divided by the divisor. The new imaginary argument is the imaginary 
# numerator divided by the divisor.
# Mock Input: self=(2.0, 1.0), no=(5.0, 6.0)
# Mock Output: Complex(0.262..., -0.114...)
    def __truediv__(self, no):
        divisor = no.real**2 + no.imaginary**2
        real_num = (self.real * no.real) + (self.imaginary * no.imaginary)
        imaginary_num = (self.imaginary * no.real) - (self.real * no.imaginary)
        return Complex(real_num / divisor, imaginary_num / divisor)
    
# ---------------------------------------------------------
# CONCEPT BLOCK 5: THE MODULUS (mod)
# ---------------------------------------------------------

# Problem 16: The Math Theory
# Concept: The modulus of a complex number is its distance from the origin on 
# a 2D plane. It is identical to the magnitude calculation from your 3D vectors 
# (just without the Z axis). 
# Formula: $\sqrt{a^2 + b^2}$

# Problem 17: Calculating the Modulus
# Concept: Calculate the square root of (`self.real` squared + `self.imaginary` 
# squared) using the `**` operator or the `math` module.

# Problem 18: The Formatting Trap
# Concept: The `mod` function evaluates to a single scalar float. However, 
# look closely at the boilerplate output expectations. It wants the modulus 
# formatted exactly like a complex number: `2.24+0.00i`.

# Problem 19: Returning the Modulus Object
# Concept: Because the boilerplate relies on `__str__` to format the outputs, 
# your `mod()` method MUST return a new `Complex` object! 
# Pass your calculated scalar modulus as the real argument, and pass a hardcoded 
# `0` as the imaginary argument.
# Mock Input: self=(2.0, 1.0)
# Mock Output: Complex(2.236..., 0)

# Problem 20: Boilerplate Execution
# Concept: The boilerplate's `print(*map(str, [x+y, x-y...]))` line evaluates 
# each of your overloaded operators, casts the resulting objects to strings 
# (triggering the provided `__str__` method), and prints them separated by 
# newlines.
    def __mod__(self, no):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)
        
# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Input Parsing & Object Creation ---
# Boilerplate reads "2 1", instantiates x = Complex(2.0, 1.0)
# Boilerplate reads "5 6", instantiates y = Complex(5.0, 6.0)

# --- Arithmetic Execution Engine ---
# Evaluates [x+y] -> Triggers x.__add__(y)
# Returns new Complex object: (7.0, 7.0)

# Evaluates [x-y] -> Triggers x.__sub__(y)
# Returns new Complex object: (-3.0, -5.0)

# Evaluates [x*y] -> Triggers x.__mul__(y)
# Evaluates (2*5 - 1*6) for real, (2*6 + 1*5) for imaginary.
# Returns new Complex object: (4.0, 17.0)

# Evaluates [x/y] -> Triggers x.__truediv__(y)
# Divisor evaluates to (5^2 + 6^2) = 61.
# Numerators divided by 61.
# Returns new Complex object: (0.262..., -0.114...)

# Evaluates [x.mod()] -> Triggers x.mod()
# Evaluates sqrt(2^2 + 1^2) = 2.236...
# Returns new Complex object: (2.236..., 0)

# --- Final String Formatting ---
# map(str, ...) iterates over the list of newly generated Complex objects.
# The provided __str__ method formats floats to exactly 2 decimal places.
# Console Prints Line 1: 7.00+7.00i
# Console Prints Line 2: -3.00-5.00i
# Console Prints Line 3: 4.00+17.00i
# Console Prints Line 4: 0.26-0.11i
# Console Prints Line 5: 2.24+0.00i

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
    
    def __mul__(self, no):
        real = (self.real * no.real) - (self.imaginary * no.imaginary)
        imaginary = (self.real * no.imaginary) + (self.imaginary * no.real)
        return Complex(real, imaginary)
    
    def __truediv__(self, no):
        divisor = no.real**2 + no.imaginary**2
        real_num = (self.real * no.real) + (self.imaginary * no.imaginary)
        imaginary_num = (self.imaginary * no.real) - (self.real * no.imaginary)
        return Complex(real_num / divisor, imaginary_num / divisor)
    
    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)
    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
    
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')