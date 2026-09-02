# ==============================================================================
# FUNDAMENTALS CURRICULUM: STRING DECOMPOSITION & DATA FILTERING
# ==============================================================================
# Goal: Write a validation function `fun(s)` that analyzes an email string. 
# It must return True if the string perfectly matches the username, website, 
# and extension rules, and False if it fails ANY rule. The boilerplate will 
# use your function to filter out bad emails.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: STRUCTURAL DECOMPOSITION (THE SPLIT)
# ---------------------------------------------------------

# Problem 1: The '@' Symbol Requirement
# Concept: A valid email must have exactly one `@` symbol. If you split the 
# string by `@`, how many pieces should it break into?
# Mock Input: "lara@hackerrank.com"
# Mock Output: ["lara", "hackerrank.com"] (Length of 2)

# Problem 2: Invalid '@' Counts
# Concept: If someone enters "lara@@hackerrank.com" or just "lara.com", the 
# split length will not be 2. If the length is not 2, immediately return False.

# Problem 3: Unpacking the First Split
# Concept: If the length is exactly 2, you can safely unpack the list into two 
# variables: `username` and `domain_str`.

# Problem 4: The '.' Symbol Requirement
# Concept: The `domain_str` must contain exactly one `.` separating the website 
# from the extension. Split `domain_str` by `.`. It must also break into 
# exactly 2 pieces, otherwise return False.

# Problem 5: Unpacking the Domain
# Concept: Unpack that second split into two variables: `website` and `extension`.

# ---------------------------------------------------------
# CONCEPT BLOCK 2: VALIDATING THE USERNAME
# ---------------------------------------------------------

# Problem 6: The Empty Username Trap
# Concept: What if the email is "@hackerrank.com"? The `username` variable 
# will be an empty string `""`. If the length of `username` is 0, return False.

# Problem 7: Allowed Characters
# Concept: The username can contain letters, numbers, dashes (-), and 
# underscores (_). Python has a built-in string method to check if a string is 
# strictly letters/numbers, but the dashes and underscores will cause it to fail.

# Problem 8: The Replacement Trick
# Concept: Before checking the characters, create a temporary string where you 
# replace all dashes and underscores with empty strings `""`.
# Mock Input: "britts_54"
# Mock Output: "britts54"

# Problem 9: The Alphanumeric Check
# Concept: Now use the built-in string method on that temporary string to check 
# if it is perfectly alphanumeric. If it is not, return False.
# Mock Input: "britts54"
# Mock Output: True

# ---------------------------------------------------------
# CONCEPT BLOCK 3: VALIDATING THE WEBSITE
# ---------------------------------------------------------

# Problem 10: The Empty Website Trap
# Concept: What if the email is "lara@.com"? Check if the length of `website` 
# is 0. If it is, return False.

# Problem 11: Validating Website Characters
# Concept: The website can ONLY contain letters and digits. Use the built-in 
# alphanumeric string method directly on the `website` variable.
# Mock Input: "hackerrank!"
# Mock Output: False (Because of the exclamation mark).

# ---------------------------------------------------------
# CONCEPT BLOCK 4: VALIDATING THE EXTENSION
# ---------------------------------------------------------

# Problem 12: The Empty Extension Trap
# Concept: What if the email is "lara@hackerrank."? Check if the length of 
# `extension` is 0. If it is, return False.

# Problem 13: Validating Extension Characters
# Concept: The extension can ONLY contain letters. Python has a different 
# built-in string method specifically for checking if a string is purely 
# alphabetical. Use it! If it fails, return False.
# Mock Input: "co1"
# Mock Output: False

# Problem 14: Validating Extension Length
# Concept: The extension has a maximum length. Check if its length is greater 
# than 3. If it is, return False.
# Mock Input: "comm"
# Mock Output: False

# ---------------------------------------------------------
# CONCEPT BLOCK 5: THE TRY/EXCEPT SAFETY NET
# ---------------------------------------------------------

# Problem 15: The Unpacking Danger
# Concept: Manually checking the length of your splits (Problems 2 & 4) is 
# great, but you can also use a `try...except` block!

# Problem 16: Triggering ValueError
# Concept: If you try to unpack `user, domain = s.split('@')` and there are 3 
# pieces, Python will crash with a `ValueError`. 

# Problem 17: Returning False on Crash
# Concept: By wrapping your unpacking logic inside a `try` block, you can use 
# `except ValueError:` to elegantly catch these formatting errors and return 
# False without crashing your script!

# ---------------------------------------------------------
# CONCEPT BLOCK 6: FILTER MECHANICS (BOILERPLATE)
# ---------------------------------------------------------

# Problem 18: Passing the Gauntlet
# Concept: If your script successfully makes it through all the checks above 
# without returning False, it means the string is perfect. The very last line 
# of your function should return True.

# Problem 19: The filter() Function
# Concept: The boilerplate passes your `fun` and the `emails` list into `filter()`. 
# It passes each email in one by one. If `fun` returns True, the email is kept. 
# If `fun` returns False, the email is discarded.

# Problem 20: Lexicographical Sorting
# Concept: The boilerplate takes the surviving emails, casts them to a list, 
# and calls `.sort()`. Since they are strings, `.sort()` automatically puts 
# them in alphabetical order!

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- Input Parsing Stage ---
# Boilerplate reads Integer N = 3
# Boilerplate loops 3 times, appending strings to the `emails` array.
# emails = ["lara@hackerrank.com", "brian-23@hackerrank.com", "britts_54@hackerrank.com"]

# --- Filter Phase: Email 1 ---
# Boilerplate calls filter(fun, emails). Evaluates Index 0.
# function attempts split by '@' -> user="lara", domain="hackerrank.com"
# function attempts split by '.' -> website="hackerrank", ext="com"
# Validates user alphanumeric? Yes.
# Validates website alphanumeric? Yes.
# Validates extension alphabetical and <= 3? Yes.
# Function returns True. Email survives.

# --- Filter Phase: Email 2 ---
# Evaluates Index 1: "brian-23@hackerrank.com"
# Replaces '-' with empty string -> "brian23"
# Validates new string alphanumeric? Yes.
# Function returns True. Email survives.

# --- Mock Filter Phase: Bad Email ---
# Evaluates Mock Index: "invalid@email@com"
# function attempts split by '@' -> yields 3 items!
# Triggers ValueError / length check fails.
# Exception block catches error -> Returns False. Email is discarded.

# --- Output Stage ---
# Filter yields surviving strings. Boilerplate creates list.
# Boilerplate calls .sort() -> Alphabetizes the strings.
# Console Prints sorted array.