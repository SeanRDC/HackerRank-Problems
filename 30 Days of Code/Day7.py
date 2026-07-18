# ==========================================
# SET 1: THE LOOP METHOD (THE HARD WAY)
# ==========================================
# Let's iterate backward through the list manually.

# MOCK INPUT:
# arr = [1, 4, 3, 2]

# Problem 1: Create a list variable `arr` containing the integers 1, 4, 3, and 2.
arr = [1, 4, 3, 2]
start =(len(arr) - 1)

# Problem 2: Write a loop that counts backward from the last index of the list down to 0.
# (Hint: Use range() with a start, stop, and negative step).
for i in range(start, -1, -1):

# Problem 3: Inside the loop, print the list element at the current index. 
# To keep them on the same line, use the `end=" "` argument in your print statement.
# EXPECTED OUTPUT: 2 3 4 1 
    print(arr[i], end=" ")

# Problem 4: Outside the loop, write an empty `print()` statement just to move 
# the terminal to a new line for the next set.
print()


# ==========================================
# SET 2: THE IN-PLACE REVERSAL
# ==========================================
# Lists have built-in methods. Let's use the one designed to reverse things.

# Problem 5: Reset your `arr` variable to `[1, 4, 3, 2]`.
arr = [1, 4, 3, 2]

# Problem 6: Call the `.reverse()` method directly on `arr`. (Note: This modifies the list 
# in place, meaning it doesn't create a new list, it permanently changes the original one).
arr.reverse()

# Problem 7: Print `arr`. 
# EXPECTED OUTPUT: [2, 3, 4, 1]
print(arr)

# Problem 8: We need it space-separated, not in brackets. You know how to use `"-".join()`, 
# but `.join()` ONLY works on strings! Our list has integers.
# NEW SYNTAX: You can turn all items in a list into strings using `map(str, list_name)`.
# Write a print statement that uses `" ".join()` combined with `map(str, arr)`.
# EXPECTED OUTPUT: 2 3 4 1
print(' '.join(map(str, arr)))

# ==========================================
# SET 3: THE SLICING SUPERPOWER
# ==========================================
# Because lists and strings are both "iterables" in Python, the exact same 
# slicing trick you used for strings works on lists!

# Problem 9: Reset your `arr` variable to `[1, 4, 3, 2]`.
arr = [1, 4, 3, 2]

# Problem 10: Use the `[::-1]` slice on `arr` and save it to a variable called `sliced_arr`.
sliced_arr = arr[::-1]

# Problem 11: Print `sliced_arr`.
# EXPECTED OUTPUT: [2, 3, 4, 1]
print(sliced_arr)

# Problem 12: Print it as a space-separated string using the `.join()` and `map()` 
# trick you learned in Problem 8.
# EXPECTED OUTPUT: 2 3 4 1
print(' '.join(map(str, sliced_arr)))


# ==========================================
# SET 4: THE ASTERISK UNPACKING (THE SECRET WEAPON)
# ==========================================
# Python has an incredible shortcut for printing lists without brackets or commas.
# NEW SYNTAX: If you put an asterisk `*` in front of a list inside a print statement, 
# it "unpacks" the list and prints the elements separated by spaces automatically!
# Example: `print(*my_list)`

# Problem 13: Reset your `arr` variable to `[1, 4, 3, 2]`.

# Problem 14: Use the unpacking operator `*` inside a print statement on `arr`.
# EXPECTED OUTPUT: 1 4 3 2

# Problem 15: Let's combine our superpowers. Inside a single print statement, 
# use the unpacking operator `*` on a reversed slice of `arr` (i.e., `arr[::-1]`).
# EXPECTED OUTPUT: 2 3 4 1

# Problem 16: Take a moment to realize you just turned a standard algorithmic problem 
# into exactly ONE line of code.


# ==========================================
# SET 5: THE GRAND FINALE
# ==========================================
# Let's integrate our one-liner into HackerRank's provided starter code.

# TERMINAL MOCK INPUT (What you will type when you run the code):
# 4
# 1 4 3 2

# Problem 17: Write the `if __name__ == '__main__':` block just like HackerRank does.

# Problem 18: Inside the block, get the integer input for `n` (array size).

# Problem 19: Next, paste HackerRank's exact code for grabbing the array:
# `arr = list(map(int, input().rstrip().split()))`

# Problem 20: Use the ultimate one-liner from Problem 15 to print the reversed array!

# TERMINAL EXPECTED OUTPUT:
# 2 3 4 1