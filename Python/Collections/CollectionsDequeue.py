# ==============================================================================
# CHALLENGE: THE DEQUE (DOUBLE-ENDED QUEUE)
# ==============================================================================
# Goal: 
# A `deque` (pronounced "deck") is an optimized list that allows you to add or 
# remove items from BOTH the front and the back extremely quickly. 
# Your goal is to read a sequence of string commands (like "append 1" or "pop") 
# and execute those exact methods on a custom deque object.
#
# Test Input Breakdown:
# Line 1: `6` (This is N, the total number of operations/commands)
# Line 2: `append 1` (Add '1' to the right side of the deque)
# Line 3: `append 2` (Add '2' to the right side)
# Line 4: `append 3` (Add '3' to the right side)
# Line 5: `appendleft 4` (Add '4' to the LEFT side of the deque)
# Line 6: `pop` (Remove the right-most element)
# Line 7: `popleft` (Remove the left-most element)
#
# Constraints & Nuances:
# Commands can be TWO words (requiring a value) or ONE word (no value needed).
# At the end, you must print the remaining elements of the deque, space-separated.
# ==============================================================================

# ---------------------------------------------------------
# PHASE 1: INITIALIZATION
# ---------------------------------------------------------

# Problem 1: The Import
# We need the specialized data structure. Write the code to import `deque` 
# from the built-in `collections` module.
from collections import deque
# Problem 2: The Deque Object
# Create a new, empty deque and assign it to a variable named `d`.
d = deque()
# ---------------------------------------------------------
# PHASE 2: STRING PARSING (TWO-WORD COMMANDS)
# ---------------------------------------------------------

# Problem 3: Two-Word Mock Input
# Create a variable named `mock_cmd_1` and set it to the string: "append 5"
mock_cmd_1 = "append 5"
# Problem 4: Splitting the Command
# Use a built-in string method to split `mock_cmd_1` by its space. 
# Save the resulting list to a variable named `cmd_parts_1`.
# Mock Output: ['append', '5']
cmd_parts_1 = mock_cmd_1.split()
# Problem 5: Extracting the Action
# Grab the very first item from your `cmd_parts_1` list and save it to `action`.
action = cmd_parts_1[0]
# Problem 6: Extracting the Value
# Grab the second item from the list. Since deque elements need to be printed 
# as strings later, you can actually keep this as a string instead of converting to int! 
# Save it to a variable named `value`.
value = cmd_parts_1[-1]
# Problem 7: Length Checking (The Two-Word Case)
# Write an `if` statement to check if the length of your `cmd_parts_1` list is exactly 2.
if len(cmd_parts_1) == 2:
# Problem 8: Executing "append"
# Inside your `if` block, check if the `action` is exactly equal to "append". 
# If it is, use the native deque append method to add `value` to `d`.
    if action == "append":
        d.append(value)
# Problem 9: Executing "appendleft"
# Inside the same `if` block, add an `elif` to check if `action` is "appendleft".
# If true, use the native deque appendleft method to add `value` to `d`.
elif action == "appendleft":
    d.appendleft(value)
print(f"Test case 1: {d}")
# ---------------------------------------------------------
# PHASE 3: STRING PARSING (ONE-WORD COMMANDS)
# ---------------------------------------------------------

# Problem 10: One-Word Mock Input
# Create a variable named `mock_cmd_2` and set it to the string: "pop"
mock_cmd_2 = "pop"
# Problem 11: Splitting the Single Command
# Split `mock_cmd_2` by spaces and save it to `cmd_parts_2`.
# Mock Output: ['pop']
cmd_parts_2 = mock_cmd_2.split()
# Problem 12: Length Checking (The One-Word Case)
# Write an `if` statement to check if the length of `cmd_parts_2` is exactly 1.
if len(cmd_parts_2) == 1:
# Problem 13: Re-Extracting Action
# Inside this `if` block, grab the first (and only) item from `cmd_parts_2` 
# and save it to `action`.
    action = cmd_parts_2[0]
# Problem 14: Executing "pop"
# Inside the same `if` block, check if `action` is equal to "pop".
# If true, execute the native pop method on your deque `d`. (No value needed!)
    if action == "pop":
        d.pop()
# Problem 15: Executing "popleft"
# Still inside, add an `elif` to check if `action` is equal to "popleft".
# If true, execute the native popleft method on `d`.
elif action == "popleft":
    d.popleft()
print(f"Test case 2: {d}")
# ---------------------------------------------------------
# PHASE 4: THE MASTER LOOP
# ---------------------------------------------------------
de = deque()
# Problem 16: The N Variable
# Imagine moving to standard input. Read the first line of input, convert it to 
# an integer, and save it to a variable `N`.
N = int(input())
# Problem 17: The Loop
# Write a loop that will run exactly `N` times.
for _ in range(N):
# Problem 18: Reading the Command
# Inside the loop, read the next line of standard input and save it to `raw_cmd`.
    raw_cmd = input().split()
# Problem 19: The Master Logic Engine
# Inside the loop, split `raw_cmd` into a list. 
# Combine the length-checking logic from Phases 2 and 3 into a single, cohesive 
# if/else structure to dynamically process whatever command was passed in!
    if len(raw_cmd) == 2:
        command = raw_cmd[0]
        val = raw_cmd[1]
        if command == 'append':
            de.append(val)
        elif command == 'appendleft':
            de.appendleft(val)
    if len(raw_cmd) == 1:
        commands = raw_cmd[0]
        if commands == 'pop':
            de.pop()
        elif commands == 'popleft':
            de.popleft()
print(*de)

# ---------------------------------------------------------
# PHASE 5: PRINTING THE DEQUE
# ---------------------------------------------------------

# Problem 20: The Unpacking Operator
# Once the loop finishes, we need to print the deque. 
# In Python, you can print elements of an iterable separated by spaces by placing 
# an asterisk (*) directly in front of the variable name inside the print statement.
# Write the print statement using this unpacking operator on `d`.
# Mock Input: deque(['1', '2'])
# Expected Output: 1 2

# ==============================================================================
# FINAL SUBMISSION
# ==============================================================================
# Summary:
# By checking the length of the split input string, you can safely determine 
# whether you need to extract a value (index 1) or just execute an action (index 0).
# Wiring this logic inside an N-loop gives you a perfectly functioning command parser.
#
# Mock Input (Stdin):
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft
#
# Expected Output:
# 1 2
# ==============================================================================

de = deque()
N = int(input())
for _ in range(N):
    raw_cmd = input().split()
    if len(raw_cmd) == 2:
        command = raw_cmd[0]
        val = raw_cmd[1]
        if command == 'append':
            de.append(val)
        elif command == 'appendleft':
            de.appendleft(val)
    if len(raw_cmd) == 1:
        commands = raw_cmd[0]
        if commands == 'pop':
            de.pop()
        elif commands == 'popleft':
            de.popleft()
print(*de)

# Optimized version
di = deque()
n = int(input())
for _ in range(n):
    cmd = input().split()
    if len(cmd) == 2:
        act = cmd[0]
        num = cmd[1]
        getattr(di, act)(num)
    elif len(cmd) == 1:
        acts = cmd[0]
        getattr(di, acts)()
print(*di)