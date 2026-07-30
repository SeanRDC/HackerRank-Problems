# ==========================================
# PRECODE: THE ASCII ART DICTIONARY
# ==========================================
# CONCEPT: DICTIONARY MAPPING
# We cannot change font sizes in the terminal. To make big numbers, we use ASCII art!
# This dictionary maps a string character (like '0') to a list of 3 strings (the top, middle, and bottom of the number).
DIGITS = {
    '0': [" _ ", "| |", "|_|"],
    '1': ["   ", "  |", "  |"],
    '2': [" _ ", " _|", "|_ "],
    '3': [" _ ", " _|", " _|"],
    '4': ["   ", "|_|", "  |"],
    '5': [" _ ", "|_ ", " _|"],
    '6': [" _ ", "|_ ", "|_|"],
    '7': [" _ ", "  |", "  |"],
    '8': [" _ ", "|_|", "|_|"],
    '9': [" _ ", "|_|", " _|"],
    ':': ["   ", " o ", " o "],
    ' ': ["   ", "   ", "   "]
}


# ==========================================
# SET 1: IMPORTS & THE GAME LOOP
# ==========================================

# MINI-LESSON: LIBRARIES AND THE INFINITE LOOP
# 1. Libraries: Python doesn't load everything at once to save memory. We must manually import tools.
#    - `os`: Lets us send commands directly to your computer's operating system (like "clear the screen").
#    - `time`: Lets us manipulate the flow of the program (like pausing execution).
#    - `datetime`: The ultimate tool for reading the computer's internal clock.
# 2. The Game Loop: A live clock is just a program that never finishes. We use `while True:` to create an infinite loop. 

# Problem 1: Import the three modules we need.
# Write: 
# `import os`
# `import time`
# `from datetime import datetime`


# Problem 2: Start the infinite heartbeat of our app. 
# Write: `while True:`


# Problem 3: Inside the loop (indented), take a snapshot of the exact current time.
# Create a variable `now` and set it equal to `datetime.now()`.


# Problem 4: If we just print the time, our terminal will scroll endlessly. We must wipe the screen first!
# Different operating systems use different commands to clear the terminal. 
# Write this exact line to make your code cross-platform: 
# `os.system('cls' if os.name == 'nt' else 'clear')`


# Problem 5 (MINI-BOSS: THE PAUSE):
# We must tell the program to go to sleep for exactly 1 second at the end of every loop so we don't crash the computer.
# Leave a blank line for our future code, and at the bottom of the loop write: `time.sleep(1)`.
# Put `pass` right above the sleep command for now, and send Set 1 over for review!



# ==========================================
# SET 2: PARSING THE TIME & DATE
# ==========================================

# MINI-LESSON: STRING FORMAT TIME (strftime)
# The `now` variable holds a massive object with everything from milliseconds to timezones.
# To extract just what we want, we use the `.strftime()` method.
# %I = 12-hour format    |    %M = Minutes
# %S = Seconds           |    %p = AM/PM
# %B = Full Month Name   |    %d = Day of month    |    %Y = 4-digit Year
# %A = Full Weekday Name

# Problem 6: Delete `pass`. Let's grab the Hours and Minutes for our big ASCII numbers.
# Create `time_str` and set it to `now.strftime("%I:%M")`.


# Problem 7: Grab the seconds for the small numbers next to the clock.
# Create `sec_str` and set it to `now.strftime("%S")`.


# Problem 8: Grab the AM / PM indicator.
# Create `ampm` and set it to `now.strftime("%p")`.


# Problem 9: The date in the image is "MARCH 11 2013" (fully capitalized). 
# Create `date_str` and set it to `now.strftime("%B %d %Y").upper()`.


# Problem 10 (MINI-BOSS: EXTRACTING THE DAY):
# The day in the image is "MONDAY".
# Create `day_str` and set it to `now.strftime("%A").upper()`.



# ==========================================
# SET 3: BUILDING THE ASCII CLOCK
# ==========================================

# MINI-LESSON: HORIZONTAL PRINTING IN A VERTICAL WORLD
# The terminal can only print text top-to-bottom, left-to-right. 
# We must build the clock ROW BY ROW. We look at the first row of the first number, attach the first row of the second number, and so on.

# Problem 11: Create three empty string variables to hold our rows as we build them.
# `row1 = ""`
# `row2 = ""`
# `row3 = ""`


# Problem 12: We need to iterate through our "HH:MM" string.
# Write a `for` loop: `for char in time_str:`


# Problem 13: Inside the `for` loop, fetch the 3-piece ASCII art for the current character.
# Create a variable `art` and set it to `DIGITS[char]`.


# Problem 14: Still inside the loop, append (`+=`) the pieces to their respective rows!
# We add a space `" "` at the end of each piece so the numbers don't squish together.
# `row1 += art[0] + " "`
# `row2 += art[1] + " "`
# `row3 += art[2] + " "`


# Problem 15 (MINI-BOSS: THE SECONDS TRICK):
# OUTSIDE the `for` loop (un-indented back to the main `while` loop level), attach the seconds to the very end of row 3!
# Write: `row3 += f" {sec_str}"`



# ==========================================
# SET 4: COLORING, ALIGNMENT, AND ASSEMBLY
# ==========================================

# MINI-LESSON: DYNAMIC ALIGNMENT
# We want the AM/PM indicator to sit perfectly flush with the right side of the seconds. 
# We can calculate the exact length of `row3` and use an f-string to push the AM/PM text that exact number of spaces to the right.

# Problem 16: Let's define our color variables so we don't have to memorize ANSI codes.
# `GREEN = '\033[92m'`
# `RESET = '\033[0m'`


# Problem 17: Measure the width of our clock, then print the AM/PM indicator right-aligned!
# Create a variable `clock_width = len(row3)`
# On the next line, print the AM/PM text using f-string alignment: `print(f"{GREEN}{ampm:>{clock_width}}{RESET}")`


# Problem 18: Print the 3 rows of our ASCII clock!
# Write three separate print statements for `row1`, `row2`, and `row3`.
# Example: `print(f"{GREEN}{row1}{RESET}")`


# Problem 19: We need some breathing room between the clock and the date.
# Write a blank `print()` statement.


# Problem 20 (THE GRAND FINALE):
# Print the Date and the Day on the very bottom line! 
# Write: `print(f"{GREEN}{date_str}      {day_str}{RESET}")`


# ==========================================
# ASSEMBLE YOUR COMPLETE SCRIPT BELOW:
# ==========================================