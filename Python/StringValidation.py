# ==========================================
# SET 1: THE BUILT-IN VALIDATORS
# ==========================================
# Let's see how these methods behave on perfect data.

# Problem 1: Print the result of `"abc".isalpha()`. (Checks if ALL characters are letters).
# Expected Output: True

# Problem 2: Print the result of `"123".isdigit()`. (Checks if ALL characters are numbers).
# Expected Output: True

# Problem 3: Print the result of `"abc123".isalnum()`. (Checks if ALL characters are letters OR numbers).
# Expected Output: True

# Problem 4: Print the result of `"hello".islower()`.
# Expected Output: True

# Problem 5: Print the result of `"HELLO".isupper()`.
# Expected Output: True


# ==========================================
# SET 2: THE HACKERRANK TRAP
# ==========================================
# HackerRank asks: "Does the string CONTAIN an alphabetical character?"
# Let's test the string "qA2".

# Problem 6: Print `"qA2".isalpha()`. 
# Expected Output: False 
# (THE TRAP! It returns False because the '2' is not a letter. It checks the ALL characters, not ANY character.)

# Problem 7: We need to check character by character. 
# Write a `for` loop that iterates over `s = "qA2"`. 
# Inside the loop, print `char.isalpha()`.
# Expected Output:
# True  (for 'q')
# True  (for 'A')
# False (for '2')

# Problem 8: We don't want to write a giant for-loop for every single check. Let's use a List Comprehension!
# Write a list comprehension that generates `[char.isalpha() for char in "qA2"]`. 
# Save it to `alpha_list` and print it.
# Expected Output: [True, True, False]

# Problem 9: Do the exact same thing, but check if the characters are digits. 
# Save to `digit_list` and print it.
# Expected Output: [False, False, True]

# Problem 10: Do the exact same thing, but check for uppercase. 
# Save to `upper_list` and print it.
# Expected Output: [False, True, False]


# ==========================================
# SET 3: THE "ANY()" SUPERPOWER
# ==========================================
# Python has a built-in function called `any()`. 
# If you feed it a list of Booleans, it will return True if AT LEAST ONE item in the list is True.

# Problem 11: Print `any([False, False, False])`.
# Expected Output: False

# Problem 12: Print `any([False, True, False])`.
# Expected Output: True

# Problem 13: Let's combine `any()` with our list comprehensions from Set 2!
# Print `any([char.isalpha() for char in "qA2"])`.
# Expected Output: True (Because 'q' and 'A' are letters!)

# Problem 14: Use `any()` and a list comprehension to check if "qA2" contains ANY digits. Print it.
# Expected Output: True

# Problem 15: Use `any()` and a list comprehension to check if "qA2" contains ANY lowercase letters. Print it.
# Expected Output: True


# ==========================================
# SET 4: THE GRAND FINALE
# ==========================================
# You now have the exact blueprint to solve the HackerRank challenge. 
# HackerRank gives you a string `s` and expects 5 print statements in a very specific order.

# Problem 16: For `s = "qA2"`, use `any()` and list comprehension to print if it contains ANY alphanumeric chars.

# Problem 17: Next line, print if it contains ANY alphabetical chars.

# Problem 18: Next line, print if it contains ANY digits.

# Problem 19: Next line, print if it contains ANY lowercase chars.

# Problem 20: Next line, print if it contains ANY uppercase chars.

# Expected Output for Problems 16-20:
# True
# True
# True
# True
# True