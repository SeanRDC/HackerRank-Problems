# ==========================================
# SET 1: UNDERSTANDING PERMUTATIONS
# ==========================================
# Let's see what the permutations function actually spits out.

# MOCK INPUT:
# S = "HACK"
# k = 2

# Problem 1: Import the `permutations` function from the `itertools` module.

# Problem 2: Create the mock variables `S` and `k`.

# Problem 3: Call `permutations(S, k)`, wrap it in `list()`, and save it to `perms`.

# Problem 4: Print `perms`.
# EXPECTED OUTPUT: [('H', 'A'), ('H', 'C'), ('H', 'K'), ('A', 'H'), ...]
# Notice how it starts with 'H' because 'H' is the first letter in "HACK".


# ==========================================
# SET 2: THE SORTING SECRET
# ==========================================
# HackerRank demands alphabetical order. If we sort the string first, 
# itertools will automatically generate the permutations in alphabetical order!

# Problem 5: Use the built-in `sorted()` function on `S` and print it.
# EXPECTED OUTPUT: ['A', 'C', 'H', 'K']

# Problem 6: Generate the permutations again, but this time pass `sorted(S)` 
# instead of `S`. Set the length to `k`. Wrap it in `list()` and save it to `sorted_perms`.

# Problem 7: Print `sorted_perms`.
# EXPECTED OUTPUT: [('A', 'C'), ('A', 'H'), ('A', 'K'), ('C', 'A'), ...]
# Boom! Alphabetical order.


# ==========================================
# SET 3: FORMATTING THE OUTPUT
# ==========================================
# We have tuples like ('A', 'C'), but HackerRank wants clean strings like AC on new lines.
# We cannot use the `print(*list)` asterisk trick here because it prints on one line!

# Problem 8: Write a `for` loop that iterates through each `tuple_item` in `sorted_perms`.

# Problem 9: Inside the loop, use `"".join()` to combine the characters of `tuple_item` 
# into a single string. 

# Problem 10: Print that joined string.
# EXPECTED OUTPUT:
# AC
# AH
# AK
# ...and so on.


# ==========================================
# SET 4: PARSING HACKERRANK'S SINGLE-LINE INPUT
# ==========================================
# HackerRank doesn't give us `S` and `k` on separate lines. It gives us: "HACK 2".

# MOCK INPUT:
# mock_input = "HACK 2"

# Problem 11: Create the `mock_input` variable.

# Problem 12: Use `.split()` on `mock_input` and save the resulting list to `parsed`.
# (This splits it at the space into ['HACK', '2']).

# Problem 13: Assign the first item in the `parsed` list to a variable `S`.

# Problem 14: Assign the second item in the `parsed` list to a variable `k`, 
# but make sure to wrap it in `int()` so it becomes a number!

# Problem 15: Print `S` and `k` to verify they are separated and correct.


# ==========================================
# SET 5: THE GRAND FINALE
# ==========================================
# Let's put it all together into a clean script.

# TERMINAL MOCK INPUT:
# HACK 2

# Problem 16: Ensure your `import` statement is at the top.

# Problem 17: Take user input using `input().split()` and assign it to `parsed`.
# PRO-TIP SHORTCUT: You can do this in one line: `S, k = input().split()`!

# Problem 18: Convert `k` to an integer.

# Problem 19: Write a `for` loop that iterates directly over `permutations(sorted(S), k)`.
# (You don't even need to save it to a list variable first!)

# Problem 20: Inside the loop, print the `"".join()` of each permutation tuple.