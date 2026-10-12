#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

# ===================================================================
# PRACTICE LADDER - 7 small problems that build up to staircase
# ===================================================================
# Solve them in order. Each one adds exactly ONE new idea.
# Write each as its own small function and compare against the
# sample output before moving on.
#
# In the samples below, every output starts in the same column (the
# one where the first "#" of problem 1 sits). Any gap to the right of
# that column is REAL leading spaces that your code must print.
#
# ---------------------------------------------------------------
# PROBLEM 1 - Do it n times
# ---------------------------------------------------------------
# Given n, print a single "#" on n separate lines.
# New idea: a `for` loop over range(n). There is no list this time,
# the loop exists only to repeat something a set number of times.
#
#   Input:  3
#   Output:
#           #
#           #
#           #
#
#   Input:  1
#   Output:
#           #
def do_it_n_times(n):
    for _ in range(n):
        print('#')

do_it_n_times(3)
# ---------------------------------------------------------------
# PROBLEM 2 - Row numbers
# ---------------------------------------------------------------
# Given n, print the numbers 1 up to n, one per line.
# New idea: range() starts at 0 and leaves out its stop value.
# Find a way to make the loop variable go 1, 2, ..., n.
#
#   Input:  4
#   Output:
#           1
#           2
#           3
#           4
#
#   Input:  1s
#   Output:
#           1
n = 4
for i in range(1, n + 1):
    print(i)

# ---------------------------------------------------------------
# PROBLEM 3 - Many on one line
# ---------------------------------------------------------------
# Given n, print n "#" symbols on ONE line, with no loop.
# New idea: multiplying a string by an integer.
# Try "ab" * 3 in a terminal first.
#
#   Input:  4
#   Output:
#           ####
#
#   Input:  1
#   Output:
#           #

print("#" * 4)
# ---------------------------------------------------------------
# PROBLEM 4 - Growing rows
# ---------------------------------------------------------------
# Given n, print n lines where row 1 has 1 hash, row 2 has 2 hashes,
# and so on. No spaces anywhere.
# New idea: problems 2 and 3 combined. The loop variable decides how
# long each line is.
#
#   Input:  4
#   Output:
#           #
#           ##
#           ###
#           ####
#
#   Input:  2
#   Output:
#           #
#           ##
def growing_rows(n):
    for i in range(1, n+1):
        print("#" * i)

growing_rows(4)
growing_rows(2)

# ---------------------------------------------------------------
# PROBLEM 5 - The other count
# ---------------------------------------------------------------
# Given n, print for each row how many SPACES that row of the
# staircase needs, one number per line. Row 1 needs n - 1 spaces,
# the last row needs 0.
# New idea: a formula that uses BOTH n and the row number.
# Hint: spaces + hashes always equals the same thing on every row.
#
#   Input:  4
#   Output:
#           3
#           2
#           1
#           0
#
#   Input:  2
#   Output:
#           1
#           0
def the_other_count(n):
    for i in range(n - 1, -1, -1):
        print(i)
the_other_count(4)

# ---------------------------------------------------------------
# PROBLEM 6 - One padded line
# ---------------------------------------------------------------
# Given width and k, print k hashes pushed to the RIGHT so the whole
# line is exactly `width` characters long.
# New idea: building two repeated strings and joining them with +.
# Do not pass them to print() as two arguments: problem 6 of
# MinMaxSum showed what print() puts between its arguments.
#
#   Input:  4, 1
#   Output:
#              #
#   (3 spaces, then 1 hash)
#
#   Input:  4, 3
#   Output:
#            ###
#   (1 space, then 3 hashes)
#
#   Input:  4, 4
#   Output:
#           ####
#   (0 spaces, then 4 hashes)
def one_padded_line(width, k):
    space = width - k
    line = (" " * space) + ("#" * k)
    print(line)
    
one_padded_line(4, 4)
        
# ---------------------------------------------------------------
# PROBLEM 7 - Staircase (the real thing, solve it below)
# ---------------------------------------------------------------
# Given n, print a right-aligned staircase of height n and width n.
# Every line is exactly n characters: spaces first, then hashes.
# Problem 4 gives you the hashes, problem 5 gives you the spaces,
# problem 6 glues them into one line.
#
#   Input:  4
#   Output:
#              #
#             ##
#            ###
#           ####
#
#   Input:  6
#   Output:
#                #
#               ##
#              ###
#             ####
#            #####
#           ######
#
#   Input:  1
#   Output:
#           #
#

def staircase(n):
    # Write your code here
    for k in range(1, n + 1):
        spaces = ' ' * (n -k)
        hashes = '#' * k
        print(spaces + hashes)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
