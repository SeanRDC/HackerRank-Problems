# ==========================================
# SET 1: MEET THE COUNTER
# ==========================================
# Let's see how Counter magically tallies up a list for us.

# MOCK INPUT:
# shoes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]

# Problem 1: Import the `Counter` class from the `collections` module.

# Problem 2: Create the mock variable `shoes` as a list of integers.

# Problem 3: Pass `shoes` into the `Counter()` function and save it to a variable 
# called `inventory`.

# Problem 4: Print `inventory`.
# EXPECTED OUTPUT: Counter({6: 2, 5: 2, 2: 1, 3: 1, 4: 1, ...})
# Notice how it automatically counted that there are two size 6s and two size 5s!


# ==========================================
# SET 2: SELLING A SHOE (MANAGING INVENTORY)
# ==========================================
# How do we check if we have a shoe, sell it, and update the count?

# Problem 5: Create a variable `total_money` and set it to 0.

# Problem 6: We have a customer who wants size 6 for $55. 
# Write an `if` statement to check if `inventory[6]` is greater than 0.

# Problem 7: Inside the `if` block, add 55 to `total_money`.

# Problem 8: Still inside the `if` block, subtract 1 from `inventory[6]`.
# Print `total_money` and `inventory[6]` to verify the transaction worked!


# ==========================================
# SET 3: THE "OUT OF STOCK" SCENARIO
# ==========================================
# What happens when customers try to buy shoes we don't have?
# Mock Customer Queue: (Size 6, $45) and then (Size 6, $55)

# Problem 9: The next customer wants size 6 for $45. 
# Copy your `if` logic from Set 2, but use $45. (Since we had two size 6s initially, 
# and sold one in Set 2, this one should successfully sell!).

# Problem 10: The third customer wants size 6 for $55. 
# Copy the `if` logic again. 

# Problem 11: Print `total_money` and `inventory[6]`. 
# EXPECTED OUTPUT: 100 for total money, 0 for inventory.
# Notice how the third customer was automatically ignored because inventory[6] was 0!


# ==========================================
# SET 4: PARSING THE FIRST THREE LINES OF INPUT
# ==========================================
# HackerRank gives us line after line of input. We need to parse it cleanly.

# MOCK TERMINAL INPUT:
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6

# Problem 12: HackerRank's first line is the number of shoes. We don't actually 
# need this for our Python logic, but we must read it to advance to the next line.
# Write: `num_shoes = int(input())`

# Problem 13: The next line is the shoe sizes. Read the input, split it, map it 
# to integers, turn it into a list, and wrap it directly in `Counter()`. 
# Save this to `inventory`.

# Problem 14: The third line is the number of customers. 
# Write: `num_customers = int(input())`


# ==========================================
# SET 5: THE GRAND FINALE
# ==========================================
# Let's combine the parsing and the selling logic into the final script.

# Problem 15: Keep your code from Set 4 (parsing the first 3 lines) and 
# set `total_money = 0`.

# Problem 16: Write a `for` loop that runs `num_customers` times using `range()`.

# Problem 17: Inside the loop, read the customer's request using the one-line 
# unpacking trick: `size, price = map(int, input().split())`

# Problem 18: Still inside the loop, write an `if` statement checking if 
# `inventory[size] > 0`.

# Problem 19: If true, add the `price` to `total_money` and decrement `inventory[size]` by 1.

# Problem 20: Outside the loop, print `total_money`.