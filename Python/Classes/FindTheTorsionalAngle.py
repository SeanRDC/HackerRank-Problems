# ==============================================================================
# FUNDAMENTALS CURRICULUM: OBJECT-ORIENTED PROGRAMMING & 3D VECTOR MATH
# ==============================================================================
# Goal: Complete a custom `Points` class by implementing the constructor, 
# operator overloading for subtraction, the scalar dot product, and the vector 
# cross product. The boilerplate will use your class to calculate the angle 
# between two planes in 3D space.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: THE CONSTRUCTOR (__init__)
# ---------------------------------------------------------

# Problem 1: The 'self' Parameter
# Concept: When HackerRank creates `Points(*points[0])`, it passes the x, y, 
# and z coordinates into the class. The `self` parameter is the actual object 
# being built. 

# Problem 2: Storing X
# Concept: Inside `__init__`, store the passed `x` argument into an instance 
# variable belonging to `self`. 

# Problem 3: Storing Y
# Concept: Store the passed `y` argument into an instance variable.

# Problem 4: Storing Z
# Concept: Store the passed `z` argument into an instance variable.
# Mock Input: Points(0.0, 4.0, 5.0)
# Mock State: The object now internally holds x=0.0, y=4.0, z=5.0.

# ---------------------------------------------------------
# CONCEPT BLOCK 2: OPERATOR OVERLOADING (__sub__)
# ---------------------------------------------------------

# Problem 5: The Magic Subtraction
# Concept: The boilerplate uses the syntax `b - a`. Because `a` and `b` are 
# custom objects, Python doesn't know how to subtract them natively. It looks 
# for a magic method called `__sub__`.

# Problem 6: Accessing the Second Object
# Concept: In `def __sub__(self, no):`, `self` is the object on the left of 
# the minus sign (e.g., `b`), and `no` is the object on the right (e.g., `a`). 

# Problem 7: Subtracting Coordinates
# Concept: Calculate the difference for all three dimensions. 
# Subtract `no`'s x from `self`'s x, `no`'s y from `self`'s y, and `no`'s z 
# from `self`'s z.

# Problem 8: The Return Type Trap
# Concept: Subtraction creates a brand new vector. You cannot just return a 
# tuple of numbers! You must return a completely new instance of your `Points` 
# class, passing your three new calculated coordinates into it.
# Mock Input: self = Points(1.0, 7.0, 6.0), no = Points(0.0, 4.0, 5.0)
# Mock Output: A new Points object containing (1.0, 3.0, 1.0)

# ---------------------------------------------------------
# CONCEPT BLOCK 3: THE SCALAR DOT PRODUCT (dot)
# ---------------------------------------------------------

# Problem 9: The Math Theory
# Concept: The dot product of two vectors is a single number (a scalar), not 
# a new vector. It represents how much the two vectors point in the same direction.

# Problem 10: X Multiplication
# Concept: In `def dot(self, no):`, multiply `self`'s x by `no`'s x.

# Problem 11: Y and Z Multiplication
# Concept: Multiply the y values together, and the z values together.

# Problem 12: The Summation
# Concept: Add those three calculated products together.
# Formula: $(x_1 \times x_2) + (y_1 \times y_2) + (z_1 \times z_2)$

# Problem 13: Returning the Scalar
# Concept: Return the final summed value. 
# Mock Input: self = Points(1.0, 3.0, 1.0), no = Points(-1.0, -2.0, 3.0)
# Mock Output: -4.0 (A float, NOT a Points object!)

# ---------------------------------------------------------
# CONCEPT BLOCK 4: THE VECTOR CROSS PRODUCT (cross)
# ---------------------------------------------------------

# Problem 14: The Math Theory
# Concept: The cross product of two vectors produces a brand new, third vector 
# that is perfectly perpendicular to both original vectors. This gives us the 
# "normal" line pointing straight up out of the plane!

# Problem 15: Calculating New X
# Concept: The cross product formula is highly specific. Calculate the new X:
# Formula: $(self.y \times no.z) - (self.z \times no.y)$

# Problem 16: Calculating New Y
# Concept: Calculate the new Y. Watch the order carefully!
# Formula: $(self.z \times no.x) - (self.x \times no.z)$

# Problem 17: Calculating New Z
# Concept: Calculate the new Z.
# Formula: $(self.x \times no.y) - (self.y \times no.x)$

# Problem 18: The Object Return
# Concept: Just like subtraction, the cross product must return a brand new 
# instance of your `Points` class holding these three new coordinates.
# Mock Input: self = Points(1.0, 3.0, 1.0), no = Points(-1.0, -2.0, 3.0)
# Mock Output: A new Points object containing (11.0, -4.0, 1.0)

# ---------------------------------------------------------
# CONCEPT BLOCK 5: BOILERPLATE INTEGRATION
# ---------------------------------------------------------

# Problem 19: The Execution Context
# Concept: Look at the provided boilerplate. It takes 4 points (A, B, C, D) 
# and automatically creates your vectors: `AB = (b - a)` and `BC = (c - b)`.

# Problem 20: The Final Math
# Concept: It then calculates the normal vectors of the two planes using your 
# cross product method, and uses your dot product to find the angle between them. 
# If your four methods return the correct data types, the boilerplate handles 
# the rest!

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Input Parsing & Object Creation ---
# Boilerplate reads 4 lines of space-separated floats.
# Instantiates 4 Points objects using your __init__:
# a = Points(0.0, 4.0, 5.0)
# b = Points(1.0, 7.0, 6.0)
# c = Points(0.0, 5.0, 9.0)
# d = Points(1.0, 7.0, 2.0)

# --- Vector Subtraction (__sub__) ---
# Boilerplate evaluates (b - a).
# Calls your __sub__ method. Returns new Points object: (1.0, 3.0, 1.0)
# Boilerplate evaluates (c - b).
# Calls your __sub__ method. Returns new Points object: (-1.0, -2.0, 3.0)
# Boilerplate evaluates (d - c).
# Calls your __sub__ method. Returns new Points object: (1.0, 2.0, -7.0)

# --- The Cross Products (cross) ---
# Boilerplate evaluates x = (b - a).cross(c - b)
# Calls your cross method on the first two generated vectors.
# Returns normal vector of Plane ABC as new Points object: (11.0, -4.0, 1.0)
#
# Boilerplate evaluates y = (c - b).cross(d - c)
# Calls your cross method on the second two generated vectors.
# Returns normal vector of Plane BCD as new Points object: (8.0, -4.0, 0.0)

# --- The Angle Calculation (dot & absolute) ---
# Boilerplate evaluates x.dot(y).
# Calls your dot method. Returns scalar float: 104.0
# Boilerplate divides 104.0 by the multiplied magnitudes of x and y.
# Uses math.acos() to find the radian angle.

# --- Final Output ---
# Formats radians to degrees.
# Console Prints: 8.19