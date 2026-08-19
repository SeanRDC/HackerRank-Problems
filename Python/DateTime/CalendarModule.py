# ==============================================================================
# FUNDAMENTALS CURRICULUM: THE CALENDAR MODULE & INTEGER MAPPING
# ==============================================================================
# Goal: Parse a date string in MM DD YYYY format, determine what day of the week 
# it was using the calendar module, and output that day as an uppercase string.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: PARSING & UNPACKING (THE ORDER TRAP)
# ---------------------------------------------------------

# Problem 1: The Mock String
# Concept: Create a mock input string representing the HackerRank sample data.
# `date_str = "08 05 2015"`
date_str = "08 05 2015"
# Problem 2: String Splitting
# Concept: Split the string into a list of individual components.
# Mock Output: ['08', '05', '2015']
date_str.split()
# Problem 3: The Leading Zero Behavior
# Concept: Test how Python's built-in integer conversion handles strings with 
# leading zeros. Pass the string `"08"` into the `int()` function and print it.
# Mock Output: 8 (Python naturally strips the leading zero for you!)
print(int("08"))
# Problem 4: Mapping to Integers
# Concept: Combine Problems 2 and 3. Use `map()` and `int` on your split string 
# from Problem 2 to convert all elements into integers.
date_str1 = list(map(int, date_str.split()))
# Problem 5: Unpacking the Variables
# Concept: HackerRank gives the input in Month, Day, Year format. 
# Extract your mapped integers directly into three variables: `month`, `day`, 
# and `year` in that exact order.
# Mock Output: month=8, day=5, year=2015
print(f"month={date_str1[0]}, day={date_str1[1]}, year={date_str1[2]}")
# ---------------------------------------------------------
# CONCEPT BLOCK 2: THE CALENDAR MODULE
# ---------------------------------------------------------

# Problem 6: The Import
# Concept: We need the `calendar` module. Write the import statement.
import calendar
# Problem 7: The Weekday Function
# Concept: The module has a function called `calendar.weekday()`. However, it 
# requires its arguments in a specific order: Year, Month, Day. 
# Pass your variables from Problem 5 into this function (noting the order flip!) 
# and save it to `day_int`.
day_int = calendar.weekday(date_str1[2], date_str1[0], date_str1[1])
# Problem 8: Evaluating the Day Integer
# Concept: Print your `day_int`. 
# Mock Output: 2
# Why 2? In the calendar module, Monday is 0, Tuesday is 1, Wednesday is 2.
print(day_int)
# ---------------------------------------------------------
# CONCEPT BLOCK 3: INTEGER-TO-STRING MAPPING
# ---------------------------------------------------------

# Problem 9: The Day Name Array
# Concept: The calendar module contains a built-in array (technically a localized 
# sequence) called `calendar.day_name`. Print this object directly.
# Mock Output: <calendar._localized_day object at 0x...>

# Problem 10: Viewing the Array
# Concept: Because it's a localized sequence, wrap `calendar.day_name` in a 
# `list()` and print it to see what is inside!
# Mock Output: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Problem 11: Indexing the Array
# Concept: Now that you know it acts like a list, you can extract a specific 
# element using bracket notation. Pass your `day_int` (which is 2) into 
# `calendar.day_name[]` and print the result. Save it to `day_string`.
# Mock Output: 'Wednesday'

# ---------------------------------------------------------
# CONCEPT BLOCK 4: STRING MANIPULATION
# ---------------------------------------------------------

# Problem 12: Uppercase Casing
# Concept: HackerRank requires the output in all capital letters. 
# Call the built-in `.upper()` string method on your `day_string` and print it.
# Mock Output: 'WEDNESDAY'

# Problem 13: The One-Liner (Optional Optimization)
# Concept: Try combining Problems 11 and 12 into a single line of code! 
# Index the array and immediately call `.upper()` on the result.

# ---------------------------------------------------------
# CONCEPT BLOCK 5: THE DATETIME ALTERNATIVE (MIND EXPANSION)
# ---------------------------------------------------------
# The calendar module is great, but datetime can also do this effortlessly!

# Problem 14: Datetime Import
# Concept: Write `from datetime import datetime`.

# Problem 15: Creating the Datetime Object
# Concept: Pass your `year`, `month`, and `day` into `datetime()`. 
# Assign it to `dt_obj`. (Notice datetime also requires Year, Month, Day order).

# Problem 16: The String Format Time Method
# Concept: Use `.strftime()` on your `dt_obj`. 
# The format code for a full weekday name is `"%A"`. Print the result.
# Mock Output: 'Wednesday'

# Problem 17: Datetime Casing
# Concept: Just like in Problem 12, append `.upper()` to your `.strftime("%A")` 
# call and print the result. 
# Mock Output: 'WEDNESDAY'
# You can use either module for the final solution!

# ---------------------------------------------------------
# CONCEPT BLOCK 6: FINAL ASSEMBLY PREP
# ---------------------------------------------------------

# Problem 18: Reading the Input
# Concept: Write the `input().split()` command necessary to read the live 
# HackerRank data instead of the mock string.

# Problem 19: The Map and Unpack
# Concept: Combine Problem 4, 5, and 18. Wrap your input command in `map()` 
# and immediately unpack it into `m`, `d`, and `y`.

# Problem 20: The Final Output
# Concept: Using either `calendar` or `datetime`, pass `y`, `m`, and `d` into 
# the logic, format to uppercase, and wrap it all inside a `print()` statement!

# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- The Initial Input ---
# input() receives string: "08 05 2015"
# String is split: ['08', '05', '2015']
# Strings mapped to ints: [8, 5, 2015]
# Variables unpacked: 
#   month -> 8
#   day -> 5
#   year -> 2015

# --- The Math Engine (Calendar Module Route) ---
# year, month, day passed to calendar logic.
# logic evaluates the date (August 5, 2015).
# logic returns the day index integer: 2
#
# Index 2 is passed into the calendar names array.
# Array returns the string at index 2: "Wednesday"

# --- Formatting ---
# "Wednesday" evaluates the uppercase transformation.
# String becomes: "WEDNESDAY"

# --- Final Output ---
# Printed to console: WEDNESDAY