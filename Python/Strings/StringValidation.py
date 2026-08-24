# ==========================================
# SET 1: THE BUILT-IN VALIDATORS
# ==========================================
# Let's see how these methods behave on perfect data.

# Problem 1: Print the result of `"abc".isalpha()`. (Checks if ALL characters are letters).
# Expected Output: True
print('abc'.isalpha())

# Problem 2: Print the result of `"123".isdigit()`. (Checks if ALL characters are numbers).
# Expected Output: True
print('123'.isdigit())

# Problem 3: Print the result of `"abc123".isalnum()`. (Checks if ALL characters are letters OR numbers).
# Expected Output: True
print('abc123'.isalnum())

# Problem 4: Print the result of `"hello".islower()`.
# Expected Output: True
print('hello'.islower())

# Problem 5: Print the result of `"HELLO".isupper()`.
# Expected Output: True
print('HELLO'.isupper())


# ==========================================
# SET 2: THE HACKERRANK TRAP
# ==========================================
# HackerRank asks: "Does the string CONTAIN an alphabetical character?"
# Let's test the string "qA2".

# Problem 6: Print `"qA2".isalpha()`. 
# Expected Output: False 
# (THE TRAP! It returns False because the '2' is not a letter. It checks the ALL characters, not ANY character.)
print('qA2'.isalpha())

# Problem 7: We need to check character by character. 
# Write a `for` loop that iterates over `s = "qA2"`. 
# Inside the loop, print `char.isalpha()`.
# Expected Output:
# True  (for 'q')
# True  (for 'A')
# False (for '2')
s = "qA2"
for i in s:
    print(i.isalpha())
    

# Problem 8: We don't want to write a giant for-loop for every single check. Let's use a List Comprehension!
# Write a list comprehension that generates `[char.isalpha() for char in "qA2"]`. 
# Save it to `alpha_list` and print it.
# Expected Output: [True, True, False]
alpha_list = [i.isalpha() for i in s]
print(alpha_list)

# Problem 9: Do the exact same thing, but check if the characters are digits. 
# Save to `digit_list` and print it.
# Expected Output: [False, False, True]
digit_list = [i.isdigit() for i in s]
print(digit_list)

# Problem 10: Do the exact same thing, but check for uppercase. 
# Save to `upper_list` and print it.
# Expected Output: [False, True, False]
upper_list = [i.isupper() for i in s]
print(upper_list)


# ==========================================
# SET 3: THE "ANY()" SUPERPOWER
# ==========================================
# Python has a built-in function called `any()`. 
# If you feed it a list of Booleans, it will return True if AT LEAST ONE item in the list is True.

# Problem 11: Print `any([False, False, False])`.
# Expected Output: False
print(any([False, False, False]))

# Problem 12: Print `any([False, True, False])`.
# Expected Output: True
print(any([False, True, False]))

# Problem 13: Let's combine `any()` with our list comprehensions from Set 2!
# Print `any([char.isalpha() for char in "qA2"])`.
# Expected Output: True (Because 'q' and 'A' are letters!)
print(any([i.isalpha() for i in s]))

# Problem 14: Use `any()` and a list comprehension to check if "qA2" contains ANY digits. Print it.
# Expected Output: True
print(any([i.isdigit() for i in s]))

# Problem 15: Use `any()` and a list comprehension to check if "qA2" contains ANY lowercase letters. Print it.
# Expected Output: True
print(any([i.islower() for i in s]))


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
s = "qA2"
print(any([char.isalnum() for char in s]))
print(any([char.isalpha() for char in s]))
print(any([char.isdigit() for char in s]))
print(any([char.islower() for char in s]))
print(any([char.isupper() for char in s]))

# Expected Output for Problems 16-20:
# True
# True
# True
# True
# True