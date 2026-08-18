# ==============================================================================
# FUNDAMENTALS CURRICULUM: DATETIME PARSING & TIMEDELTAS
# ==============================================================================
# Goal: Parse complex timestamp strings containing timezones into Python datetime 
# objects, calculate the exact difference between them, and output the absolute 
# difference in total seconds.
# ==============================================================================

# ---------------------------------------------------------
# CONCEPT BLOCK 1: STRPTIME (STRING PARSE TIME) FORMATTING
# ---------------------------------------------------------
# Python reads time strings using specific % codes. Let's learn the codes.

# Problem 1: The Import
# Concept: We need the `datetime` class from the `datetime` module. 
# Write the import statement to bring in `datetime`.
from datetime import datetime
now = datetime.now()
# Problem 2: Parsing the Day of the Week
# Concept: The string starts with "Sun". The format code for an abbreviated 
# weekday is `%a`. Create a string variable `fmt_day = "%a"`.
fmt_day = "%a"
# Problem 3: Parsing the Date
# Concept: The next part is "10 May 2015". 
# The codes are `%d` (day), `%b` (abbreviated month), and `%Y` (4-digit year).
# Create a string variable `fmt_date` combining these with spaces.
fmt_date = "%d %b %Y"
# Problem 4: Parsing the Time
# Concept: The time is "13:54:36".
# The codes are `%H` (24hr hour), `%M` (minute), `%S` (second).
# Create a string variable `fmt_time` combining these with colons.
fmt_time = "%H:%M:%S"
# Problem 5: Parsing the Timezone
# Concept: The timezone is "-0700".
# The code for a UTC offset is `%z`. Create a variable `fmt_tz = "%z"`.
fmt_tz = "%z"
# Problem 6: The Master Format String
# Concept: Combine all the codes from Problems 2-5 into a single format string 
# that exactly matches "Day dd Mon yyyy hh:mm:ss +xxxx".
# Assign this to a variable called `time_format`.
time_format = "%a %d %b %Y %H:%M:%S %z"
print(time_format)
# ---------------------------------------------------------
# CONCEPT BLOCK 2: CONVERTING STRINGS TO OBJECTS
# ---------------------------------------------------------

# Problem 7: The Test String
# Concept: Create a mock string: `time_str = "Sun 10 May 2015 13:54:36 -0700"`
time_str = "Sun 10 May 2015 13:54:36 -0700"
# Problem 8: The Conversion
# Concept: Use `datetime.strptime()` passing in your `time_str` and your 
# `time_format`. Assign it to a variable `dt_obj` and print it.
# Mock Output: 2015-05-10 13:54:36-07:00
# Notice how Python translated the string into a mathematical object!
dt_obj = datetime.strptime(time_str, time_format)
print(dt_obj)
# ---------------------------------------------------------
# CONCEPT BLOCK 3: TIMEDELTA MATH
# ---------------------------------------------------------

# Problem 9: Mocking a Second Object
# Concept: Create a second mock object representing exactly one hour later 
# in the SAME timezone. (Just hardcode the string and parse it).
# `time_str_2 = "Sun 10 May 2015 14:54:36 -0700"`. Parse it to `dt_obj_2`.
time_str_2 = "Sun 10 May 2015 14:54:36 -0700"
dt_obj2 = datetime.strptime(time_str_2, time_format)
print(dt_obj2)
# Problem 10: Subtracting Time
# Concept: In Python, you can literally subtract two datetime objects using `-`.
# Write: `difference = dt_obj - dt_obj_2` and print `difference`.
# Mock Output: -1 day, 23:00:00
# (Python represents negative 1 hour as "negative 1 day plus 23 hours").
difference = dt_obj - dt_obj2
print(difference)
# Problem 11: The Absolute Difference
# Concept: We don't care which time came first. We just want the raw gap.
# Wrap your subtraction in the built-in `abs()` function. Print it.
# Mock Output: 1:00:00 (Exactly 1 hour difference!)
difference2 = abs(dt_obj - dt_obj2)
print(difference2)
# Problem 12: Total Seconds
# Concept: A timedelta object has a built-in method called `.total_seconds()`.
# Call this method on your absolute difference from Problem 11.
# Mock Output: 3600.0 (Because 60 mins * 60 secs = 3600).
print(difference2.total_seconds())
# Problem 13: Floating Point Fix
# Concept: `.total_seconds()` returns a float (3600.0). HackerRank expects 
# an integer. Wrap your total seconds calculation in `int()` and print it.
# Mock Output: 3600
print(int(difference2.total_seconds()))

