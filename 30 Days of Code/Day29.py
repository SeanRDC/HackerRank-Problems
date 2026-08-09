# ==============================================================================
# CHALLENGE: BITWISE AND
# ==============================================================================
# Goal: 
# You are given a sequence of integers from 1 to N[cite: 1].
# You need to find two integers, A and B, from this sequence such that A < B.
# Your goal is to maximize the result of the bitwise AND operation (A & B)[cite: 1].
# The absolute catch: This maximum result MUST be strictly less than a given integer K.
#
# Test Input Breakdown:
# N = 5, K = 2
# Sequence = {1, 2, 3, 4, 5}
# Possible pairs (A, B) and their Bitwise AND (A & B):
# (1, 2) -> 1 & 2 = 0
# (1, 3) -> 1 & 3 = 1
# (1, 4) -> 1 & 4 = 0
# (2, 3) -> 2 & 3 = 2
# The max value strictly less than K (which is 2) is 1.
#
# Constraints & Nuances:
# A standard nested loop checking every single pair (O(N^2)) will result in a 
# Time Limit Exceeded (TLE) error on HackerRank because T and N are large. 
# We must solve this mathematically in O(1) constant time using bitwise properties!
# ==============================================================================

# ---------------------------------------------------------
# PHASE 1: BITWISE FUNDAMENTALS
# ---------------------------------------------------------

# Problem 1: Binary Conversion
# To understand bitwise logic, we must look at binary. 
# Concept: Use the built-in Python function to convert the integer 4 into a binary string.
# Mock Output: '0b100'
print(bin(4))

# Problem 2: Binary Conversion II
# Concept: Convert the integer 5 into a binary string.
# Mock Output: '0b101'
print(bin(5))

# Problem 3: Bitwise AND
# The Bitwise AND operator (&) compares bits. If both bits are 1, it results in 1. Otherwise, 0.
# Concept: Write an expression that performs a bitwise AND on the integers 4 and 5. 
# (Mentally compare 100 & 101).
# Mock Output: 4 (Because 100 & 101 = 100)
print(bin(4 & 5))
print(4 & 5)

# Problem 4: Bitwise OR
# The Bitwise OR operator (|) compares bits. If AT LEAST one bit is 1, it results in 1.
# Concept: Write an expression that performs a bitwise OR on the integers 4 and 5.
# (Mentally compare 100 | 101).
# Mock Output: 5 (Because 100 | 101 = 101)
print(bin(4 | 5))
print(4 | 5)

# ---------------------------------------------------------
# PHASE 2: THE THEORETICAL MAXIMUM
# ---------------------------------------------------------

# Problem 5: The Highest Possible Answer
# We need to find the maximum possible result strictly less than K. 
# Mathematically, what is the absolute highest integer that is strictly less than K?
# Concept: Create a variable `K` and set it to 5. Then create a variable `target` 
# that represents this highest possible answer relative to `K`.
K = 5
target = K - 1

# Problem 6: Checking the Target
# Concept: Print your `target` variable from Problem 5.
# Mock Output: 4
print(target)

# Problem 7: The Optimal Pair Rule
# To achieve our `target` using `target & B = target`, the integer `B` must contain 
# ALL the 1-bits that `target` has, plus at least one more to make it larger than `target`.
# The absolute smallest integer greater than `target` that satisfies this is `target | (target + 1)`.
# Concept: Since `target` is `K - 1`, then `target + 1` is simply `K`. 
# Write an expression that calculates `target | K`. Save this to a variable `optimal_B`.
optimal_B = target | K

# Problem 8: Checking the Optimal Pair
# Concept: Print your `optimal_B` variable to see the smallest integer we can pair with `target`.
# Mock Input (K=5, target=4): 4 | 5
# Mock Output: 5
print(optimal_B)

# ---------------------------------------------------------
# PHASE 3: THE UPPER BOUNDARY CHECK
# ---------------------------------------------------------

# Problem 9: Setting the Upper Limit
# We have a sequence that only goes up to `N`. 
# Concept: Create a variable `N` and set it to 8. 
N = 8

# Problem 10: Validating the Optimal Pair
# We know our `target` is perfectly achievable IF our `optimal_B` is actually in the sequence.
# Concept: Write an `if` statement that checks if `optimal_B` is less than or equal to `N`.
if optimal_B <= N:

# Problem 11: Setting the Result
# Concept: Inside that `if` block, create a variable `result` and assign it the value of `target`.
    result = target
    
# Problem 12: A Failing Scenario
# Let's test a scenario where the boundary fails. 
# Concept: Create variables `K_fail = 2` and `N_fail = 2`.
K_fail = 2
N_fail = 2

# Problem 13: Recalculating Target for Failure Case
# Concept: Calculate the `target_fail` for `K_fail` (which is K_fail - 1). 
# Mock Output: 1
target_fail = K_fail - 1

# Problem 14: Recalculating Optimal B for Failure Case
# Concept: Calculate `optimal_B_fail` using the bitwise OR rule from Problem 7 
# (target_fail | K_fail).
# Mock Output (1 | 2): 3
optimal_B_fail = target_fail | K_fail
print(optimal_B_fail)

# ---------------------------------------------------------
# PHASE 4: THE MATHEMATICAL FALLBACK
# ---------------------------------------------------------

# Problem 15: The Boundary Fails
# Concept: Write an `if` statement checking if `optimal_B_fail` is less than or equal to `N_fail`.
# (Since 3 is not <= 2, this condition will evaluate to False).

# Problem 16: The Mathematical Fallback
# If `optimal_B` is greater than `N`, it is mathematically impossible to pair our `target` 
# with anything in the sequence. A mathematical theorem for this specific problem proves 
# that if `K - 1` fails, the absolute maximum valid result is ALWAYS exactly `K - 2`.
# Concept: Create a variable `fallback_result` and set it to `K_fail - 2`.
# Mock Output: 0

# ---------------------------------------------------------
# PHASE 5: THE FINAL LOGIC ENGINE
# ---------------------------------------------------------

# Problem 17: Function Definition
# Concept: Define a function named `bitwiseAnd` that accepts two parameters: `N` and `K`.

# Problem 18: Isolate the Target inside the Function
# Concept: Inside the function, calculate the `target` (which is K - 1) and save it to a variable.

# Problem 19: Calculate Optimal B inside the Function
# Concept: Inside the function, calculate the optimal pairing integer using the 
# Bitwise OR rule (target | K) and save it to a variable.

# Problem 20: The Master Return Statement
# Concept: Use an `if/else` block (or a one-line ternary return) to return the `target` 
# IF the optimal pairing integer is less than or equal to `N`. ELSE, return `K - 2`.

# ==============================================================================
# FINAL SUBMISSION
# ==============================================================================
# Summary:[cite: 1]
# By understanding the bitwise OR relationship, we can bypass nested loops entirely.
# The maximum possible answer is ALWAYS `K - 1`, as long as the smallest compatible 
# matching pair `(K - 1) | K` does not exceed the sequence limit `N`. If it does 
# exceed `N`, the maximum possible answer is mathematically proven to be `K - 2`. 
# This reduces an O(N^2) operation to O(1) constant time!
#
# Mock Input (Stdin):
# 3
# 5 2
# 8 5
# 2 2
#
# Expected Output:
# 1
# 4
# 0
# ==============================================================================