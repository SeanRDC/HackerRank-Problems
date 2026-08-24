# ==========================================
# SET 1: THE SETUP & STRING ITERATION
# ==========================================

# MINI-LESSON: STRINGS AND INDICES
# Strings in Python are just arrays of characters. BANANA has a length of 6, with indices 0 through 5.
# To solve this problem without timing out, we need to look at each character one by one and track its index.

# Problem 1: Define the function `def minion_game(string):`. 
# Put `pass` inside it for now.
def minion_game(string):

# Problem 2: Inside the function, delete `pass`. 
# We need to know what a vowel is. Create a string variable called `vowels` and set it equal to "AEIOU".
    vowels = 'AEIOU'

# Problem 3: We need to keep track of the scores. 
# Create two variables, `kevin_score` and `stuart_score`, and initialize both of them to 0.
    kevin_score = 0
    stuart_score = 0

# Problem 4: We will need the total length of the string for our math trick later. 
# Create a variable called `length` and set it equal to `len(string)`.
    length = len(string)

# Problem 5 (MINI-BOSS: THE LOOP):
# We need to iterate through the string, but we need the INDEX of each letter. 
# Write a `for` loop using `range(length)`. Use `i` as your loop variable (e.g., `for i in ...`).
# Inside the loop, create a variable `char` and grab the current letter using `string[i]`.
# Put `pass` on the next line. Send this Set 1 code over for review!
    for i in range(length):
        char = string[i]
        


# ==========================================
# SET 2: THE MATH TRICK (Avoiding Timeouts)
# ==========================================

# MINI-LESSON: THE MATHEMATICAL SHORTCUT
# Look at the file "image_d77b15.png". 
# The string is BANANA (length = 6). The letter 'B' is at index 0. 
# Look under Stuart's column. How many substrings start with that exact 'B'?
# B, BA, BAN, BANA, BANAN, BANANA. Exactly 6 words!
# The formula for how many substrings can be made starting at ANY index is simply: (length - index)
# If 'A' is at index 1: (6 - 1) = 5 words. We don't need to build the words; we just need to add the math!

# Problem 6: Inside your `for` loop, replace `pass` with an `if` statement.
# Check if the current `char` exists inside your `vowels` string. (Hint: Use the `in` keyword).
        if char in vowels:

# Problem 7: If the character IS a vowel, Kevin gets the points! 
# Inside the `if` block, calculate how many substrings can be made using the math trick `(length - i)`.
# Add this number to `kevin_score`.
            kevin_score = length - i

# Problem 8: Below that, write an `else` statement. 
# If the character is not in our `vowels` string, it MUST be a consonant!

# Problem 9: If it's a consonant, Stuart gets the points! 
# Inside the `else` block, calculate the substrings using the same math trick `(length - i)`.
# Add this number to `stuart_score`.
        else:
            stuart_score = length - i

# Problem 10 (MINI-BOSS: THE SCORING ENGINE):
# Review your loop. You should be looping through indices, checking if the character at that index is a vowel, and mathematically adding the correct number of substrings to either Kevin or Stuart's score. 



# ==========================================
# SET 3: DETERMINING THE WINNER
# ==========================================

# MINI-LESSON: EVALUATING THE RESULTS
# Once the `for` loop is completely finished, all the points have been tallied. 
# Now we just need to figure out who has the bigger number.

# Problem 11: OUTSIDE and BELOW your `for` loop (make sure your indentation is correct), 
# write an `if` statement to check if `stuart_score` is strictly greater than `kevin_score`.
    if stuart_score > kevin_score:

# Problem 12: Inside that `if` block, print Stuart's name and his score separated by a space.
# (Hint: An f-string like `f"Stuart {stuart_score}"` is perfect here).
        print(f"Stuart {stuart_score}")

# Problem 13: Write an `elif` statement to check if `kevin_score` is strictly greater than `stuart_score`.
    elif kevin_score > stuart_score:

# Problem 14: Inside that `elif` block, print Kevin's name and score separated by a space using an f-string.
        print(f"Kevin {kevin_score}")

# Problem 15 (MINI-BOSS: TIE GAME):
# What if they have the exact same score? 
# Write an `else` statement. Inside it, just print the exact word `"Draw"`.
    else:
        print("Draw")


# ==========================================
# SET 4: DRIVER CODE & GRAND FINALE
# ==========================================

# MINI-LESSON: THE ENTRY POINT
# We have a beautiful function, but it won't run unless something calls it! 

# Problem 16: Outside the function, at the very bottom of the file (no indentation), 
# write the standard execution block: `if __name__ == '__main__':`
if __name__ == '__main__':


# Problem 17: Inside this block, create a variable `s`. 
# Set it equal to `input()` so HackerRank can pass the test string to us.
    s = input()

# Problem 18: Call your `minion_game` function! 
# Pass your newly created variable `s` into the function's parentheses.
    minion_game(s)

# Problem 19 (No code needed): 
# Take a deep breath. You just turned a massive, complex string-parsing nightmare into a highly optimized, $O(N)$ mathematical algorithm! 
    

# Problem 20 (THE GRAND FINALE):
# Assemble your full script! The function, the variables, the loop, the math trick, the winner logic, and the driver code.


# ==========================================
# ASSEMBLE YOUR COMPLETE SCRIPT BELOW:
# ==========================================