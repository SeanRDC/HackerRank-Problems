# ==========================================
# SET 1: SET DELETION MECHANICS
# ==========================================

# Problem 1: Create a set from a mock list of numbers and print it.
# Mock Input: my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Problem 2: Use the `.remove()` method to delete the number `9` from your set. Print the set.
# Mock Input: my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Expected Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Problem 3: Use the `.discard()` method to delete the number `99` (which doesn't exist) from your set. Print the set. 
# Notice how the code doesn't crash! (If you tried this with .remove(99), it would throw a KeyError).
# Mock Input: my_set = {1, 2, 3, 4, 5, 6, 7, 8}
# Expected Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Problem 4: Use the `.pop()` method to remove an arbitrary element from your set. Print the set.
# Mock Input: my_set = {1, 2, 3}
# Expected Output: {2, 3} (Note: sets are unordered, but pop usually removes the "first" item in memory)

# Problem 5 (MINI-BOSS: COMBINE 1-4):
# Given `boss_set`, perform these exact actions in order: .remove(4), .discard(10), .pop(). 
# Then, print the SUM of the remaining elements.
# Mock Input: boss_set = {1, 2, 3, 4}
# Expected Output: 5 (Because 4 is removed, 10 does nothing, pop removes 1. Remaining: {2, 3}. Sum = 5)


# ==========================================
# SET 2: PARSING STRING COMMANDS
# ==========================================
# HackerRank gives us commands as raw text strings (e.g., "remove 9"). We need to chop them up.

# Problem 6: Given a mock input string, use `.split()` to break it into a list of strings. Print the list.
# Mock Input: raw_input = "remove 9"
# Expected Output: ['remove', '9']

# Problem 7: Extract just the command word (the first item in the split list) and save it to a variable `cmd`. Print `cmd`.
# Mock Input: split_list = ['remove', '9']
# Expected Output: remove

# Problem 8: Extract the number (the second item in the split list), convert it to an `int`, and save it to `target`. Print `target`.
# Mock Input: split_list = ['remove', '9']
# Expected Output: 9

# Problem 9: What if the command is just "pop"? Split it, and print the length of the resulting list.
# Mock Input: raw_input = "pop"
# Expected Output: 1 (This tells us there is no target number to extract!)

# Problem 10 (MINI-BOSS: COMBINE 6-9):
# Given `boss_input`, split the string. Save index 0 to `cmd`. 
# Using an `if` statement based on the length of the split list, extract index 1 as an integer to `target` (if it exists). 
# If the length is only 1, set `target = None`. Print `cmd` and `target`.
# Mock Input 1: boss_input = "discard 5" -> Expected Output: discard, 5
# Mock Input 2: boss_input = "pop" -> Expected Output: pop, None


# ==========================================
# SET 3: EXECUTING COMMANDS DYNAMICALLY
# ==========================================

# Use this mock setup for Problems 11-14:
# active_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Problem 11: Write an `if` statement: if `cmd == "remove"`, execute `active_set.remove(target)`. 
# Mock Input: cmd = "remove", target = 9, active_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Expected Output of active_set: {1, 2, 3, 4, 5, 6, 7, 8}

# Problem 12: Add an `elif` statement: if `cmd == "discard"`, execute `active_set.discard(target)`.
# Mock Input: cmd = "discard", target = 8, active_set = {1, 2, 3, 4, 5, 6, 7, 8}
# Expected Output of active_set: {1, 2, 3, 4, 5, 6, 7}

# Problem 13: Add an `elif` statement: if `cmd == "pop"`, execute `active_set.pop()`. (No target needed!)
# Mock Input: cmd = "pop", active_set = {1, 2, 3, 4, 5, 6, 7}
# Expected Output of active_set: {2, 3, 4, 5, 6, 7}

# Problem 14: Put your if/elif/elif logic inside a function or a block of code, and print the active_set.

# Problem 15 (MINI-BOSS: COMBINE PARSING + EXECUTION):
# Loop through a list of raw string commands. For each string: split it, figure out the `cmd` and `target`, 
# and use your if/elif/elif block to update `boss_set`. Print the SUM of `boss_set` at the end.
# Mock Input: 
# boss_set = {1, 2, 3, 4, 5}
# commands = ["remove 5", "pop", "discard 4"]
# Expected Output: 5 (Removes 5, pops 1, discards 4. Remaining: {2, 3}. Sum = 5)


# ==========================================
# SET 4: THE GRAND FINALE (HACKERRANK READY)
# ==========================================

# Problem 16: Read `n` (the number of elements). You know the drill from the runner-up score problem: 
# capture it, but you don't actually need to use it!
# Mock Input: n = int("9")

# Problem 17: Read the space-separated elements, split them, convert to ints, and turn them into a `set` called `s`.
# Mock Input: elements_string = "1 2 3 4 5 6 7 8 9"
# Expected Output of `s`: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Problem 18: Read the number of commands, `N`.
# Mock Input: N = int("10")

# Problem 19: Write a `for` loop using `range(N)` that takes a single `input()` on each iteration. 
# (Just print the input for now to prove it works).
# Mock Input: N = 2, inputs = "pop", "remove 9"
# Expected Output: pop \n remove 9

# Problem 20 (THE GRAND FINALE):
# Put it all together using the full HackerRank Sample Input! 
# Build the set, loop N times, parse the input string, extract the command/target, execute the set method, and print `sum(s)`!
# Mock Input: 
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5
# Expected Output: 4