# ==========================================
# SET 1: UNDERSTANDING REPLACEMENT
# ==========================================
# Let's see how this differs from standard combinations.

# MOCK INPUT:
# S = "HACK"
# k = 2

# Problem 1: Import `combinations_with_replacement` from the `itertools` module.
from itertools import combinations_with_replacement
# Problem 2: Create the mock variables `S` and `k`.
S = "HACK"
k = 2

# Problem 3: Call `combinations_with_replacement(S, k)`, wrap it in `list()`, 
# and save it to `cwr`.
cwr = list(combinations_with_replacement(S, k))

# Problem 4: Print `cwr`. 
# Notice that ('H', 'H') and ('A', 'A') exist! Standard combinations would never allow that.
print(cwr)

# ==========================================
# SET 2: THE SORTING REQUIREMENT (AGAIN)
# ==========================================
# HackerRank needs alphabetical order. Just like before, we sort first.

# Problem 5: Use `sorted()` on `S` and save it to `sorted_S`.
sorted_S = sorted(S)

# Problem 6: Run the function again using `sorted_S` and `k`. Wrap it in `list()` 
# and save it to `sorted_cwr`.
sorted_cwr = list(combinations_with_replacement(sorted_S, k))

# Problem 7: Print `sorted_cwr`.
print(sorted_cwr)

# Problem 8: Verify your output starts with ('A', 'A') and ('A', 'C').


# ==========================================
# SET 3: DROPPING THE OUTER LOOP
# ==========================================
# In the last challenge, you needed an outer loop `for i in range(1, k + 1):` 
# because it asked for sizes UP TO k. This one asks for EXACTLY size k!

# Problem 9: Write a single `for` loop: 
# `for c in combinations_with_replacement(sorted_S, k):`
#for c in combinations_with_replacement(sorted_S, k):

# Problem 10: Inside the loop, print `c`.
    #print(c)
# Problem 11: Notice that it prints the raw tuples exactly size `k`. 

# Problem 12: Delete or comment out this print loop, we will format it perfectly next.


# ==========================================
# SET 4: FORMATTING THE OUTPUT
# ==========================================
# Time to turn those tuples into clean strings.

# Problem 13: Rewrite your `for c in combinations_with_replacement(...)` loop.
for c in combinations_with_replacement(sorted_S, k):

# Problem 14: Inside the loop, use `"".join()` to stitch the tuple `c` into a string.
    print(''.join(c))
# Problem 15: Print the joined string.

# Problem 16: Check your output. It should perfectly match: 
# AA
# AC
# AH
# AK
# CC
# ...and so on.


# ==========================================
# SET 5: THE GRAND FINALE
# ==========================================
# Let's strip away the mock variables and assemble the final script.

# TERMINAL MOCK INPUT:
# HACK 2

# Problem 17: Ensure your `import` statement is at the top. (It is a long name to type!)

# Problem 18: Take user input using the 1-line unpacking trick: `S, k = input().split()`

# Problem 19: Convert `k` to an integer.

# Problem 20: Write your `for` loop combining the `combinations_with_replacement` function 
# and the `sorted(S)` trick, printing the `"".join()` of each tuple inside.
# (You should be able to solve this entire challenge in 5 lines of code!)
from itertools import combinations_with_replacement

S, k = input().split()
k = int(k)
for c in combinations_with_replacement(sorted(S), k):
    print(''.join(c))