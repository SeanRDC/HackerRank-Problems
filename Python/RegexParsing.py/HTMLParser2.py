# ==========================================
# BLOCK 1: Newlines and String Classification
# ==========================================

# ---------------------------------------------------------
# Problem 1: Detecting Newlines
# ---------------------------------------------------------
# To figure out if a comment is multi-line, we have to look for newlines.
# Task: Write a loop that goes through the list `comments` below.
# If the string contains a newline character ('\n'), print "Has newline".
# Otherwise, print "No newline".
#
# MOCK INPUT:
comments = ["Just a normal comment", "A comment\nwith a line break"]
#
# EXPECTED OUTPUT:
# No newline
# Has newline

# Write your code for Problem 1 here:
import re

for text in comments:
    has = bool(re.search(r'[\r\n]', text))
    if has:
        print("Has newline")
    else:
        print("No newline")
        
# ---------------------------------------------------------
# Problem 2: The Exact Match Edge Case
# ---------------------------------------------------------
# HackerRank tells us: "Do not print data if data == '\n'".
# Task: Loop through the list `data_nodes`. 
# If the string is EXACTLY equal to '\n', print "Skip". 
# Otherwise, print "Keep".
#
# MOCK INPUT:
data_nodes = ["Hello World", "\n", "   "]
#
# EXPECTED OUTPUT:
# Keep
# Skip
# Keep

# Write your code for Problem 2 here:
for i in data_nodes:
    if i == "\n":
        print("Skip")
    else:
        print("Keep")
        
# ---------------------------------------------------------
# Problem 3: Single vs. Multi-line Classification
# ---------------------------------------------------------
# Let's combine this logic.
# Task: Write a function `classify_comment(text)` that takes a string.
# If the string contains '\n', print "Multi-line".
# If it does not contain '\n', print "Single-line".
#
# MOCK INPUT / EXECUTION:
# classify_comment("One line")
# classify_comment("Line one\nLine two")
#
# EXPECTED OUTPUT:
# Single-line
# Multi-line

# Write your code for Problem 3 here:
def classify_comment(text):
    for i in text:
        if i == "\n":
            print("New-line")
            
    for string in text:
        has = bool(re.search(r'[\r\n]', string))
        if has:
            print("Multi-line")
        else:
            print("Single-line")

classify_comment("One line")
classify_comment("Line one\nLine two")
classify_comment("\n")

# ---------------------------------------------------------
# Problem 4: Printing the Headers and Data
# ---------------------------------------------------------
# The HackerRank output format requires specific headers.
# Task: Write a function `print_data(text)` that takes a string.
# If the string is EXACTLY '\n', do nothing (use `pass` or `return`).
# Otherwise, print ">>> Data" followed by the text on the next line.
#
# MOCK INPUT / EXECUTION:
# print_data("Welcome to HackerRank")
# print_data("\n")
# print_data("End of page")
#
# EXPECTED OUTPUT:
# >>> Data
# Welcome to HackerRank
# >>> Data
# End of page

# Write your code for Problem 4 here:
def print_data(text):
    if text == "\n":
        pass
    else:
        print(f">>> Data\n{text}")
        
print_data("Welcome to HackerRank")
print_data("\n")
print_data("End of page")

# ---------------------------------------------------------
# Problem 5: The Full Comment Printer
# ---------------------------------------------------------
# Task: Write a function `print_comment(text)` that checks for newlines.
# If it has a newline, print ">>> Multi-line Comment" followed by the text.
# If it does NOT have a newline, print ">>> Single-line Comment" followed by the text.
#
# MOCK INPUT / EXECUTION:
# print_comment("This is hidden")
# print_comment("Hidden\non two lines")
#
# EXPECTED OUTPUT:
# >>> Single-line Comment
# This is hidden
# >>> Multi-line Comment
# Hidden
# on two lines

# Write your code for Problem 5 here:
def print_comment(text):
    if bool(re.search(r'[\r\n]', text)):
        print(f">>> Multi-line Comment\n{text}")
    else:
        print(f">>> Single-line Comment\n{text}")
        
print_comment("This is hidden")
print_comment("Hidden\non two lines")