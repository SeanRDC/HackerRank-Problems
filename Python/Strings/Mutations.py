# ==========================================
# SET 1: THE LIST MUTATION METHOD
# ==========================================
# Strings are immutable, but lists are not!

# Problem 1: Convert the string `word = "Python"` into a list of characters. 
# Save it to `word_list` and print it.
# Expected Output: ['P', 'y', 't', 'h', 'o', 'n']
word = "Python"
word_list = []
for i in word:
    word_list += i
    
print(word_list)
# shortcut for string to list word_list = list(word)
# Problem 2: Change the character at index 3 of `word_list` to "x". Print the list.
# Expected Output: ['P', 'y', 't', 'x', 'o', 'n']
word_list[3] = 'x'
print(word_list)

# Problem 3: Smash `word_list` back into a string using `"".join()` and print it.
# Expected Output: Pytxon
print(''.join(word_list))


# ==========================================
# SET 2: THE SLICING METHOD (The Pythonic Way)
# ==========================================
# Slicing grabs specific chunks of a string: `string[start:stop]` (stop is exclusive!)
# If you leave `start` blank ([:5]), it starts from the very beginning. 
# If you leave `stop` blank ([6:]), it goes to the very end.

# Problem 4: Grab everything BEFORE index 5 in `word = "abracadabra"`. 
# Save it to `first_half` using `word[:5]`. Print it.
# Expected Output: abrac
word = "abracadabra"
first_half = word[:5] # exclusive
print(first_half)

# Problem 5: Grab everything AFTER index 5 in `word = "abracadabra"`. 
# Save it to `second_half` using `word[6:]` (Notice we use 6 to skip index 5!). Print it.
# Expected Output: dabra
second_half = word[6:] # inclusive
print(second_half)

# Problem 6: Combine them! Add `first_half`, the string `"k"`, and `second_half` together. 
# Print the final result.
# Expected Output: abrackdabra
print(f'{first_half}k{second_half}')


# ==========================================
# SET 3: THE GRAND FINALE
# ==========================================

# Problem 7: Complete the HackerRank function!
# You can use either the List method or the Slicing method.
# Task: Read a given string, change the character at a given index and then print the modified string.
def mutate_string(string, position, character):
    word_list = list(string)
    word_list[position] = character
    return ''.join(word_list)

# Test it with the HackerRank sample data:
print(mutate_string("abracadabra", 5, "k"))