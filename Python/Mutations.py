# ==========================================
# SET 1: THE LIST MUTATION METHOD
# ==========================================
# Strings are immutable, but lists are not!

# Problem 1: Convert the string `word = "Python"` into a list of characters. 
# Save it to `word_list` and print it.
# Expected Output: ['P', 'y', 't', 'h', 'o', 'n']

# Problem 2: Change the character at index 3 of `word_list` to "x". Print the list.
# Expected Output: ['P', 'y', 't', 'x', 'o', 'n']

# Problem 3: Smash `word_list` back into a string using `"".join()` and print it.
# Expected Output: Pytxon


# ==========================================
# SET 2: THE SLICING METHOD (The Pythonic Way)
# ==========================================
# Slicing grabs specific chunks of a string: `string[start:stop]` (stop is exclusive!)
# If you leave `start` blank ([:5]), it starts from the very beginning. 
# If you leave `stop` blank ([6:]), it goes to the very end.

# Problem 4: Grab everything BEFORE index 5 in `word = "abracadabra"`. 
# Save it to `first_half` using `word[:5]`. Print it.
# Expected Output: abrac

# Problem 5: Grab everything AFTER index 5 in `word = "abracadabra"`. 
# Save it to `second_half` using `word[6:]` (Notice we use 6 to skip index 5!). Print it.
# Expected Output: dabra

# Problem 6: Combine them! Add `first_half`, the string `"k"`, and `second_half` together. 
# Print the final result.
# Expected Output: abrackdabra


# ==========================================
# SET 3: THE GRAND FINALE
# ==========================================

# Problem 7: Complete the HackerRank function!
# You can use either the List method or the Slicing method. 
# def mutate_string(string, position, character):
#     # Your code here!
#     return ...

# Test it with the HackerRank sample data:
# print(mutate_string("abracadabra", 5, "k"))