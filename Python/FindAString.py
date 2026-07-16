# ==========================================
# SET 1: THE BUILT-IN TRAP
# ==========================================

# Problem 1: Python has a built-in `.count()` method. Let's see why it fails here.
# Print the result of `"ABCDCDC".count("CDC")`.
# Expected Output: 1
# (Wait, why 1? The built-in method doesn't count OVERLAPPING strings! 
# It finds the first "CDC", skips past it, and only checks the last "C". We need to find 2!)
print("ABCDCDC".count("CDC"))


# ==========================================
# SET 2: THE SLIDING WINDOW
# ==========================================
# To catch overlapping strings, we have to look at every single letter, 
# look ahead by the length of the substring, and check for a match.

word = "ABCDCDC"
sub = "CDC"

# Problem 2: First, we need to know how big our window is.
# Create a variable `window = len(sub)`. Print `window`.
# Expected Output: 3
window = len(sub)
print(window)

# Problem 3: Now let's loop through the main word using its length.
# Write a for loop: `for i in range(len(word)):`
# Inside the loop, print the slice of the word starting at `i` and ending at `i + window`.
# Example: print(word[i:i + window])
# Expected Output:
# ABC
# BCD
# CDC
# DCD
# CDC
# DC
# C
for i in range(len(word)):
    print(word[i:i + window])


# ==========================================
# SET 3: THE GRAND FINALE
# ==========================================

# Problem 4: Combine the pieces into the HackerRank function!
# 1. Create a `count = 0` variable.
# 2. Find the `window` size using `len(sub_string)`.
# 3. Create your `for` loop.
# 4. Inside the loop, slice the string using your window. 
# 5. If that slice `== sub_string`, increment your count by 1!
# 6. Return the count at the very end.

def count_substring(string, sub_string):
    count = 0
    window = len(sub_string)
    
    for i in range(len(string)):
        sliced = string[i:i + window]
        if sliced == sub_string:
            count += 1
    return count
    
print(count_substring("ABCDCDC", "CDC"))
# Expected Output: 2