# ==========================================
# SET 1: THE HAPPY PATH (String to Integer)
# ==========================================

# MINI-LESSON: TYPE CASTING
# Python takes input as strings by default. If a user types "3", Python sees it as the word "3", not the math number 3. 
# We use the built-in `int()` function to force (or "cast") a string into an integer.

# Problem 1: Let's do a practice run outside the main code. 
# Create a dummy variable called `test_string` and set it equal to the string `"12345"`.
test_string = "12345"

# Problem 2: Create a new variable called `test_integer`. 
# Set it equal to `int(test_string)` to convert the word into a math number.
test_integer = int(test_string)

# Problem 3: Print your `test_integer` variable.
print(test_integer)

# Problem 4: (Concept Check - No code needed)
# What do you think would happen right now if `test_string` was `"hello"` instead of `"12345"`?
# Answer: Python would panic. It would throw a massive red error called a `ValueError` and the entire program would crash immediately.


# Problem 5 (MINI-BOSS: THE HAPPY PATH):
# Group your code together. Define a string "99", convert it to an integer, and print it. 
# (You can comment this out once you see it prints 99 successfully). Send Set 1 over for review!
string = "99"
integer = int(string)
print(f"{integer} is {type(integer)}")

# ==========================================
# SET 2: THE SAFETY NET (Try / Except)
# ==========================================

# MINI-LESSON: EXCEPTION HANDLING
# To stop Python from crashing when it hits an error, we put our risky code inside a `try` block. 
# It tells Python: "Try to do this, but if it blows up, don't crash! Just jump to my backup plan."

# Problem 6: We are going to write the real logic now. 
# Assume we have a variable called `S` that contains the user's input.
# Write the keyword `try:` (This opens the safe zone block).
S = input()
try:

# Problem 7: Inside the `try` block (indented), take the variable `S` and convert it to an integer.
# You can store it in a variable, or just write `print(int(S))` directly.
    print(int(S))

# Problem 8: (Concept Check - No code needed). 
# If `S` is "3", the `try` block succeeds and prints 3. But what if `S` is "za"?
# If the `try` block fails, Python immediately stops what it's doing and looks for an `except` block.


# Problem 9: OUTSIDE the `try` block (un-indented back to the same level as `try`), 
# write the keyword `except:`
except:

# Problem 10 (MINI-BOSS: THE BACKUP PLAN):
# Inside the `except` block (indented), write the backup plan. 
# The instructions say if it fails to convert, we must print "Bad String".
# Write that print statement here. 
    print("Bad String")


# ==========================================
# SET 3: CATCHING SPECIFIC ERRORS
# ==========================================

# MINI-LESSON: SPECIFIC EXCEPTIONS
# A bare `except:` catches EVERYTHING. If you accidentally unplug your keyboard, it might print "Bad String". 
# Good programmers specify exactly which error they are expecting to catch. When `int("za")` fails, Python throws a `ValueError`.

# Problem 11: Go back to your `except:` line from Problem 9. 
# Change it to specifically catch a ValueError. 
# Syntax: `except ValueError:`


# Problem 12: Inside this specific `except ValueError:` block, ensure you are still printing "Bad String".


# Problem 13: (Concept Check - No code needed). 
# Notice how we didn't use a single `if/else` statement? We didn't check if the string had letters in it. We just blindly attempted the conversion and caught the error. This is a very "Pythonic" way to code, often called EAFP (Easier to Ask for Forgiveness than Permission).


# Problem 14: Is there any other code needed for our logic? 
# No! The `try/except` block is the entire brain of this script. 


# Problem 15 (MINI-BOSS: THE FULL LOGIC):
# Assemble your complete `try` and `except ValueError` block. 
# (Assume the variable `S` exists right above it).



# ==========================================
# SET 4: DRIVER CODE & GRAND FINALE
# ==========================================

# MINI-LESSON: THE DRIVER CODE
# HackerRank just provides the string to us via `input()`. We just need to grab it and feed it into our logic.

# Problem 16: At the bottom of your file (no indentation), write the main execution block:
# `if __name__ == '__main__':`


# Problem 17: Inside this block, create a variable `S`. 
# Set it equal to `input()` to grab the user's string.


# Problem 18: To be extra safe with inputs, it is a good habit to strip away any accidental spaces the user might have typed.
# Modify your input to: `S = input().strip()`


# Problem 19: Now, take your completed `try` / `except ValueError` block from Set 3, 
# and paste it right below your `S` variable, INSIDE the `if __name__` block.


# Problem 20 (THE GRAND FINALE):
# Assemble your full script! The main execution block, grabbing the input string, trying to print it as an integer, and catching the ValueError to print "Bad String".


# ==========================================
# ASSEMBLE YOUR COMPLETE SCRIPT BELOW:
# ==========================================