# ==============================================================================
# FUNDAMENTALS CURRICULUM: LAMBDA FUNCTIONS & THE FIBONACCI ALGORITHM
# ==============================================================================
# Goal: Write a lambda function that cubes a given number. Then, write a 
# function that generates a list of the first `N` Fibonacci numbers. The provided 
# boilerplate will use `map()` to apply your lambda to your generated list.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: THE TRANSFORMATION ENGINE (LAMBDA)
# ---------------------------------------------------------

# Problem 1: The Anonymous Concept
# Concept: A lambda function is just a function without a name. The boilerplate 
# assigns it to the variable `cube = lambda x: ...`. The `x` represents the 
# single element being passed in.

# Problem 2: The Implicit Return
# Concept: Unlike a standard `def` block, `lambda` does not use the `return` 
# keyword. Whatever expression you write after the colon is automatically returned.

# Problem 3: The Math Operation
# Concept: You need to calculate the cube of `x`. You can use the standard 
# multiplication operator three times, or Python's built-in exponent operator.

# Problem 4: Mental Sandbox for Lambda
# Concept: If the system evaluates `cube(3)`, what will your expression calculate?
# Mock Input: x = 3
# Mock Output: 27
x = 3
def cube1(x):
    return x**3
print(cube1(x)) 

# ---------------------------------------------------------
# CONCEPT BLOCK 2: FIBONACCI - THE RULES AND EDGE CASES
# ---------------------------------------------------------

# Problem 5: The Fibonacci Rule
# Concept: The Fibonacci sequence starts with 0 and 1. Every subsequent number 
# is the sum of the two numbers immediately preceding it.
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13...

# Problem 6: The N=0 Edge Case Trap
# Concept: HackerRank will test an input of `0`. If asked for zero Fibonacci 
# numbers, your function must not return `[0]`; it must return an empty list.
# Mock Input: n = 0
# Mock Output: []

# Problem 7: The N=1 Edge Case
# Concept: If asked for exactly 1 Fibonacci number, the list only contains the 
# starting number.
# Mock Input: n = 1
# Mock Output: [0]

# Problem 8: Handling the Edge Cases First
# Concept: Inside `def fibonacci(n):`, set up conditional checks (`if`, `elif`) 
# to immediately return the correct lists for the `0` and `1` edge cases before 
# doing any heavy lifting.
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]

print(fibonacci(1))
print(fibonacci(0))
# ---------------------------------------------------------
# CONCEPT BLOCK 3: FIBONACCI - THE GENERATOR ENGINE
# ---------------------------------------------------------

# Problem 9: The Base State
# Concept: If `n` is greater than 1, we can safely initialize our sequence with 
# the first two numbers. Create a standard list variable holding these two integers.
# Mock State: current_list = [0, 1]
current_list = [0, 1]
# Problem 10: The Iteration Goal
# Concept: If `n = 5`, and our list already has 2 elements, we only need to 
# calculate 3 more numbers. We need a loop that runs exactly `n - 2` times.
n = 5
for j in range(n -2):
# Problem 11: Accessing the End of the List
# Concept: Inside your loop, you need to grab the last item added to the list. 
# Remember that negative indexing (like `-1`) allows you to grab the item at 
# the very end without needing to know the list's total length.
    last = current_list[-1]
# Problem 12: Accessing the Second-to-Last Item
# Concept: You also need the item right before it. What negative index grabs 
# the second-to-last item?
    slast = current_list[-2]
# Problem 13: The Addition Math
# Concept: Add the value from Problem 11 and the value from Problem 12 together 
# to create the `next_number`.
    next_number = last + slast
# Problem 14: Growing the Sequence
# Concept: Append the newly calculated `next_number` to your list variable.
    current_list.append(next_number)
# Problem 15: Returning the Sequence
# Concept: Once the loop finishes, return the final list.
# Mock Input (n=5): List initializes as [0, 1]. Loop runs 3 times.
# Loop 1: Adds 0 + 1. Appends 1. List is [0, 1, 1].
# Loop 2: Adds 1 + 1. Appends 2. List is [0, 1, 1, 2].
# Loop 3: Adds 1 + 2. Appends 3. List is [0, 1, 1, 2, 3].
# Mock Output: [0, 1, 1, 2, 3]
n = 10
current_list = [0, 1]
for i in range(n - len(current_list)):
    current_list.append(current_list[-1] + current_list[-2])
print(current_list)

# ---------------------------------------------------------
# CONCEPT BLOCK 4: UNDERSTANDING THE BOILERPLATE'S MAP()
# ---------------------------------------------------------

# Problem 16: The Function Call
# Concept: The boilerplate evaluates `fibonacci(5)` and gets your list back.

# Problem 17: The Map Concept
# Concept: `map()` takes two things: a function (your lambda) and an iterable 
# (your list). It runs a hidden loop, passing each item from the list into the 
# function one by one.

# Problem 18: Map Iteration 1
# Concept: `map` grabs index 0 of your list (the number 0) and passes it to `cube`.
# Result: 0

# Problem 19: Map Iteration 5
# Concept: `map` grabs index 4 of your list (the number 3) and passes it to `cube`.
# Result: 27

# Problem 20: The Final Cast
# Concept: `map` returns a hidden generator object to save memory (just like `zip`). 
# The boilerplate wraps it in `list()` to force it to calculate all the values 
# immediately, then prints the final transformed array.

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Input Stage ---
# Standard Input reads the string "5"
# Boilerplate casts "5" to Integer.

# --- Sequence Generation Phase ---
# Boilerplate calls fibonacci(5).
# Function checks N=0 (False).
# Function checks N=1 (False).
# Function initializes list with [0, 1].
# Loop evaluates length needed. Calculates three new numbers: 1, 2, 3.
# Appends sequentially.
# Function returns array: [0, 1, 1, 2, 3]

# --- Mapping Phase ---
# Boilerplate sets up map with the cube lambda.
# Engine isolates index 0 -> Value 0 -> evaluates 0^3 -> Yields 0
# Engine isolates index 1 -> Value 1 -> evaluates 1^3 -> Yields 1
# Engine isolates index 2 -> Value 1 -> evaluates 1^3 -> Yields 1
# Engine isolates index 3 -> Value 2 -> evaluates 2^3 -> Yields 8
# Engine isolates index 4 -> Value 3 -> evaluates 3^3 -> Yields 27

# --- Output Stage ---
# Boilerplate casts yielded values into a single array structure.
# Console Prints: [0, 1, 1, 8, 27]
cube = lambda x: x**3

n = 5
def fibo(n):
    cur = [0, 1]
    if n == 0:
        return []
    if n == 1:
        return [0]

    for _ in range(n - len(cur)):
        cur.append(cur[-1] + cur[-2])
    return cur

print(list(map(cube, fibo(n))))