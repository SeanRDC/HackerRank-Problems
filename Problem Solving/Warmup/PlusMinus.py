#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    #
    # ---------------------------------------------------------------
    # THE IDEA
    # ---------------------------------------------------------------
    # A "ratio" here is just:  (how many of one kind) / (how many total).
    # So the whole problem is really two smaller problems:
    #   1. COUNT how many numbers are positive, negative, and zero.
    #   2. DIVIDE each count by the size of the array, then print it
    #      with exactly 6 digits after the decimal point.
    #
    # Check yourself with the sample: [-4, 3, -9, 0, 4, 1]
    #   positives = 3, negatives = 2, zeros = 1, total = 6
    #   3/6 = 0.500000, 2/6 = 0.333333, 1/6 = 0.166667
    #
    # ---------------------------------------------------------------
    # STEP 1 - Set up your counters
    # ---------------------------------------------------------------
    # You need three variables to keep score, one per category.
    # Think: what value should a counter have before you've looked
    # at any number yet?
    #
    
    # ---------------------------------------------------------------
    # STEP 2 - Walk through the array and classify each number
    # ---------------------------------------------------------------
    # Tools you need: a `for` loop over arr, and an `if / elif / else` chain.
    # For each number, ask: is it greater than 0? less than 0? or neither?
    # Whichever branch matches, add 1 to that category's counter.
    #
    # Things to think about:
    #   - Every number lands in exactly ONE of the three categories.
    #     That's why if/elif/else fits better than three separate `if`s.
    #   - If it is not positive and not negative, what must it be?
    #     Do you even need to write a condition for that last case?
    #
    # ---------------------------------------------------------------
    # STEP 3 - Turn counts into ratios
    # ---------------------------------------------------------------
    # Tools you need: len() to get the total, and the division operator.
    # Python has TWO division operators: `/` and `//`.
    # One gives a decimal result, the other throws the decimal part away.
    # Which one do you want here? (Try 3 / 6 and 3 // 6 in a terminal.)
    #
    # ---------------------------------------------------------------
    # STEP 4 - Print with exactly 6 decimal places
    # ---------------------------------------------------------------
    # This is the "precision" part the problem warns about.
    # A plain print() of 0.5 shows `0.5`, but the judge expects `0.500000`.
    # And 1/6 would print far more than 6 digits.
    #
    # Tool you need: a "format specifier" for fixed-point floats.
    # Look up either of these (they do the same job):
    #   - f-strings with a format spec  -> search "python f-string decimal places"
    #   - the built-in format() function
    # The piece you are hunting for is the part that says
    # "float, with N digits after the point".
    #
    # Why not round()? Try round(0.5, 6) and see what it prints.
    # round() changes the VALUE; formatting changes how it is DISPLAYED.
    # Trailing zeros only exist in the display.
    #
    # ORDER MATTERS: print positive first, then negative, then zero,
    # each on its own line.
    #
    # ---------------------------------------------------------------
    # REMINDER
    # ---------------------------------------------------------------
    # The function PRINTS its results. It does not return anything.
    #
    # ---------------------------------------------------------------
    # AFTER IT PASSES (stretch thinking, optional)
    # ---------------------------------------------------------------
    #   - How many times does your code look at each element? (That is
    #     its time complexity. One pass is the best you can do here.)
    #   - You wrote nearly the same print line three times. Could a
    #     loop over your three counts remove that repetition?

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
