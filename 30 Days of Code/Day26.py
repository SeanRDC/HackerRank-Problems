# =====================================================================
# THE PROBLEM: Calculate a library fine based on expected vs. actual return dates.
# THE GOAL: Build the date parsing and nested logic blocks piece-by-piece, 
# test them individually, and then assemble them into the final algorithm.
# =====================================================================

# ---------------------------------------------------------
# BLOCK A: DATA PARSING
# ---------------------------------------------------------

# Problem 1: Create a variable `date_str` set to "9 6 2015". 
# Split this string into a list of strings.
# Expected Output: ['9', '6', '2015']
date_str = "9 6 2015"
print(list(date_str.split()))

# Problem 2: Take the list from Problem 1 and convert every element into an integer.
# Expected Output: [9, 6, 2015]
date_list = list(map(int, date_str.split()))

# Problem 3: Given the list `[9, 6, 2015]`, unpack it directly into three variables: `d1`, `m1`, `y1`.
# Print `m1`.
# Expected Output: 6
d1, m1, y1 = date_list
print(m1)

# Problem 4: Combine Problems 1-3 into a single line of code. 
# Create `d2`, `m2`, `y2` by splitting and mapping "6 6 2015".
# Print `y2`.
# Expected Output: 2015
d2, m2, y2 = list(map(int, date_str.split()))
print(y2)

# ---------------------------------------------------------
# BLOCK B: DAY LOGIC (Assume same month and same year)
# ---------------------------------------------------------

# Problem 5: Write a function `check_days(d1, d2)`. 
# If `d1 > d2`, calculate and return the fine (15 * days late).
# Otherwise, return 0.
def check_days(d1, d2):
    if d1 > d2:
        days_late = d1 - d2
        return (15 * days_late)
    else:
        return 0

# Problem 6: Call `check_days(9, 6)` and print the result.
# Mock Input: d1=9, d2=6
# Expected Output: 45
print(check_days(9, 6))

# Problem 7: Call `check_days(5, 6)` and print the result.
# Mock Input: d1=5, d2=6
# Expected Output: 0
print(check_days(5, 6))


# ---------------------------------------------------------
# BLOCK C: MONTH LOGIC (Assume same year)
# ---------------------------------------------------------

# Problem 8: Write a function `check_months(m1, m2)`.
# If `m1 > m2`, calculate and return the fine (500 * months late).
# Otherwise, return 0.
def check_months(m1, m2):
    if m1 > m2:
        months_late = m1 - m2
        return (500 * months_late)
    else:
        return 0 
# Problem 9: Call `check_months(8, 5)` and print the result.
# Mock Input: m1=8, m2=5
# Expected Output: 1500
print(check_months(8, 5))

# Problem 10: Call `check_months(3, 5)` and print the result.
# Mock Input: m1=3, m2=5
# Expected Output: 0
print(check_months(3, 5))

# ---------------------------------------------------------
# BLOCK D: COMBINING MONTH AND DAY (Assume same year)
# ---------------------------------------------------------

# Problem 11: Write a function `same_year(d1, d2, m1, m2)`.
# Inside, check if `m1 == m2`. If true, return the result of `check_days(d1, d2)`.
def same_year(d1, d2, m1, m2):
    if m1 == m2:
        return check_days(d1, d2)

# Problem 12: Inside `same_year`, add a check: if `m1 > m2`, 
# return the result of `check_months(m1, m2)`.
    elif m1 > m2:
        return check_months(m1, m2)

# Problem 13: Inside `same_year`, add a check: if `m1 < m2`, return 0.
    elif m1 < m2:
        return 0

# Problem 14: Call `same_year(9, 6, 6, 6)` and print the result.
# Mock Input: d1=9, d2=6, m1=6, m2=6
# Expected Output: 45
print(same_year(9, 6, 6, 6))

# Problem 15: Call `same_year(1, 6, 7, 6)` and print the result.
# Mock Input: d1=1, d2=6, m1=7, m2=6
# Expected Output: 500
print(same_year(1, 6, 7, 6))


# ---------------------------------------------------------
# BLOCK E: YEAR LOGIC AND FINAL ASSEMBLY
# ---------------------------------------------------------

# Problem 16: Write a final function `library_fine(d1, m1, y1, d2, m2, y2)`.
# Inside, check if `y1 > y2`. If true, return the fixed fine of 10000.


# Problem 17: Inside `library_fine`, check if `y1 < y2`. If true, return 0.


# Problem 18: Inside `library_fine`, handle the last remaining possibility (`y1 == y2`).
# If true, return the result of your `same_year(d1, d2, m1, m2)` function!


# Problem 19: Call `library_fine(1, 1, 2016, 31, 12, 2015)` and print the result.
# Mock Input: Actual=(1, 1, 2016), Expected=(31, 12, 2015)
# Expected Output: 10000


# Problem 20: Call `library_fine(31, 12, 2014, 1, 1, 2015)` and print the result.
# Mock Input: Actual=(31, 12, 2014), Expected=(1, 1, 2015)
# Expected Output: 0

# =====================================================================
# FINAL SUBMISSION
# Once all 20 building blocks work perfectly, you can combine your logic 
# into one clean, continuous script below to paste into HackerRank!
# =====================================================================