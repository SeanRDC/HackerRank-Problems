# ==========================================
# SET 1: GRABBING & CONVERTING TO BINARY
# ==========================================
# Problem 1: First, we need to grab the base-10 integer from HackerRank.
# -> MOCK INPUT (from HackerRank): 13
# Problem 2: In your editor, write: n = int(input().strip())
# -> INTERNAL OUTPUT: The variable `n` now holds the integer 13.
# Problem 3: In other languages, converting to binary requires heavy math loops.
# Problem 4: In Python, simply pass the number into the built-in bin() function!
# -> MOCK ACTION: bin(n)


# ==========================================
# SET 2: STRING SLICING (REMOVING THE PREFIX)
# ==========================================
# Problem 5: There is a slight catch with Python's bin() function.
# -> INTERNAL OUTPUT of bin(13): '0b1101'
# Problem 6: Python adds '0b' to the front to identify it as a binary string. 
# Problem 7: We don't want the '0b'. We only want the raw numbers: '1101'.
# Problem 8: Use Python string slicing to chop off the first two characters. 
# Write: binary_str = bin(n)[2:]
# -> INTERNAL OUTPUT: `binary_str` now holds the string '1101'


# ==========================================
# SET 3: THE PYTHONIC CHEAT CODE (SPLITTING)
# ==========================================
# Problem 9: Now we have '1101' and need to find the longest streak of consecutive '1's.
# Problem 10: Instead of a big 'for' loop, we will use the string .split() method!
# Problem 11: When you split a string by a character, Python destroys that character 
# and chops the string into a list of the leftover chunks.
# -> MOCK INPUT to split: '1101'
# Problem 12: If we split by '0', the '0' is destroyed, leaving the chunks '11' and '1'.
# Problem 13: Write: ones_groups = binary_str.split('0')
# -> INTERNAL OUTPUT: `ones_groups` is now a list containing ['11', '1']


# ==========================================
# SET 4: FINDING THE MAXIMUM
# ==========================================
# Problem 14: You now have a list containing every single streak of 1s!
# -> MOCK SCENARIO: If the binary was '10011101', your list would be ['1', '', '111', '1'].
# Problem 15: Python has a built-in max() function that finds the largest item in a list.
# Problem 16: When max() looks at strings, it finds the "longest" one alphabetically/numerically.
# Problem 17: Pass your list into max() so it can find the longest streak.
# Problem 18: Write: longest_streak = max(ones_groups)
# -> INTERNAL OUTPUT: `longest_streak` now holds the string '11'


# ==========================================
# SET 5: THE GRAND FINALE
# ==========================================
# Problem 19: HackerRank doesn't want the string '11'; it wants the integer length (2).
# -> MOCK INPUT to len(): '11'
# Problem 20: Pass your longest_streak into the len() function, and print the result!
# -> FINAL OUTPUT: 2

n = int(input().strip())
binary_str = bin(n)[2:]
print(len(max(binary_str.split('0'))))
