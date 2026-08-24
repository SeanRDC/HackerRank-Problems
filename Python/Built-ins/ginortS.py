# ==============================================================================
# FUNDAMENTALS CURRICULUM: ADVANCED SORTING & TUPLE PRIORITIES
# ==============================================================================
# Goal: Sort a string by prioritizing lowercase (0), uppercase (1), odd digits (2), 
# and even digits (3), while maintaining alphabetical/numerical order within groups.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: THE ASCII DEFAULT
# ---------------------------------------------------------

# Problem 1: The Mock String
# Concept: Create a mock string representing the sample input.
# `s = "Sorting1234"`

# Problem 2: The Default Sort
# Concept: Call `sorted(s)` and print it.
# Mock Output: ['1', '2', '3', '4', 'S', 'g', 'i', 'n', 'o', 'r', 't']

# Problem 3: Analyzing the Default
# Concept: Notice the default order? Digits -> Uppercase -> Lowercase. 
# This happens because Python sorts by ASCII values! Our goal is to completely 
# reverse this priority system.

# ---------------------------------------------------------
# CONCEPT BLOCK 2: CHARACTER CATEGORIZATION
# ---------------------------------------------------------

# Problem 4: Lowercase Check
# Concept: Test the built-in string methods. Print `'g'.islower()`. (True)

# Problem 5: Uppercase Check
# Concept: Print `'S'.isupper()`. (True)

# Problem 6: Digit Check
# Concept: Print `'1'.isdigit()`. (True)

# Problem 7: Odd/Even Check
# Concept: If a character is a digit, you can cast it to an integer and use 
# modulo to check for odd/even. Print `int('3') % 2 == 1`. (True = Odd)

# ---------------------------------------------------------
# CONCEPT BLOCK 3: THE TUPLE TIE-BREAKER
# ---------------------------------------------------------

# Problem 8: How Python Sorts Tuples
# Concept: Create a list of tuples: `data = [(1, 'A'), (0, 'a')]`. 
# Print `sorted(data)`.

# Problem 9: Evaluating the Tuple Sort
# Concept: Mock Output: [(0, 'a'), (1, 'A')]
# Python mathematically looks at the 0 and 1 first. Because 0 comes before 1, 
# 'a' is sorted before 'A'. We can use this exact mechanic as our sorting key!

# ---------------------------------------------------------
# CONCEPT BLOCK 4: THE PRIORITY FUNCTION
# ---------------------------------------------------------

# Problem 10: Defining the Key Function
# Concept: Let's build a dedicated function to evaluate characters.
# Write: `def get_priority(c):`

# Problem 11: Priority 0 (Lowercase)
# Concept: Inside the function, write `if c.islower(): return (0, c)`

# Problem 12: Priority 1 (Uppercase)
# Concept: Write `elif c.isupper(): return (1, c)`

# Problem 13: Priority 2 (Odd Digits)
# Concept: Write `elif c.isdigit() and int(c) % 2 == 1: return (2, c)`

# Problem 14: Priority 3 (Even Digits)
# Concept: Write `elif c.isdigit() and int(c) % 2 == 0: return (3, c)`

# Problem 15: Testing the Function
# Concept: Pass `'S'` into `get_priority()` and print it. 
# Mock Output: (1, 'S')

# ---------------------------------------------------------
# CONCEPT BLOCK 5: APPLYING THE CUSTOM SORT
# ---------------------------------------------------------

# Problem 16: The Sort Execution
# Concept: Use your function as the key for the `sorted()` function!
# `result = sorted(s, key=get_priority)`

# Problem 17: Viewing the Result
# Concept: Print `result`.
# Mock Output: ['g', 'i', 'n', 'o', 'r', 't', 'S', '1', '3', '2', '4']

# Problem 18: Rebuilding the String
# Concept: The `sorted()` function always returns a list. To stitch a list of 
# characters back into a string, use the string join method: `"".join(result)`.

# ---------------------------------------------------------
# CONCEPT BLOCK 6: FINAL ASSEMBLY PREP
# ---------------------------------------------------------

# Problem 19: The Input
# Concept: Swap out the mock string `s` for `input()`.

# Problem 20: Clean Code Execution
# Concept: Assemble your final script. Write your `get_priority` function, 
# read the input, sort it using the function, and print the joined string!

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Input Parsing ---
# input() receives string: "Sorting1234"

# --- The Sorting Engine ---
# sorted() iterates character by character, passing each to get_priority().
# get_priority('S') -> Returns Tuple: (1, 'S')
# get_priority('g') -> Returns Tuple: (0, 'g')
# get_priority('1') -> Returns Tuple: (2, '1')
# get_priority('2') -> Returns Tuple: (3, '2')

# Python compares the tuples: 
# (0, 'g') is prioritized over (1, 'S').
# If priorities match (e.g., (0, 'g') and (0, 'i')), Python breaks the tie 
# using the character itself ('g' comes before 'i' alphabetically).

# --- Final Assembly ---
# sorted() returns: ['g', 'i', 'n', 'o', 'r', 't', 'S', '1', '3', '2', '4']
# "".join() binds it together.
# Console Prints: ginortS1324