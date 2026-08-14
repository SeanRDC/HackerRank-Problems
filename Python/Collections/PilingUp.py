# ==============================================================================
# CHALLENGE: PILING UP! (STACKING CUBES)
# ==============================================================================
# Goal: 
# You have a row of cubes. You must build a vertical pile by picking ONLY from
# the leftmost or rightmost available cube. 
# The golden rule of stacking: Every cube you place on top MUST be less than 
# or equal to the cube directly below it.
#
# Test Input Breakdown:
# blocks = [4, 3, 2, 1, 3, 4]
# Pick right (4) -> pile: 4
# Pick left (4)  -> pile: 4, 4
# Pick right (3) -> pile: 4, 4, 3
# Pick left (3)  -> pile: 4, 4, 3, 3
# Pick left (2)  -> pile: 4, 4, 3, 3, 2
# Pick left (1)  -> pile: 4, 4, 3, 3, 2, 1
# Result: Yes (Stacking was possible!)
#
# Logic Secret:
# You must always be greedy. At any given moment, you evaluate the left end 
# and the right end. You MUST pick the larger of the two, provided it's valid.
# If the larger of the two is strictly greater than the top of your pile, 
# stacking is mathematically impossible and fails immediately.
# ==============================================================================

# ---------------------------------------------------------
# PHASE 1: DEQUE SETUP & INSPECTION
# ---------------------------------------------------------

# Problem 1: The Import
# Concept: We need double-ended queue functionality. Write the code to import 
# `deque` from the `collections` module.
from collections import deque

# Problem 2: Creating the Deque
# Concept: Create a mock list: `mock_input = [4, 3, 2, 1, 3, 4]`. 
# Pass this list into `deque()` and assign it to a variable named `blocks`.
mock_input = [4, 3, 2, 1, 3, 4]
blocks = deque(mock_input)

# Problem 3: Inspecting Ends Without Popping
# We need to look at the ends of the deque to decide which one to take.
# Concept: Write an expression to view the leftmost element of `blocks` without removing it.
# Mock Output: 4
print(blocks[0])

# Problem 4: Inspecting the Right End
# Concept: Write an expression to view the rightmost element of `blocks` without removing it.
# Mock Output: 4
print(blocks[-1])

# ---------------------------------------------------------
# PHASE 2: THE GREEDY CHOICE & STATE
# ---------------------------------------------------------

# Problem 5: The Pile's Foundation
# Before we place the first cube, the "top of the pile" technically doesn't exist.
# To make our logic work, the first cube we pick must be <= the "top". 
# Concept: Create a variable `top_of_pile` and set it to mathematical infinity 
# using `float('inf')`. This guarantees the very first block is always valid!
top_of_pile = float('inf')
while blocks:
    # Problem 6: The Comparison
    # Concept: Write an `if/elif/else` block that compares the leftmost block 
    # and the rightmost block of your deque. 
    # Goal: We want to extract (pop) whichever side is LARGER or equal.
    if blocks:
        if blocks[0] >= blocks[-1]:

    # Problem 7: Popping the Left
    # Concept: Inside the condition where the left block is >= the right block, 
    # use the correct deque method to remove and return the left block. 
    # Save this returned value to a variable named `popped_block`.
            popped_block = blocks.popleft()
    # Problem 8: Popping the Right
    # Concept: Inside the condition where the right block is > the left block, 
    # use the correct deque method to remove and return the right block. 
    # Save this returned value to the same variable `popped_block`.
        elif blocks[-1] > blocks[0]:
            popped_block = blocks.pop()
    # ---------------------------------------------------------
    # PHASE 3: THE VALIDITY CHECK & LOOP ENGINE
    # ---------------------------------------------------------

    # Problem 9: Checking Validity
    # Concept: Now that you have `popped_block`, write an `if` statement to check 
    # if it is less than or equal to `top_of_pile`.
    if popped_block <= top_of_pile:
    # Problem 10: Updating the State
    # Concept: If the `popped_block` is valid, it becomes the new top of our pile. 
    # Inside the `if` block from Problem 9, update `top_of_pile` to equal `popped_block`.
        top_of_pile = popped_block
    # Problem 11: The Failure State
    # Concept: Add an `else` block to the condition from Problem 9. If the `popped_block` 
    # is strictly greater than `top_of_pile`, we can't stack it. 
    # Inside this `else` block, print "No".
    else:
        print("No")
    # Problem 12: Triggering the Escape
    # If stacking fails, we want to immediately stop checking this test case.
    # Concept: Right beneath your `print("No")` statement, write the command to 
    # forcefully exit a loop. (Hint: break).
        break
# Problem 13: The Master Loop
# Concept: Wrap the logic from Problems 6 through 12 inside a `while` loop 
# that runs as long as the `blocks` deque is not empty (i.e., `while blocks:`).

# Problem 14: The Pythonic Success Catch
# Did you know Python `while` loops can have an `else` statement? 
# The `else` block executes ONLY if the loop finishes naturally (meaning it 
# emptied the deque without ever hitting a `break` statement).
# Concept: Attach an `else:` block directly to the bottom of your `while` loop 
# (at the same indentation level as `while`). Inside it, print "Yes".
else:
    print("Yes")
# ---------------------------------------------------------
# PHASE 4: HACKERRANK INTEGRATION
# ---------------------------------------------------------

# Problem 15: The Test Case Loop
# HackerRank provides an integer T for the number of test cases.
# Concept: Write a `for _ in range(T):` loop to handle multiple test cases.

# Problem 16: Reading N
# Concept: Inside the T loop, read the next line of input (which is the number 
# of cubes, N). You actually don't need to use N for our deque logic, but 
# you MUST read it to clear the line. Call it `n = int(input())`.

# Problem 17: Parsing the Blocks
# Concept: Read the next line of input, split the space-separated string, 
# convert each item to an integer, and wrap the whole thing directly in `deque()`.
# Assign it to `blocks`.

# Problem 18: Resetting the Pile
# Concept: Make sure you initialize `top_of_pile = float('inf')` INSIDE the 
# T loop, so each test case starts with a fresh, empty pile.

# Problem 19: Insert the Engine
# Concept: Place your entire `while` loop logic (from Phase 3) inside the T loop, 
# right under your deque and `top_of_pile` setup.

# Problem 20: Final Polish
# Double-check your indentation. Your `for` loop manages the test cases, 
# your `while` loop empties the deque, and your `while...else` structure 
# guarantees that "Yes" or "No" prints exactly once per test case.