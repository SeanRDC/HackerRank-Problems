# ==========================================
# THE PROBLEM: Calculate the total revenue per item in a supermarket 
# while maintaining the exact chronological order the items were first scanned.
# THE GOAL: Build a string-parsing engine to separate names from prices, 
# then feed them into an OrderedDict to accumulate the totals.
# ==========================================

# ---------------------------------------------------------
# PHASE 1: THE SETUP
# ---------------------------------------------------------

# Problem 1: The Import
# We need to bring in our special tool. 
# Write the code to import `OrderedDict` from the `collections` module.
from collections import OrderedDict


# Problem 2: The Cash Register
# Create a variable named `manager_ledger`.
# Instantiate a new, empty `OrderedDict` and assign it to this variable.
manager_ledger = OrderedDict()

# ---------------------------------------------------------
# PHASE 2: THE STRING PARSING ENGINE (Mock Testing)
# ---------------------------------------------------------

# Problem 3: The Mock Input
# Create a variable `mock_line` and set it to the string: "POTATO CHIPS 30"
# Create a variable `words` and split `mock_line` into a list of individual strings.
mock_line = "POTATO CHIPS 30"
words = mock_line.split()

# Problem 4: Extracting the Price
# The price is ALWAYS the very last item in the list, no matter how long the item name is. 
# How do you target the last element of a list in Python?
# Grab it, convert it to an integer, and save it to a variable named `price`.
price = int(words[-1])

# Problem 5: Extracting the Name Pieces
# How do you grab a "slice" of a list that contains everything EXCEPT the last item?
# Grab that slice and save it to a variable named `name_pieces`.
name_pieces = words[:-1]

# Problem 6: Rebuilding the Name
# Right now, `name_pieces` is a list of strings: ['POTATO', 'CHIPS']. We want a clean string.
# What string method allows you to glue a list of strings together with a space in between them?
# Perform this action, save the result to `item_name`, and print it to test!
# Expected Output: POTATO CHIPS
item_name = ' '.join(name_pieces)

# ---------------------------------------------------------
# PHASE 3: THE COUNTING LOGIC (Mock Testing)
# ---------------------------------------------------------

# Problem 7: The First Scan
# Write an `if` statement to check if your `item_name` does NOT exist in your `manager_ledger`.
if item_name not in manager_ledger:

    # Problem 8: The Initial Price
    # Inside the if-block, add `item_name` to the `manager_ledger` as a new key, 
    # and set its value to your `price` variable.
    manager_ledger[item_name] = price

# Problem 9: The Repeat Scan
# Write an `else:` block for when the item already exists in the ledger.
else:

    # Problem 10: Accumulating the Total
    # Inside the else-block, look up the existing `item_name` in the ledger 
    # and mathematically add the new `price` to its current total.
    manager_ledger[item_name] += price

# ---------------------------------------------------------
# PHASE 4: THE MASTER LOOP (Real Execution)
# ---------------------------------------------------------

# Problem 11: Total Transactions
# Read the very first line of standard input, convert it to an integer, and save it to `N`.
N = int(input())

# Problem 12: The Execution Loop
# Write a `for` loop that runs exactly `N` times.
for i in range(N):

    # Problem 13: Read the Line
    # Inside the loop, read the next line of standard input and save it to a variable `line`.
    line = input()
    
    # Problem 14: Split the Line
    # Split the `line` into a list of words.
    words = line.split()
    
    # Problem 15: Grab the Price
    # Repeat the logic from Problem 4 here inside the loop. Grab the price and convert to int.
    price = int(words[-1])
    
    # Problem 16: Grab the Name
    # Repeat the logic from Problems 5 & 6 here to slice and join the item name.
    item_name = words[:-1]
    item = ' '.join(item_name)
    
    # Problem 17: Update the Ledger
    # Repeat the logic from Problems 7, 8, 9, and 10 here. 
    # If the item is new, set it. If it exists, add the price to the total!
    if item not in manager_ledger:
        manager_ledger[item] = price
    else:
        manager_ledger[item] += price        

# ---------------------------------------------------------
# PHASE 5: PRINTING THE RECEIPT
# ---------------------------------------------------------

# Problem 18: Unpacking the Ledger
# Step completely outside the `N` loop.
# Write a new `for` loop that unpacks BOTH the keys and values from your dictionary at the same time.


    # Problem 19: The Final Output
    # Inside this new loop, print the key (the item) and the value (the total) separated by a space.


# =====================================================================
# FINAL SUBMISSION
# SUMMARY: Assemble your import, your empty OrderedDict, your `N` reading, 
# your master loop (which parses strings and updates the ledger), and 
# your final receipt-printing loop into one clean script.
# 
# MOCK INPUT (STDIN): 
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30
# 
# EXPECTED OUTPUT: 
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20
# =====================================================================

# Paste your assembled final script here!