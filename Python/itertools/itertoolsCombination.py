# ==========================================
# SET 1: UNDERSTANDING COMBINATIONS
# ==========================================
# Let's see how combinations differ from permutations.

# MOCK INPUT:
# S = "HACK"
# k = 2

# Problem 1: Import the `combinations` function from the `itertools` module.
from itertools import combinations

# Problem 2: Create the mock variables `S` and `k`.
S = "HACK"
k = 2

# Problem 3: Call `combinations(S, k)`, wrap it in `list()`, and save it to `combs`.
combs = list(combinations(S, k))

# Problem 4: Print `combs`. 
# Notice there is no ('A', 'H') or ('C', 'H') generated because order doesn't matter!
print(combs)

# ==========================================
# SET 2: THE SORTING REQUIREMENT
# ==========================================
# Just like before, HackerRank demands alphabetical order. 

# Problem 5: Print `list(combinations(sorted(S), k))`.
# EXPECTED OUTPUT: [('A', 'C'), ('A', 'H'), ('A', 'K'), ('C', 'H'), ('C', 'K'), ('H', 'K')]
# Notice how everything is perfectly alphabetical now.
print(list(combinations(sorted(S), k)))

# ==========================================
# SET 3: THE "UP TO" SIZE K LOOP
# ==========================================
# HackerRank wants size 1 first, then size 2... all the way up to k. 
# We need an outer loop to control the size!

# Problem 6: Write a `for` loop using `i` and `range()` that starts at 1.
# What should the stop value be to ensure it includes `k`? (Hint: `k + 1`).
for i in range(1, k + 1):

# Problem 7: Inside that loop, print `list(combinations(sorted(S), i))`.
# EXPECTED OUTPUT: 
# [('A',), ('C',), ('H',), ('K',)]
# [('A', 'C'), ('A', 'H'), ('A', 'K'), ('C', 'H'), ('C', 'K'), ('H', 'K')]
    print(list(combinations(sorted(S), i)))

# ==========================================
# SET 4: FORMATTING THE OUTPUT
# ==========================================
# We have our outer loop working. Now we need to format those tuples into strings.

# Problem 8: Keep your outer loop: `for i in range(1, k + 1):`

# Problem 9: Inside the outer loop, write an inner loop: 
# `for c in combinations(sorted(S), i):`
    for c in combinations(sorted(S), i):

# Problem 10: Inside the inner loop, use `"".join()` to combine `c` into a string.
        print(''.join(c))
# Problem 11: Print that joined string!
# EXPECTED OUTPUT:
# A
# C
# H
# K
# AC
# AH
# ...and so on!


# ==========================================
# SET 5: THE GRAND FINALE
# ==========================================
# Let's assemble the final script.

# TERMINAL MOCK INPUT:
# HACK 2

# Problem 12: Ensure your `import` statement is at the top.

# Problem 13: Take user input using the 1-line unpacking trick: `S, k = input().split()`

# Problem 14: Convert `k` to an integer.

# Problem 15: Sort the string `S` and save it to a variable `sorted_S` so you don't 
# have to re-sort it every time the loop runs. (Efficiency!)

# Problem 16: Write your outer `for` loop to handle the sizes from `1` to `k` (inclusive).

# Problem 17: Write your inner `for` loop to iterate through the combinations for that size.

# Problem 18: Inside the inner loop, print the joined string.

# Problem 19: Double-check your indentation. Your inner loop should be indented once, 
# and your print statement should be indented twice.

# Problem 20: Marvel at the fact that you just solved a complex combinatorics problem 
# in about 6 lines of code.
from itertools import combinations
S, k = input().split()
k = int(k)

sorted_S = sorted(S)
for i in range(1, k + 1):
    for j in list(combinations(sorted_S, i)):
        print(''.join(j))