# ---------------------------------------------------------
# CONCEPT BLOCK 4: TIMEZONE SHIFTING (THE INVISIBLE MATH)
# ---------------------------------------------------------

# Problem 14: The UTC Shift
# Concept: Create two strings with the EXACT same clock time, but different zones.
# `t1 = "Sun 10 May 2015 13:54:36 -0700"`
# `t1 = "Sun 10 May 2015 13:54:36 -0700`
# Parse both into datetime objects.
t1 = "Sun 10 May 2015 13:54:36 -0700"
t2 = "Sun 10 May 2015 13:54:36 -0000"
# Problem 15: Proving the Shift
# Concept: Subtract `t2` from `t1`, get the absolute value, convert to total 
# seconds, and cast to an integer. Print it.
# Mock Output: 25200 
# (Python automatically calculated the 7-hour timezone difference!)
n1 = datetime.strptime(t1, time_format)
n2 = datetime.strptime(t2, time_format)
print(int(abs(n1 - n2).total_seconds()))
# ---------------------------------------------------------
# CONCEPT BLOCK 5: INPUT ARCHITECTURE
# ---------------------------------------------------------

# Problem 16: Reading Test Cases
# Concept: The first line of input is the number of test cases. 
# Read it and convert it to an integer `T`.
T = int(input())
# Problem 17: The Outer Loop
# Concept: Write a `for` loop that runs `T` times. 
# (Use the `_` throwaway variable for the loop).

def get_time_diff(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    n1 = datetime.strptime(t1, format)
    n2 = datetime.strptime(t2, format)
    return int(abs(n1 - n2).total_seconds())

for _ in range(T):
# Problem 18: Reading the Pairs
# Concept: Inside the loop, read two sequential inputs and assign them to 
# `string_1` and `string_2`.
    string_1 = input()
    string_2 = input()
# Problem 19: The Execution Function (Optional but Clean)
# Concept: Write a function `get_time_diff(t1, t2)` that takes two raw strings, 
# parses them, and returns the integer total seconds. 

# Problem 20: The Final Print
# Concept: Inside your T loop, call your execution function with your two 
# strings and print the result.
    print(get_time_diff(string_1, string_2))
# ==========================================
# FULL SCRIPT DATA FLOW (MOCK INPUTS/OUTPUTS)
# ==========================================

# --- The Initial Input ---
# First input() receives: "2"
# T evaluates to: 2

# --- Test Case Loop 1 ---
# First string read: "Sun 10 May 2015 13:54:36 -0700"
# Object 1 created: 2015-05-10 13:54:36 (UTC -7)
#
# Second string read: "Sun 10 May 2015 13:54:36 -0000"
# Object 2 created: 2015-05-10 13:54:36 (UTC 0)
#
# Math Engine evaluates: abs(Object 1 - Object 2)
# Timedelta evaluates to: 7 hours
# Total seconds evaluates to: 25200.0
# Cast to Integer: 25200
# Console Prints: 25200

# --- Test Case Loop 2 ---
# First string read: "Sat 02 May 2015 19:54:36 +0530"
# Object 1 created: 2015-05-02 19:54:36 (UTC +5.5)
#
# Second string read: "Fri 01 May 2015 13:54:36 -0000"
# Object 2 created: 2015-05-01 13:54:36 (UTC 0)
#
# Math Engine evaluates: abs(Object 1 - Object 2)
# Timedelta evaluates to: 1 day, 0:30:00 (24.5 hours)
# Total seconds evaluates to: 88200.0
# Cast to Integer: 88200
# Console Prints: 88200