# ==========================================
# SET 1: THE MANUAL PRODUCT (THE HARD WAY)
# ==========================================
# Let's see what a Cartesian product actually looks like under the hood.

# MOCK INPUT:
# A = [1, 2]
# B = [3, 4]

# Problem 1: Create the mock list variables A and B.
A = [1, 2]
B = [3, 4]

# Problem 2: Create an empty list called `manual_product`.
manual_product = []

# Problem 3: Write an outer loop that iterates through each item `a` in list A.
for a in A:

# Problem 4: Inside that loop, write an inner loop that iterates through each item `b` in list B.
    for b in B:

# Problem 5: Inside the inner loop, append a tuple containing `(a, b)` to your `manual_product` list.
        manual_product.append((a, b))
# Outside both loops, print `manual_product`.
print(manual_product)
# EXPECTED OUTPUT: [(1, 3), (1, 4), (2, 3), (2, 4)]


# ==========================================
# SET 2: THE ITERTOOLS MODULE (THE EASY WAY)
# ==========================================
# Python has a module that replaces that entire nested loop setup.
# NEW SYNTAX: `from itertools import product`

# Problem 6: Import the `product` function from the `itertools` module.
from itertools import product

# Problem 7: Call `product(A, B)` and save it to a variable called `result`. 
# Print `result`. (Notice it just prints an "itertools object" in memory!)
result = product(A, B)

# Problem 8: The `product` function generates items lazily to save memory. 
# Wrap your `product(A, B)` call inside `list()` to force it to generate all the pairs, 
# then print it.
# EXPECTED OUTPUT: [(1, 3), (1, 4), (2, 3), (2, 4)]
print(list(product(A, B)))


# ==========================================
# SET 3: PARSING THE HACKERRANK INPUT
# ==========================================
# HackerRank gives us strings like "1 2" instead of actual lists. We need to parse them.

# MOCK STRING INPUT:
input_A = "1 2"
input_B = "3 4"

# Problem 9: Create the mock string variables `input_A` and `input_B`.

# Problem 10: Using the `split()`, `map()`, and `list()` combo you learned in the 
# reverse array challenge, convert `input_A` into a list of integers. Save it to `list_A`.
list_A = list(map(int, input_A.split()))


# Problem 11: Do the exact same thing to convert `input_B` into `list_B`.
list_B = list(map(int, input_B.split()))

# Problem 12: Print `list_A` and `list_B` to verify they are actual integer lists.
print(list_A)
print(list_B)

# ==========================================
# SET 4: FORMATTING THE OUTPUT
# ==========================================
# We have the data, but HackerRank is extremely picky about the output format.
# It wants: (1, 3) (1, 4) (2, 3) (2, 4)
# It DOES NOT want: [(1, 3), (1, 4), (2, 3), (2, 4)]

# Problem 13: Generate the cartesian product of `list_A` and `list_B` using `list(product())`. 
# Save it to `final_product`.
final_product = list(product(list_A, list_B))

# Problem 14: How do we strip the square brackets off a list and print the elements 
# separated by spaces? Hint: Use the "Secret Weapon" you learned in the Reverse Array challenge!
print(*final_product)

# Problem 15: Use the unpacking operator `*` inside a print statement on `final_product`.
# EXPECTED OUTPUT: (1, 3) (1, 4) (2, 3) (2, 4)


# ==========================================
# SET 5: THE GRAND FINALE
# ==========================================
# Let's strip away all the mock variables and write the final submission.

# TERMINAL MOCK INPUT:
# 1 2
# 3 4

# Problem 16: Make sure your `import` statement is at the very top.

# Problem 17: Get the first line of user input, map it to integers, and save it as list A.

# Problem 18: Get the second line of user input, map it to integers, and save it as list B.

# Problem 19: Compute the product of A and B, convert it to a list, and save it to a variable.

# Problem 20: Print the unpacked list to perfectly match HackerRank's required format.