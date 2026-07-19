# ==========================================
# SET 1: UNDERSTANDING GROUPBY
# ==========================================
# Let's see how groupby separates the keys from their groups.

# MOCK INPUT:
# S = '1222311'

# Problem 1: Import `groupby` from the `itertools` module.
from itertools import groupby

# Problem 2: Create the mock variable `S`.
S = '1222311'
# Problem 3: Write a loop that unpacks the groupby object: 
# `for key, group in groupby(S):`
for i, group in groupby(S):

# Problem 4: Inside the loop, print `key` and `list(group)`.
# EXPECTED OUTPUT:
# 1 ['1']
# 2 ['2', '2', '2']
# 3 ['3']
# 1 ['1', '1']
# (Notice how it groups consecutive matches, but treats the second '1's as a new group!)
    print(i, list(group))

# ==========================================
# SET 2: EXTRACTING THE LENGTH AND VALUE
# ==========================================
# We don't want the raw list of strings; we just want the length of that list!

# Problem 5: Write the `for key, group in groupby(S):` loop again.
for i, group in groupby(S):
# Problem 6: Inside the loop, create a variable `count` and assign it `len(list(group))`.
    count = len(list(group))

# Problem 7: HackerRank expects the character to be printed as a number. 
# Create a variable `number` and assign it `int(key)`.
    number = int(i)
# Problem 8: Print the tuple `(count, number)`.
# EXPECTED OUTPUT: 
# (1, 1)
# (3, 2)
# (1, 3)
# (2, 1)
    print((count, number))
    


# ==========================================
# SET 3: STORING THE RESULTS
# ==========================================
# We need to save all these tuples so we can format them perfectly on one line.

# Problem 9: Before your loop, create an empty list called `compressed`.
    compressed = []
# Problem 10: Write your `groupby` loop one more time. 
    for i, group in groupby(S):
# Problem 11: Inside the loop, append your `(count, number)` tuple to the `compressed` list. 
# (Make sure to calculate count and number exactly as you did in Set 2).
        count = len(list(group))
        number = int(i)
        compressed.append((count, number))
# Problem 12: Outside the loop, print `compressed`.
# EXPECTED OUTPUT: [(1, 1), (3, 2), (1, 3), (2, 1)]
print(compressed)


# ==========================================
# SET 4: THE UNPACKING TRICK
# ==========================================
# We have a list of tuples, but HackerRank wants space-separated tuples.

# Problem 13: Look at your printed list from Problem 12. It has square brackets and commas.

# Problem 14: Recall the "asterisk unpacking" trick you learned in the arrays challenge.

# Problem 15: Use `*compressed` inside a print statement.

# Problem 16: Check your output. It should perfectly match HackerRank's requirement:
# (1, 1) (3, 2) (1, 3) (2, 1)
print(*compressed)


# ==========================================
# SET 5: THE GRAND FINALE
# ==========================================
# Let's write the final, HackerRank-ready script!

# TERMINAL MOCK INPUT:
# 1222311

# Problem 17: Ensure your `import` statement is at the very top.
from itertools import groupby

# Problem 18: Take user input using `S = input()`. 
# (Do NOT use `.split()` because the input is just one continuous string with no spaces!)
S = input()

# Problem 19: Create your empty list, run your `groupby` loop, and append the tuples.
compressed = []
for i, group in groupby(S):
    count = len(list(group))
    number = int(i)
    compressed.append((count, number))

# Problem 20: Print the unpacked list of tuples.
print(*compressed)