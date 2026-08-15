# ==============================================================================
# CHALLENGE: MAXIMIZE IT!
# ==============================================================================
# Goal: 
# You have K lists. You must pick exactly ONE number from each list.
# You square each of the numbers you picked, add them together, and find the 
# modulo (%) of that sum against a given number M.
# You want to find the combination that gives the absolute HIGHEST modulo result.
# ==============================================================================

# ---------------------------------------------------------
# PHASE 1: THE CARTESIAN PRODUCT
# ---------------------------------------------------------

# Problem 1: The Import
# Concept: We need a tool to generate every possible combination of picking one 
# item from multiple lists. 
# Write the code to import `product` from the `itertools` module.
from itertools import product
# Problem 2: Mocking the Lists
# Concept: Create two simple lists to test the product tool. 
# `list1 = [5, 4]` and `list2 = [7, 8]`.
list1 = [5, 4]
list2 = [7, 8]
# Problem 3: Generating Combinations
# Concept: Use `product(list1, list2)` to generate the combinations. Wrap the 
# whole thing in `list()` so we can see the output, and print it.
# Mock Output: [(5, 7), (5, 8), (4, 7), (4, 8)]
# Notice how it gives us every possible way to pick one from each list!
print(list(product(list1, list2)))
# ---------------------------------------------------------
# PHASE 2: THE MATH ENGINE
# ---------------------------------------------------------

# Problem 4: The Mock Combo
# Concept: Assume our product generator just gave us this specific combination.
# Create a variable: `combo = (5, 9, 10)` and a modulo variable `M = 1000`.

# Problem 5: Squaring the Elements
# Concept: We need to square every number in that combination. 
# Write a list comprehension that squares each `x` in `combo`.
# Mock Output: [25, 81, 100]

# Problem 6: Summing the Squares
# Concept: Wrap your list comprehension from Problem 5 inside Python's built-in 
# `sum()` function to add them all together.
# Mock Output: 206

# Problem 7: Applying the Modulo
# Concept: Take the entire sum from Problem 6 and apply the modulo operator 
# (`% M`). Assign this final math equation to a variable `result` and print it.

# Problem 8: The Math Function (Optional but clean)
# Concept: Wrap the logic from Problem 7 into a quick lambda function (or standard function) 
# named `calculate_score(combo, M)` that returns the final modulo math.

# ---------------------------------------------------------
# PHASE 3: INPUT PARSING (THE TRICKY PART)
# ---------------------------------------------------------

# Problem 9: Reading K and M
# Concept: The first line of input is "3 1000". Write the code to read the 
# input, split it, convert both to integers, and assign them to `K` and `M`.

# Problem 10: The List Container
# Concept: Create an empty list called `all_lists`. We will append all our 
# parsed rows into this master list.

# Problem 11: Reading a Row
# Concept: A row looks like this: "3 7 8 9". The first number (3) just tells us 
# how many elements there are. We don't actually need it for our math!
# Create a mock string: `row_input = "3 7 8 9"`

# Problem 12: Slicing the Row
# Concept: Split `row_input` into a list of strings. Then, use Python slicing 
# (`[1:]`) to chop off that first number, leaving only `['7', '8', '9']`.

# Problem 13: Mapping to Integers
# Concept: Wrap your sliced list from Problem 12 in `map(int, ...)` and then 
# `list(...)` to convert those string numbers into real integers. 
# Save it to `parsed_row`.

# Problem 14: Appending to the Master List
# Concept: Append `parsed_row` into your `all_lists` from Problem 10.

# ---------------------------------------------------------
# PHASE 4: ASSEMBLY & THE UNPACKING OPERATOR
# ---------------------------------------------------------

# Problem 15: The K Loop
# Concept: Wrap the logic from Problems 11-14 inside a `for _ in range(K):` 
# loop to process all the lines dynamically.

# Problem 16: The Max Tracker
# Concept: Create a variable `max_score = 0`. We will use this to keep track 
# of the highest modulo result we find.

# Problem 17: Generating the Final Combinations
# How do we pass a dynamic number of lists into `product()`? We unpack them!
# Concept: Write a `for combo in product(*all_lists):` loop. The `*` unpacks 
# the lists inside `all_lists` as separate arguments for the product tool.

# Problem 18: Testing the Combo
# Concept: Inside the loop, run your `calculate_score(combo, M)` math engine 
# from Problem 8. Save it to `current_score`.

# Problem 19: The Greedy Update
# Concept: If `current_score` > `max_score`, update `max_score` to equal 
# `current_score`. (Or, more Pythonically, use `max_score = max(max_score, current_score)`).

# Problem 20: The Final Output
# Concept: After the loop finishes checking every combination, print `max_score`.