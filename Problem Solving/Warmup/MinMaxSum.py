#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    #
    # ---------------------------------------------------------------
    # THE IDEA
    # ---------------------------------------------------------------
    # "Sum exactly four of the five" sounds like you must try every
    # combination. You don't. Flip the question around:
    #
    #     Choosing 4 numbers to ADD is the same as
    #     choosing 1 number to LEAVE OUT.
    #
    # Look at the sample, [1, 2, 3, 4, 5]. The total of all five is 15.
    #     leave out 1 -> 14
    #     leave out 2 -> 13
    #     leave out 3 -> 12
    #     leave out 4 -> 11
    #     leave out 5 -> 10
    # Every one of those is just (total - the number you left out).
    #
    # Now answer these before you code:
    #   - To make the sum as SMALL as possible, which number do you
    #     leave out?
    #   - To make the sum as LARGE as possible, which number do you
    #     leave out?
    #
    # ---------------------------------------------------------------
    # STEP 1 - Get the total of all five numbers
    # ---------------------------------------------------------------
    # Tool you need: Python has a built-in function that adds up
    # everything in a list. Store the result in a variable.
    #
    # ---------------------------------------------------------------
    # STEP 2 - Find the smallest and largest number in the array
    # ---------------------------------------------------------------
    # Tools you need: Python has a built-in function for each of these.
    # Each takes a list and gives back a single value.
    #
    # ---------------------------------------------------------------
    # STEP 3 - Compute the two answers
    # ---------------------------------------------------------------
    # Use the "total minus the one you left out" idea twice, once for
    # the minimum sum and once for the maximum sum.
    #
    # Careful: this is the step where people swap them. Re-read your
    # answers to the two questions above, then check against the
    # sample, which must give 10 and 14.
    #
    # ---------------------------------------------------------------
    # STEP 4 - Print both on ONE line, separated by a space
    # ---------------------------------------------------------------
    # Minimum first, then maximum.
    # In Staircase, print() putting a space between its arguments was
    # a trap. Here that same behaviour is exactly what you want.
    #
    # ---------------------------------------------------------------
    # ABOUT THE "INTEGER OVERFLOW" WARNING
    # ---------------------------------------------------------------
    # Each number can be up to 10^9, so four of them can reach 4 * 10^9.
    # That is bigger than a 32-bit integer can hold (about 2.1 * 10^9),
    # which is why C, C++ and Java need a `long`.
    # Python integers grow as large as they need to, so you don't have
    # to do anything about it. It is still worth knowing WHY the
    # warning exists, because it will matter in other languages.
    #
    # ---------------------------------------------------------------
    # EDGE CASE TO THINK ABOUT
    # ---------------------------------------------------------------
    # What if all five numbers are the same, e.g. [5, 5, 5, 5, 5]?
    # Work out by hand what the output should be, then check that your
    # code agrees.
    #
    # To test locally, run the file and type: 1 2 3 4 5
    #
    # ---------------------------------------------------------------
    # AFTER IT PASSES (stretch thinking, optional)
    # ---------------------------------------------------------------
    #   - Another route: sort the array first. After sorting, which
    #     four positions make up the minimum sum, and which four make
    #     up the maximum? Solve it again using slicing.
    #   - Your first version walks the array three times (total,
    #     smallest, largest). Could you get all three in a single
    #     `for` loop, without the built-ins? This is the version an
    #     interviewer would ask you for.

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
