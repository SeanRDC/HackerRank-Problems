# =====================================================================
# THE PROBLEM: Provide test data to validate a coworker's minimum_index function.
# 
# THE DETAILED GOAL: The precode contains three test functions that run assertions 
# against your data. You must build three classes that supply data to pass these tests:
# 
# 1. TestDataEmptyArray:
#    - The test expects `minimum_index` to raise a ValueError. 
#    - Your goal: Supply a completely empty array (e.g., []).
# 
# 2. TestDataUniqueValues:
#    - The test asserts: `len(seq) >= 2` (Must have at least 2 elements)
#    - The test asserts: `len(list(set(seq))) == len(seq)` (All elements MUST be unique)
#    - Your goal: Supply a unique array (e.g., [7, 4, 9]) and accurately return 
#      the index of the minimum value (e.g., index 1).
# 
# 3. TestDataExactlyTwoDifferentMinimums:
#    - The test asserts: `len(seq) >= 2`
#    - The test asserts: When sorted, the first two elements are identical, and 
#      any third element is strictly greater. 
#    - Your goal: Supply an array where the lowest number appears exactly twice 
#      (e.g., [5, 2, 8, 2]) and return the index of its VERY FIRST appearance (e.g., index 1).
# =====================================================================

# ---------------------------------------------------------
# PHASE 1: CLASSES AND STATIC METHODS
# ---------------------------------------------------------

# Problem 1: Class Definition
# Define a class named `TestDataEmptyArray`.
class TestDataEmptyArray:

    # Problem 2: The Static Method Decorator
    # We want to call methods on the class itself, not on an instance of the class 
    # (e.g., `TestDataEmptyArray.get_array()` instead of `obj = TestDataEmptyArray(); obj.get_array()`).
    # Above your next method definition, add the built-in Python decorator that makes a method static.
    @staticmethod

    # Problem 3: The Empty Array Method
    # Define a method named `get_array` directly under the decorator. 
    # Because it is static, it does NOT need `self` as an argument.
    def get_array():

        # Problem 4: Returning Empty
        # Inside `get_array`, return an empty Python list.
        # Mock Input: None
        # Expected Output: []
        return []

# ---------------------------------------------------------
# PHASE 2: UNIQUE VALUES TEST DATA
# ---------------------------------------------------------

# Problem 5: Class Definition
# Define a class named `TestDataUniqueValues`.
class TestDataUniqueValues:

    # Problem 6: The Static Method Decorator
    # Add the static method decorator again for the next method.
    @staticmethod

    # Problem 7: The Array Method
    # Define a method named `get_array`.
    def get_array():

        # Problem 8: Returning Unique Data
        # Inside `get_array`, return a hardcoded list of at least 2 integers where 
        # EVERY integer is completely unique.
        # Example Mock List: [5, 10, 15, 20]
        return [5, 10, 15, 20]

    # Problem 9: The Static Method Decorator
    # Add the static method decorator for the next method.
    @staticmethod

    # Problem 10: The Expected Result Method
    # Define a method named `get_expected_result`.
    def get_expected_result():

        # Problem 11: Finding the Minimum Index
        # Look at the hardcoded list you created in Problem 8.
        # What is the index (0-based) of the smallest number in that list?
        # Return that exact integer value here.
        # Mock Input: Assuming list is [5, 10, 15]
        # Expected Output: 0
        return 0

# ---------------------------------------------------------
# PHASE 3: EXACTLY TWO MINIMUMS TEST DATA
# ---------------------------------------------------------

# Problem 12: Class Definition
# Define a class named `TestDataExactlyTwoDifferentMinimums`.


    # Problem 13: The Static Method Decorator
    # Add the static method decorator.


    # Problem 14: The Array Method
    # Define a method named `get_array`.


        # Problem 15: Returning Duplicate Minimums Data
        # Inside `get_array`, return a hardcoded list of integers.
        # CRUCIAL RULE: The absolute minimum value in this list MUST appear exactly twice.
        # Every other number must be strictly greater than that minimum value.
        # Example Mock List: [8, 3, 9, 3, 12] (The minimum is 3, and it appears at index 1 and 3)


    # Problem 16: The Static Method Decorator
    # Add the static method decorator.


    # Problem 17: The Expected Result Method
    # Define a method named `get_expected_result`.


        # Problem 18: Finding the FIRST Minimum Index
        # Look at the hardcoded list you created in Problem 15.
        # The target function `minimum_index` is supposed to return the *smallest* index 
        # if there are ties. What is the very first index where your minimum value appears?
        # Return that exact integer value here.
        # Mock Input: Assuming list is [8, 3, 9, 3, 12]
        # Expected Output: 1


# ---------------------------------------------------------
# PHASE 4: UNDERSTANDING THE TARGET FUNCTION
# ---------------------------------------------------------

# Problem 19: Reviewing the Target Code
# Look closely at the `minimum_index(seq)` function provided in the precode.
# What does `len(seq) == 0` do? 
# (Mental exercise: How does your `TestDataEmptyArray` interact with this?)

# Problem 20: Reviewing the Tie-Breaker Logic
# Look at the `if seq[i] < seq[min_idx]:` line in the target function.
# Notice the `<` operator. If it encounters a value *equal* to the current minimum, it does nothing.
# (Mental exercise: How does this prove your `TestDataExactlyTwoDifferentMinimums.get_expected_result()` is correct?)


# =====================================================================
# FINAL SUBMISSION
# SUMMARY: Assemble the three classes you built (`TestDataEmptyArray`, 
# `TestDataUniqueValues`, `TestDataExactlyTwoDifferentMinimums`) and their 
# respective static methods. Combine them with the provided precode. The 
# test functions at the bottom will automatically call your classes to 
# validate that your mock data meets the constraints.
# 
# MOCK INPUT (STDIN): 
# (No STDIN required for this challenge, the tests run internally)
# 
# EXPECTED OUTPUT: 
# OK
# =====================================================================

# Paste your assembled final script (including the precode) here!