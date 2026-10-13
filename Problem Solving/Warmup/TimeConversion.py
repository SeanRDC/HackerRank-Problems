#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# ===================================================================
# PRACTICE LADDER - 9 small problems that build up to timeConversion
# ===================================================================
# Solve them in order. Each one adds exactly ONE new idea.
# Write each as its own small function and compare against the
# sample output before moving on.
#
# ---------------------------------------------------------------
# PROBLEM 1 - The last two characters
# ---------------------------------------------------------------
# Given a 12-hour time string, return just the AM/PM part.
# New idea: slicing from the END of a string with a negative index.
#
#   Input:  "07:05:45PM"
#   Output: PM
#
#   Input:  "12:00:00AM"
#   Output: AM
def last_two_char(s):
    return s[-2:]

print(last_two_char("07:05:45PM"))
print(last_two_char("12:00:00AM"))
# ---------------------------------------------------------------
# PROBLEM 2 - The front and the middle
# ---------------------------------------------------------------
# Return the hour part, then everything between the hour and the AM/PM.
# New idea: a slice with BOTH a start and a stop.
# Check: hour + middle + AM/PM should rebuild the original string.
#
#   Input:  "07:05:45PM"
#   Output: 07
#           :05:45
#
#   Input:  "12:00:00AM"
#   Output: 12
#           :00:00
def front_middle(s):
    return s[2:8]

print(front_middle("07:05:45PM"))
print(front_middle("12:00:00AM"))
# ---------------------------------------------------------------
# PROBLEM 3 - Text to number
# ---------------------------------------------------------------
# Given an hour as a STRING, return that hour plus 12 as a number.
# New idea: converting a string into an integer before doing math.
# Try "07" + 12 first and read the error it gives you.
#
#   Input:  "07"
#   Output: 19
#
#   Input:  "12"
#   Output: 24
def text_to_number(s):
    return int(s) + 12

print(text_to_number("07"))
print(text_to_number("12"))
# ---------------------------------------------------------------
# PROBLEM 4 - Always two digits
# ---------------------------------------------------------------
# Given an hour as a NUMBER, return it as a string that is always
# exactly two characters wide.
# New idea: a zero-padding format specifier (a cousin of the .6f
# you used in plusMinus).
# Try str() first and see why it fails on the first sample.
#
#   Input:  7
#   Output: 07
#
#   Input:  19
#   Output: 19
#
#   Input:  0
#   Output: 00
def always_two_digits(s):
    return f"{s:02d}"

print(always_two_digits(7))
print(always_two_digits(19))
print(always_two_digits(0))
# ---------------------------------------------------------------
# PROBLEM 5 - Swap the hour
# ---------------------------------------------------------------
# Given a 12-hour time string and a new hour as a NUMBER, return the
# time with the hour replaced and the AM/PM removed.
# New idea: gluing pieces back together (problem 2 + problem 4).
# No clock logic yet, the new hour is handed to you.
#
#   Input:  "07:05:45PM", 19
#   Output: 19:05:45
#
#   Input:  "12:01:00AM", 0
#   Output: 00:01:00
def swap_the_hour(time, hour):
    remove = time[2:8]
    return f"{hour:02d}{remove}"

print(swap_the_hour("07:05:45PM", 19))
print(swap_the_hour("12:01:00AM", 0))
# ---------------------------------------------------------------
# PROBLEM 6 - PM hours
# ---------------------------------------------------------------
# Given an hour from 1 to 12 that is known to be PM, return the
# 24-hour version as a number.
# New idea: a rule with ONE exception. Work out which PM hour does
# not follow the "add 12" rule.
#
#   Input:  7
#   Output: 19
#
#   Input:  1
#   Output: 13
#
#   Input:  12
#   Output: 12
def pm_hours(n):
    if n == 12:
        return 12
    else:
        return n+12

print(pm_hours(7))
print(pm_hours(1))
print(pm_hours(12))
# ---------------------------------------------------------------
# PROBLEM 7 - AM and PM hours
# ---------------------------------------------------------------
# Given an hour from 1 to 12 and "AM" or "PM", return the 24-hour
# version as a number.
# New idea: the mirror-image exception on the AM side, so the branch
# now depends on TWO things at once (the period and the hour).
#
#   Input:  7, "AM"
#   Output: 7
#
#   Input:  7, "PM"
#   Output: 19
#
#   Input:  12, "AM"
#   Output: 0
#
#   Input:  12, "PM"
#   Output: 12
def am_pm_hours(hour, period):
    if period == "AM":
        if hour == 12:
            print(0)
        else:
            print(hour)
        
    else:
        if hour == 12:
            print(12)
        else:
            print(hour + 12)

am_pm_hours(7, "AM")
am_pm_hours(7, "PM")
am_pm_hours(12, "AM")
am_pm_hours(12, "PM")

# ---------------------------------------------------------------
# PROBLEM 8 - Same shape, different question
# ---------------------------------------------------------------
# Go the other way: given a 24-hour time string, return the 12-hour
# version with AM/PM on the end.
# New idea: nothing new, and that is the point. Slice, convert,
# branch, pad, glue. If you can reverse the direction without
# looking back, you own the pattern.
#
#   Input:  "19:05:45"
#   Output: 07:05:45PM
#
#   Input:  "07:05:45"
#   Output: 07:05:45AM
#
#   Input:  "00:01:00"
#   Output: 12:01:00AM
#
#   Input:  "12:01:00"
#   Output: 12:01:00PM
def different_question(s):
    hh, mm, ss = s.split(':')
    hour24 = int(hh)
    
    if hour24 == 0:
        hour12 = 12
        period = "AM"
        
    elif hour24 == 12:
        hour12 = 12
        period = "PM"
        
    elif hour24 > 12:
        hour12 = hour24 - 12
        period = "PM"
    else:
        hour12 = hour24
        period = "AM"
        
    return f"{hour12:02d}:{mm}:{ss}{period}"

print(different_question("19:05:45"))
print(different_question("07:05:45"))
print(different_question("00:01:00"))
print(different_question("12:01:00"))

# ---------------------------------------------------------------
# PROBLEM 9 - Time Conversion (the real thing, solve it below)
# ---------------------------------------------------------------
# Given a time in 12-hour AM/PM format, return it in 24-hour format.
#
#   Input:  "07:05:45PM"
#   Output: 19:05:45
#
#   Input:  "06:40:03AM"
#   Output: 06:40:03
#
#   Input:  "12:01:00AM"
#   Output: 00:01:00
#
#   Input:  "12:01:00PM"
#   Output: 12:01:00
#

def timeConversion(s):
    period = s[-2:]
    pure_time = s[:-2]
    
    hh, mm, ss = pure_time.split(':')
    hour12 = int(hh)
    
    if period == "AM":
        if hour12 == 12:
            hour24 = 0
        else:
            hour24 = hour12
    elif period == "PM":
        if hour12 == 12:
            hour24 = 12
        else:
            hour24 = hour12 + 12
            
    if hour24 < 10:
        hour24_string = "0" + str(hour24)
    else:
        hour24_string = str(hour24)
        
    return f"{hour24_string}:{mm}:{ss}"

print(timeConversion("07:05:45PM"))
print(timeConversion("06:40:03AM"))
print(timeConversion("12:01:00AM"))
print(timeConversion("12:01:00PM"))