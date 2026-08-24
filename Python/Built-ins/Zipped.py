# ==============================================================================
# FUNDAMENTALS CURRICULUM: ZIP() AND MATRIX TRANSPOSITION
# ==============================================================================
# Goal: Read a 2D array where rows are subjects and columns are students. 
# Transpose the array so rows become students, calculate the average for each 
# student, and format the output to exactly one decimal place.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: UNDERSTANDING ZIP()
# ---------------------------------------------------------

# Problem 1: The Mock Subjects
# Concept: Create two mock lists representing the first two subjects.
# `sub1 = [89, 90, 78]`
# `sub2 = [90, 91, 85]`

# Problem 2: The Zip Function
# Concept: Pass both lists into the `zip()` function and assign to `zipped`.

# Problem 3: The Zip Object (Python 3 Behavior)
# Concept: Print `zipped`. 
# Mock Output: <zip object at 0x...>
# In Python 3, `zip()` returns a generator object to save memory!

# Problem 4: Viewing the Zip
# Concept: Wrap your `zipped` variable in `list()` and print it.
# Mock Output: [(89, 90), (90, 91), (78, 85)]
# Look closely at the output! The 1st tuple is Student 1's scores. The 2nd 
# tuple is Student 2's scores. Zip automatically grouped them vertically!

# ---------------------------------------------------------
# CONCEPT BLOCK 2: MATRIX TRANSPOSITION (THE MAGIC ASTERISK)
# ---------------------------------------------------------

# Problem 5: The 2D Array
# Concept: In HackerRank, you won't have individual variables for subjects; 
# you will have a 2D array (a list of lists). 
# Create: `matrix = [sub1, sub2]`

# Problem 6: The Unpacking Callback
# Concept: In the last challenge, you used `*` to unpack a list into a print 
# statement. If you write `zip(*matrix)`, Python literally unpacks your 2D 
# array, treating every single row inside it as a separate argument!

# Problem 7: The Transposition
# Concept: Print `list(zip(*matrix))`.
# Mock Output: [(89, 90), (90, 91), (78, 85)]
# You just flipped the entire spreadsheet in a single line of code!

# ---------------------------------------------------------
# CONCEPT BLOCK 3: TUPLE MATHEMATICS
# ---------------------------------------------------------

# Problem 8: Iterating the Zipped Object
# Concept: Write a `for` loop: `for student_scores in zip(*matrix):`.

# Problem 9: Summing the Tuple
# Concept: Inside the loop, you can use the built-in `sum()` function directly 
# on the `student_scores` tuple. Assign this to a variable `total`.

# Problem 10: Getting the Divisor
# Concept: How many subjects did the student take? It's simply the length 
# of their tuple! Assign `len(student_scores)` to a variable `subject_count`.

# Problem 11: The Average Math
# Concept: Divide `total` by `subject_count` to get the average.

# ---------------------------------------------------------
# CONCEPT BLOCK 4: OUTPUT FORMATTING
# ---------------------------------------------------------

# Problem 12: The Rounding Trap
# Concept: HackerRank wants exactly 1 decimal place. 
# If you use `round(90, 1)`, Python will output `90` (dropping the .0). 

# Problem 13: F-String Formatting
# Concept: To force exactly one decimal place, even if it is a zero, we use 
# f-string format specifiers. 
# Create `avg = 90`. Print `f"{avg:.1f}"`. 
# Mock Output: 90.0

# ---------------------------------------------------------
# CONCEPT BLOCK 5: INPUT ARCHITECTURE
# ---------------------------------------------------------

# Problem 14: Reading N and X
# Concept: Line 1 contains students (N) and subjects (X). 
# Read `input().split()`, map to `int`, and unpack into `N` and `X`.

# Problem 15: The Empty Matrix
# Concept: Create an empty list called `scores_matrix = []`.

# Problem 16: The Subject Loop
# Concept: We need to read `X` rows of subjects. 
# Write a `for` loop that iterates `X` times.

# Problem 17: Parsing the Subject
# Concept: Inside the loop, read the next line. 
# Warning! Scores might be decimals (like 90.5). Map the input to `float`, 
# NOT `int`! Convert the mapped result to a `list`.

# Problem 18: Building the Matrix
# Concept: Append that parsed list to your `scores_matrix`.

# ---------------------------------------------------------
# CONCEPT BLOCK 6: FINAL ASSEMBLY PREP
# ---------------------------------------------------------

# Problem 19: The Master Loop
# Concept: Below your input logic, write a new `for` loop that iterates 
# through `zip(*scores_matrix)`.

# Problem 20: Clean Code Execution
# Concept: Inside that loop, calculate the average (sum / length) and print 
# it directly using the f-string format specifier!

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Input Parsing ---
# Input reads Line 1: N = 5, X = 3
# Loop runs 3 times (for 3 subjects).
# Subject 1 parses to list of floats: [89.0, 90.0, 78.0, 93.0, 80.0]
# (Matrix continues building...)

# --- Matrix State ---
# scores_matrix = [
#   [89.0, 90.0, 78.0, 93.0, 80.0],
#   [90.0, 91.0, 85.0, 88.0, 86.0],
#   [91.0, 92.0, 83.0, 89.0, 90.5]
# ]

# --- The Zip Engine ---
# zip(*scores_matrix) dynamically unpacks the 3 lists and groups index by index.

# --- Loop Iteration 1 ---
# Yields Tuple: (89.0, 90.0, 91.0)
# Evaluates total: sum() -> 270.0
# Evaluates length: len() -> 3
# Evaluates average: 270.0 / 3 -> 90.0
# Formats string: "90.0"
# Console Prints: 90.0

# --- Loop Iteration 2 ---
# Yields Tuple: (90.0, 91.0, 92.0)
# Evaluates total: sum() -> 273.0
# Evaluates length: len() -> 3
# Evaluates average: 273.0 / 3 -> 91.0
# Formats string: "91.0"
# Console Prints: 91.0

# (Process continues for all 5 students)