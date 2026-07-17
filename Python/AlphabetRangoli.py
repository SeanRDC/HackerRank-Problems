# ==========================================
# SET 1: THE ALPHABET TOOLKIT
# ==========================================
# Python has the alphabet built in, so we don't have to type it manually.

# Problem 1: Import the string module (`import string`). 
# Print `string.ascii_lowercase`.
# Expected Output: abcdefghijklmnopqrstuvwxyz
import string

print(string.ascii_lowercase)

# Problem 2: Set `N = 5`. Slice the first N letters of the alphabet. 
# Save it to a variable called `letters` and print it.
# Expected Output: abcde
N = 5
letters = (string.ascii_lowercase[:5])
print(letters)

# Problem 3: Practice your slicing. Print `letters` completely reversed using `[::-1]`.
# Expected Output: edcba
print(letters[::-1])

# ==========================================
# SET 2: BUILDING THE DIAMOND CORE
# ==========================================
# Let's manually build a single row. The logic relies on taking a slice of letters, 
# reversing it for the left side, and keeping it normal for the right side.

# Problem 4: Set a test variable `i = 2`. 
# Slice `letters` from index `i` to the end (`letters[i:]`), and then reverse it using `[::-1]`.
# Save it to `left_side` and print it. 
# Expected Output: edc

# Problem 5: Slice `letters` from index `i + 1` to the end (`letters[i+1:]`). 
# Save it to `right_side` and print it.
# Expected Output: de

# Problem 6: Add `left_side` and `right_side` together! Save it to `combined` and print it.
# Expected Output: edcde

# Problem 7: Use `"-".join(combined)` to put dashes between every letter. Print it.
# Expected Output: e-d-c-d-e


# ==========================================
# SET 3: THE DYNAMIC WIDTH
# ==========================================
# Just like the binary challenge, we need to find the width of the very longest row (the middle) 
# so we can perfectly center all the shorter rows.

# Problem 8: The middle row happens when `i = 0`. 
# Using the exact logic from Problems 4, 5, and 6, generate the `combined` string for `i = 0`.
# Expected Output: edcbabcde

# Problem 9: Use `"-".join()` on your string from Problem 8. Save it to `master_row` and print it.
# Expected Output: e-d-c-b-a-b-c-d-e

# Problem 10: Find the `len()` of `master_row`. Save it to `width` and print it.
# Expected Output: 17

# Problem 11: Take your short string from Problem 7 ("e-d-c-d-e") and use `.center()` 
# on it using your `width` variable and "-" as the fill character. Print it!
# Expected Output: ------e-d-c-d-e------


# ==========================================
# SET 4: THE LIST MIRROR (New Concept!)
# ==========================================
# Instead of printing right away, we are going to store our rows in a list.

# Problem 12: Create an empty list called `rows = []`.

# Problem 13: Write a `for` loop: `for i in range(N - 1, -1, -1):`
# (This counts backward from 4 down to 0). Print `i` inside to verify it works.

# Problem 14: Inside the loop, generate `left_side = letters[i:][::-1]`.

# Problem 15: Inside the loop, generate `right_side = letters[i+1:]`.

# Problem 16: Inside the loop, join them: `row_string = "-".join(left_side + right_side)`.

# Problem 17: Inside the loop, center it: `centered_row = row_string.center(width, "-")`. 
# Finally, `.append()` `centered_row` to your `rows` list.

# Problem 18: Outside the loop, print your `rows` list. 
# You should see the entire top half and the middle row of the Rangoli!


# ==========================================
# SET 5: THE GRAND FINALE
# ==========================================

# Problem 19: We need the bottom half. The bottom half is exactly the same as the top half, 
# just flipped upside down (and missing the middle row so it doesn't duplicate).
# Create `bottom_half = rows[:-1][::-1]`. 
# (This slices away the last item, which is the middle row, and reverses the rest of the list!)

# Problem 20: Combine the lists: `final_rangoli = rows + bottom_half`.
# Finally, use `"\n".join(final_rangoli)` to print the entire diamond beautifully!

# Try plugging it into the HackerRank function!
def print_rangoli(size):
    # Your beautiful, dynamic code goes here!
    pass