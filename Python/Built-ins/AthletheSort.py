# ==============================================================================
# FUNDAMENTALS CURRICULUM: 2D ARRAYS & CUSTOM SORTING (LAMBDA)
# ==============================================================================
# Goal: Take a 2D array of athlete data, sort it based on a specific target 
# column (k) using a custom key, and print the resulting rows seamlessly.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: UNDERSTANDING 2D ARRAYS
# ---------------------------------------------------------

# Problem 1: The Mock Spreadsheet
# Concept: Create a mock 2D array representing the HackerRank sample data.
# `arr = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]`

# Problem 2: Accessing a Row
# Concept: A 2D array is just a list of lists. 
# Print `arr[0]` to view the details of the first athlete.
# Mock Output: [10, 2, 5]

# Problem 3: Accessing an Attribute
# Concept: To get a specific attribute, you chain the indices. 
# Print `arr[0][1]` to view the 2nd attribute (index 1) of the 1st athlete.
# Mock Output: 2

# ---------------------------------------------------------
# CONCEPT BLOCK 2: NAIVE SORTING
# ---------------------------------------------------------

# Problem 4: The Default Sort
# Concept: What happens if we just sort the array without instructions?
# Call `sorted(arr)` and assign it to `naive_sort`. Print it.

# Problem 5: Evaluating Naive Sort
# Concept: Notice how `naive_sort` arranged the data? 
# It automatically sorted by the 0th index (1, 6, 7, 9, 10). If there were ties, 
# it would check the 1st index, and so on. We need to override this behavior!

# ---------------------------------------------------------
# CONCEPT BLOCK 3: LAMBDA FUNCTIONS (THE ANONYMOUS ENGINE)
# ---------------------------------------------------------

# Problem 6: The Key Parameter
# Concept: Python's `sort()` and `sorted()` functions have an optional parameter 
# called `key`. It accepts a function that tells Python exactly what value to 
# look at when sorting.

# Problem 7: Creating a Standard Function
# Concept: Create a normal function called `get_second_element(row)`. 
# Have it return `row[1]`. 

# Problem 8: The Lambda Alternative
# Concept: Writing a full function just for a sort key is tedious. 
# Python has "lambda" functions (anonymous, one-line functions).
# The equivalent of Problem 7 is: `lambda row: row[1]`.

# Problem 9: Testing the Lambda
# Concept: Assign `my_lambda = lambda row: row[1]`. 
# Pass `arr[0]` into `my_lambda(arr[0])` and print it. 
# Mock Output: 2 (It successfully extracted the target attribute!)

# ---------------------------------------------------------
# CONCEPT BLOCK 4: CUSTOM SORTING 
# ---------------------------------------------------------

# Problem 10: The Custom Sort
# Concept: Pass your lambda function directly into the `key` parameter of 
# the `sorted()` function: `sorted(arr, key=lambda row: row[1])`.
# Assign this to `custom_sort` and print it.
# Mock Output: [[7, 1, 0], [10, 2, 5], [6, 5, 9], [9, 9, 9], [1, 23, 12]]
# (Notice how it is now perfectly sorted by the middle column!)

# Problem 11: Dynamic Sorting Variables
# Concept: Instead of hardcoding `1`, we need to use the variable `k` provided 
# by HackerRank. Create `k = 1`. Write a new lambda: `lambda row: row[k]`.

# Problem 12: The Stability Guarantee
# Concept: HackerRank explicitly states: "If two attributes are the same... 
# print the row that appeared first". This is called a "Stable Sort".
# Good news: Python's built-in Timsort algorithm is 100% stable by default! 
# You don't have to write any extra code to handle ties.

# ---------------------------------------------------------
# CONCEPT BLOCK 5: OUTPUT FORMATTING (THE UNPACKING ASTERISK)
# ---------------------------------------------------------

# Problem 13: The Iteration
# Concept: We need to print each row of our `custom_sort` array on a new line. 
# Write a `for row in custom_sort:` loop.

# Problem 14: The Raw Print
# Concept: Inside the loop, print `row`.
# Mock Output: [7, 1, 0] (This includes the brackets and commas. HackerRank 
# will reject this!)

# Problem 15: Manual Indexing (The Hard Way)
# Concept: You could format it using f-strings: `f"{row[0]} {row[1]} {row[2]}"`.
# But what if there are 20 columns? This breaks.

# Problem 16: The Asterisk Unpacker
# Concept: Python has a magic unpacking operator: `*`. 
# When placed in front of a list inside a function call, it unpacks the list 
# into individual arguments! 
# Inside your loop, change your print statement to `print(*row)`.
# Mock Output: 7 1 0 (Perfect space-separated values!)

# ---------------------------------------------------------
# CONCEPT BLOCK 6: FINAL ASSEMBLY PREP
# ---------------------------------------------------------

# Problem 17: The HackerRank Boilerplate
# Concept: Review the boilerplate. They already mapped everything into the 
# `arr` variable and gave you the target column in the `k` variable.

# Problem 18: In-Place vs New List
# Concept: You can use `arr = sorted(arr, key=...)` OR you can sort the list 
# in-place to save memory using the list method: `arr.sort(key=...)`.

# Problem 19: The Final Loop
# Concept: After triggering the sort, write your `for` loop to iterate 
# through `arr`.

# Problem 20: Clean Code Execution
# Concept: Inside the loop, use the `*` unpacker in your print statement. 
# You only need to add exactly 3 lines of code below the boilerplate!

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- The Boilerplate Parsing ---
# Loops 5 times parsing inputs into `arr`.
# arr = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
# k = 1

# --- The Sorting Engine ---
# arr.sort(key=lambda row: row[1]) executes.
# Evaluates row 1: returns 2
# Evaluates row 2: returns 1
# Evaluates row 3: returns 9
# Evaluates row 4: returns 23
# Evaluates row 5: returns 5
#
# Python sorts based on those returned keys: 1, 2, 5, 9, 23.
# Array becomes: [[7, 1, 0], [10, 2, 5], [6, 5, 9], [9, 9, 9], [1, 23, 12]]

# --- The Output Engine ---
# Loop Iteration 1:
# row = [7, 1, 0]
# print(*row) -> print(7, 1, 0)
# Console Prints: 7 1 0

# Loop Iteration 2:
# row = [10, 2, 5]
# print(*row) -> print(10, 2, 5)
# Console Prints: 10 2 5

# (Process repeats for remaining rows)