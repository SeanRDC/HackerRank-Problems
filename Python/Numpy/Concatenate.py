# ==============================================================================
# FUNDAMENTALS CURRICULUM: NUMPY ARRAYS & CONCATENATION
# ==============================================================================
# Goal: Import numpy, read the dimensions of the matrices, construct two separate 
# arrays, and stitch them together vertically (axis 0).
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: EXTRACTING THE DIMENSIONS
# ---------------------------------------------------------

# Problem 1: The Dimension Variables
# Concept: The first line of input gives you N, M, and P. 
# N = Rows in Array 1
# M = Rows in Array 2
# P = Columns in both arrays (NumPy requires columns to match for axis=0!)
# Mock Syntax: `n, m, p = map(int, input().split())`

# ---------------------------------------------------------
# CONCEPT BLOCK 2: CONSTRUCTING THE MATRICES
# ---------------------------------------------------------

# Problem 2: Reading the Rows
# Concept: You need to read the next `N` lines of input and turn them into a list 
# of lists (a 2D grid). You can use a list comprehension!
# Mock Syntax: `[input().split() for _ in range(n)]`

# Problem 3: The NumPy Cast
# Concept: A list of lists is just standard Python. You must wrap that entire 
# list comprehension inside `numpy.array( ... , int)` to convert the strings 
# into a strict matrix of integers.
# Mock State: arr1 = numpy.array([['1', '2'], ['1', '2']], int)
# (NumPy is smart enough to cast all the strings to ints for you if you tell it to!)

# Problem 4: Repeat for Array 2
# Concept: Do the exact same thing for `M` to build the second matrix.

# ---------------------------------------------------------
# CONCEPT BLOCK 3: THE STITCHING ENGINE
# ---------------------------------------------------------

# Problem 5: The Concatenation Tuple
# Concept: `numpy.concatenate()` takes a TUPLE of the arrays you want to join. 
# Do not pass them as separate arguments!
# Bad:  `numpy.concatenate(arr1, arr2)`
# Good: `numpy.concatenate((arr1, arr2))`

# Problem 6: The Axis Argument
# Concept: 
# `axis=0` means stacking vertically (row on top of row). This is the default.
# `axis=1` means stacking horizontally (column next to column).
# We want to stack Array 1 on top of Array 2, so axis=0 is our target.

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Input Stage ---
# Read dimensions: n=4, m=3, p=2
# Loop 4 times to build arr1.
# Loop 3 times to build arr2.

# --- Matrix State ---
# arr1 = 
# [[1 2]
#  [1 2]
#  [1 2]
#  [1 2]]
#
# arr2 =
# [[3 4]
#  [3 4]
#  [3 4]]

# --- Concatenation State ---
# numpy.concatenate((arr1, arr2), axis=0)
# Output prints the combined 7x2 matrix automatically formatted by NumPy!
import numpy
n, m, p = map(int, input().split())

N1 = numpy.array([input().split() for _ in range(n)], int)
M1 = numpy.array([input().split() for _ in range(m)], int)

concat = numpy.concatenate((N1, M1))
print(concat)