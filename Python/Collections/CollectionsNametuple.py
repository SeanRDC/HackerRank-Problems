# ==============================================================================
# CHALLENGE: COLLECTIONS.NAMEDTUPLE()
# ==============================================================================
# Goal: 
# You are given a spreadsheet of student data. The catch? The columns can be 
# in ANY order. You need to calculate the average of the 'MARKS' column.
#
# Test Input Breakdown:
# 5                                     <- N (Number of students)
# ID         MARKS      NAME       CLASS  <- The column headers (can be in any order)
# 1          97         Raymond    7      <- Row 1
# 2          50         Steven     4      <- Row 2
# ...
#
# Constraints & Nuances:
# You must use a `namedtuple`. 
# We need to output the average to exactly 2 decimal places.
# HackerRank dares you to do this in 4 lines of code! We will build the standard 
# version first, then golf it down to 4 lines in the final phase.
# ==============================================================================

# ---------------------------------------------------------
# PHASE 1: NAMEDTUPLE BASICS
# ---------------------------------------------------------

# Problem 1: The Import
# Concept: Write the code to import `namedtuple` from the `collections` module.
from collections import namedtuple
# Problem 2: Creating the Blueprint
# A namedtuple creates a mini-class. You give it a name, and a string of space-separated fields.
# Concept: Create a namedtuple blueprint called `Student`. Pass the string 
# `'Student'` as the first argument, and `'ID MARKS NAME CLASS'` as the second. 
# Assign this blueprint to a variable named `Student`.
Student = namedtuple('Student', 'ID MARKS NAME CLASS')
# Problem 3: Instantiating an Object
# Concept: Now that you have the `Student` blueprint, create a new student named `student_1`.
# Pass in 4 string arguments: '1', '97', 'Raymond', '7'.
student_1 = Student('1', '97', 'Raymond', '7')
# Problem 4: Accessing Attributes
# Concept: Instead of using `student_1[1]` like a normal tuple, write an expression 
# to access the marks using dot notation (e.g., `.MARKS`) and print it.
# Mock Output: '97'
print(student_1.MARKS)

# ---------------------------------------------------------
# PHASE 2: DYNAMIC COLUMN CREATION
# ---------------------------------------------------------

# Problem 5: The Split Trick
# In the real HackerRank test, the columns won't always be 'ID MARKS NAME CLASS'.
# But HackerRank gives us the exact order on line 2! 
# Concept: Create a mock input string: `mock_headers = "MARKS CLASS NAME ID"`. 
# Use the `.split()` method on it to create a list of strings, and save it to `columns_list`.
mock_headers = "MARKS CLASS NAME ID"
columns_list = mock_headers.split()

# Problem 6: The Dynamic Blueprint
# Did you know `namedtuple` can accept a list of strings for its fields, not just a single string?
# Concept: Recreate the `Student` blueprint, but this time pass `columns_list` 
# as the second argument instead of a hardcoded string.
Student = namedtuple('Student', columns_list)

# Problem 7: Validating the Dynamic Blueprint
# Concept: Create `student_2 = Student('92', '2', 'Calum', '1')`. 
# Print `student_2.MARKS` to verify it correctly mapped '92' to MARKS based on your dynamic list!
# Mock Output: '92'
student_2 = Student('92', '2', 'Calum', '1')
print(student_2.MARKS)
# ---------------------------------------------------------
# PHASE 3: THE UNPACKING OPERATOR (*)
# ---------------------------------------------------------

# Problem 8: Row Data
# Concept: Create a mock list representing a row of data from input().split():
# `row_data = ['94', '2', 'Jason', '3']`
row_data = ['94', '2', 'Jason', '3']

# Problem 9: The Asterisk (*) Unpacker
# If you try `Student(row_data)`, Python thinks you are passing 1 argument (a list) 
# instead of 4 separate arguments. The `*` operator unpacks a list into separate arguments!
# Concept: Create `student_3` by passing `*row_data` into your `Student` blueprint.
student_3 = Student(*row_data)

# Problem 10: Validating the Unpack
# Concept: Print `student_3.NAME` to ensure the unpacking worked perfectly.
# Mock Output: 'Jason'
print(student_3.NAME)
# ---------------------------------------------------------
# PHASE 4: THE STANDARD LOOP ENGINE
# ---------------------------------------------------------

# Problem 11: The Accumulator
# Concept: Create a variable `total_marks` and set it to 0. 
total_marks = 0
# Problem 12: Converting to Integer
# When we pull `.MARKS` from our namedtuple, it's a string. We must convert it to do math.
# Concept: Write an expression that takes `student_3.MARKS`, converts it to an integer, 
# and adds it to `total_marks`.
total_marks += int(student_3.MARKS)
# Problem 13: Formatting to 2 Decimal Places
# Concept: Assume `total_marks` is now 94, and `N` (total students) is 1. 
# The average is 94.0. Using an f-string, write a print statement that formats 
# `total_marks / 1` to exactly two decimal places using `:.2f`.
# Mock Output: '94.00'
result = total_marks / 1
print(f"{result:.2f}")
# ---------------------------------------------------------
# PHASE 5: THE 4-LINE CHALLENGE (CODE GOLFING)
# ---------------------------------------------------------

# Problem 14: Line 1 - The Import
# Concept: Your first line of the final script is simply your import statement from Problem 1.
from collections import namedtuple
# Problem 15: Line 2 - The Double Assignment
# We can read `N` and build the `Student` blueprint in one line using tuple unpacking!
# Concept: Write `N, Student = int(input()), namedtuple('Student', input().split())`.
N, Student = int(input()), namedtuple('Student', input().split())

# Problem 16: Line 3 (Part A) - The List Comprehension Loop
# Instead of a `for` loop, we can gather all the marks in one go using a list comprehension.
# Concept: Write the skeleton of a list comprehension that loops N times: `[___ for _ in range(N)]`

# Problem 17: Line 3 (Part B) - Reading and Unpacking inside the Comprehension
# Inside that comprehension, we need to read the line, split it, unpack it, and build a Student.
# Concept: Replace the `___` with `Student(*input().split())`
marks = [int(Student(*input().split()).MARKS) for _ in range(N)]
# Problem 18: Line 3 (Part C) - Extracting the Marks
# We don't want a list of Student objects; we just want their integer marks!
# Concept: Modify Part B to extract the `.MARKS` attribute and wrap it in `int()`.
# E.g., `int(Student(*input().split()).MARKS)`

# Problem 19: Line 3 (Complete) - The Marks List
# Concept: Combine 16, 17, and 18 into a single line. Assign it to a variable called `marks`.
# (e.g., `marks = [int(...) for _ in range(N)]`)

# Problem 20: Line 4 - The Final Calculation and Print
# Concept: Your final line simply prints the average. Use the `sum()` function on your 
# `marks` list, divide it by `N`, and wrap it in the f-string formatting from Problem 13!
print(f"{sum(marks) / N:.2f}")

# ==============================================================================
# SUMMARY:
# You just learned how to create lightweight objects on the fly, map dynamic 
# column headers to class attributes, unpack lists into arguments using `*`, 
# and compress a multi-line data parsing loop into a single, hyper-efficient 
# list comprehension. 
# ==============================================================================
from collections import namedtuple

N, Student = int(input()), namedtuple('Student', input().split())
marks = [int(Student(*input().split()).MARKS) for _ in range(N)]
print(f"{sum(marks) / N:.2f}")