# ==========================================
# SET 1: THE INVISIBLE BOXES
# ==========================================
# By default, alignment methods fill extra space with empty spaces (" ").
# You can optionally pass a second character to see the "box".

# Problem 1: Create a string `word = "Hacker"`. 
# Use `.ljust()` to put it in a box of width 15, using "-" as the fill character. Print it.
# Expected Output: Hacker---------

# Problem 2: Put `word` in a box of width 15 using `.rjust()`, filling with "*". Print it.
# Expected Output: *********Hacker

# Problem 3: Put `word` in a box of width 15 using `.center()`, filling with "_". Print it.
# Expected Output: ____Hacker_____

# Problem 4: If you don't provide a fill character, Python uses spaces.
# Print `word` centered in a box of width 20 (no fill character).

# Problem 5: String multiplication is crucial here. 
# Print the letter "H" multiplied by 5. 
# Expected Output: HHHHH


# ==========================================
# SET 2: BUILDING THE SHAPES
# ==========================================
# Let's build the pieces of the logo on a miniature scale (thickness = 3).

c = "H"

# Problem 6 (Left side of a cone): 
# Write a `for` loop where `i` goes from 0 to 2 (using `range(3)`).
# Inside, multiply `c` by `i`. Right-justify that string in a width of 3. Print it.
# Expected Output: 
#   (blank space)
#  H
# HH

# Problem 7 (Right side of a cone): 
# In a new `for` loop (`range(3)`), multiply `c` by `i`. 
# Left-justify it in a width of 3. Print it.
# Expected Output:
#   (blank space)
# H  
# HH 

# Problem 8 (The Full Top Cone): 
# Combine them! In a `range(3)` loop, print:
# (Left side right-justified) + center "H" + (Right side left-justified)
# Expected Output:
#   H  
#  HHH 
# HHHHH

# Problem 9 (The Pillars): 
# Print `"HHH"` centered in a box of width 6.
# Expected Output:  HHH  

# Problem 10 (The Belt):
# Print `"HHHHHHHHHHHHHHH"` centered in a box of width 18.


# ==========================================
# SET 3: ADVANCED MOVEMENT
# ==========================================
# The bottom cone in the logo points down AND is pushed all the way to the right.

# Problem 11 (Inverted Loop): 
# Write a `for` loop `range(3)`. Inside, print `3 - i - 1`.
# Expected Output:
# 2
# 1
# 0

# Problem 12 (Bottom Cone - Just the shape):
# In a `range(3)` loop, multiply `c` by `(3 - i - 1)`. 
# Use the same logic from Problem 8 to make a downward-pointing cone.
# Expected Output:
# HHHHH
#  HHH 
#   H  

# Problem 13 (The Giant Shift):
# Take the string "Move Me" and right-justify it in a massive box of width 40.

# Problem 14 (Moving the Cone):
# Take your print statement from Problem 12. Wrap the ENTIRE thing in parentheses,
# and right-justify the whole cone in a width of 20.

# Problem 15 (Dynamic Variables):
# Set `t = 5`. Print `c * (t * 5)` centered in a width of `t * 6`.


# ==========================================
# SET 4: THE GRAND FINALE
# ==========================================
# Time to solve the HackerRank puzzle! 
# Look at the code provided in the HackerRank prompt. You need to replace the `______` blanks.
# Write down whether each blank should be `ljust`, `rjust`, or `center`.

# Problem 16: Top Cone left side blank -> `(c*i).______(thickness-1)`
# What alignment pushes the H's to the right so they connect with the middle?

# Problem 17: Top Cone right side blank -> `(c*i).______(thickness-1)`
# What alignment pushes the H's to the left so they connect with the middle?

# Problem 18: Top Pillars blanks -> `(c*thickness).______(thickness*2)`
# The pillars are floating perfectly in the middle of their designated zones. Which method does this?

# Problem 19: Middle Belt blank -> `(c*thickness*5).______(thickness*6)`
# The belt is floating perfectly in the middle of the screen.

# Problem 20: Bottom Cone blanks
# The inner blanks form the downward cone shape: `(c*(thickness-i-1)).______(thickness)`
# The final outer blank shifts the ENTIRE cone to the far right side of the screen: `.______(thickness*6)`

# Once you figure out the words for 16-20, drop them into the HackerRank editor and run it!