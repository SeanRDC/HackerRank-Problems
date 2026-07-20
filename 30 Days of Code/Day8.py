# ==========================================
# SET 1: DICTIONARY BASICS
# ==========================================
# Let's see how standard dictionaries store key-value pairs.

# Problem 1: Create an empty dictionary called `phone_book`. 
# (Hint: Use curly braces `{}`).

# Problem 2: Add a new entry to the dictionary where the key is "sam" 
# and the value is "99912222". 
# Syntax: dictionary[key] = value

# Problem 3: Add another entry for "tom" with the number "11122222".

# Problem 4: Print the phone number for "sam" by accessing `phone_book["sam"]`.
# EXPECTED OUTPUT: 99912222


# ==========================================
# SET 2: HANDLING MISSING KEYS Gracefully
# ==========================================
# If you try to access a key that doesn't exist (like `phone_book["edward"]`), 
# Python will crash with a KeyError. We must check if it exists first!

# Problem 5: Create a mock variable `query_1 = "sam"`.

# Problem 6: Write an `if` statement checking if `query_1` is `in` the `phone_book`.

# Problem 7: If it is in the phone book, print the perfectly formatted string:
# name=phonenumber (e.g., sam=99912222). 
# Hint: Use an f-string! `f"{query_1}={phone_book[query_1]}"`

# Problem 8: Write the `else` block. If it is NOT in the phone book, print "Not found".
# Change `query_1` to "edward" and run it again to test your else block!


# ==========================================
# SET 3: PARSING THE PHONE BOOK (KNOWN LOOP)
# ==========================================
# We know exactly how many entries to read because HackerRank gives us `n`.

# MOCK INPUT:
# 3
# sam 99912222
# tom 11122222
# harry 12299933

# Problem 9: Read the first line of input and convert it to an integer `n`.

# Problem 10: Write a `for` loop that runs `n` times using `range(n)`.

# Problem 11: Inside the loop, read the line, split it, and unpack it into two 
# variables: `name` and `phone`.

# Problem 12: Add the `name` and `phone` to your `phone_book` dictionary.


# ==========================================
# SET 4: HANDLING UNKNOWN QUERIES (THE EOF TRAP)
# ==========================================
# HackerRank doesn't tell us how many queries are left. If we call `input()` 
# and there is no more text, Python throws an `EOFError` and crashes.

# Problem 13: Set up an infinite loop using `while True:`

# Problem 14: Inside the loop, start a `try:` block.

# Problem 15: Inside the `try` block, attempt to read a query using `query = input()`.
# Paste your `if/else` logic from Set 2 right below this to print the result!

# Problem 16: Write the `except EOFError:` block. If we run out of input, 
# simply `break` out of the infinite `while` loop.


# ==========================================
# SET 5: THE GRAND FINALE
# ==========================================
# Let's assemble the final script!

# Problem 17: Initialize your empty `phone_book` dictionary.

# Problem 18: Read `n` and write your `for` loop to populate the dictionary.

# Problem 19: Write your `while True:` infinite loop.

# Problem 20: Inside the infinite loop, put your `try/except` block to read queries, 
# look them up in the dictionary, print the exact required formatting, and `break` 
# when the input runs out.