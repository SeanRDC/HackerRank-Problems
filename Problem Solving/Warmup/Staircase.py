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

def staircase(n):
    # Write your code here
    #
    # ---------------------------------------------------------------
    # THE IDEA
    # ---------------------------------------------------------------
    # Don't think of this as "drawing a shape". Think of it as printing
    # n lines of text, where every line is built from two pieces:
    #
    #     [ some spaces ][ some # symbols ]
    #
    # The whole problem is working out HOW MANY of each go on each line.
    #
    # ---------------------------------------------------------------
    # STEP 1 - Find the pattern on paper first (do this before coding)
    # ---------------------------------------------------------------
    # Fill in this table for n = 4. The first row is done for you:
    #
    #     row | spaces | hashes | spaces + hashes
    #     ----+--------+--------+----------------
    #      1  |   3    |   1    |       4
    #      2  |   ?    |   ?    |       ?
    #      3  |   ?    |   ?    |       ?
    #      4  |   ?    |   ?    |       ?
    #
    # Now answer these:
    #   - How does the number of hashes relate to the row number?
    #   - What does the last column always equal?
    #   - So if you know the hashes, how do you get the spaces
    #     using only n and the row number?
    #
    # Once you can write both counts as a small formula in terms of
    # n and the row number, the coding part is short.
    #
    # ---------------------------------------------------------------
    # STEP 2 - Loop once per row
    # ---------------------------------------------------------------
    # Tools you need: a `for` loop with range().
    #
    # Watch out: range(n) starts counting at 0, not 1. Your table above
    # starts at row 1. You have two ways to deal with that:
    #   - give range() a start and a stop so it counts 1..n, or
    #   - keep it starting at 0 and adjust your formulas by one.
    # Either works. Pick one and be consistent. Also remember the stop
    # value of range() is NOT included.
    #
    # ---------------------------------------------------------------
    # STEP 3 - Build one line
    # ---------------------------------------------------------------
    # Tool you need: string repetition. In Python you can MULTIPLY a
    # string by an integer. Try this in a terminal and see what happens:
    #     "ab" * 3
    # Use that idea twice (once for the spaces, once for the hashes),
    # then join the two pieces with string concatenation.
    #
    # ---------------------------------------------------------------
    # STEP 4 - Print it
    # ---------------------------------------------------------------
    # print() already ends each call with a newline, so one print per
    # row gives you one line per row. Nothing extra needed.
    #
    # ---------------------------------------------------------------
    # COMMON MISTAKES
    # ---------------------------------------------------------------
    #   - Off by one: the first row has 1 hash, not 0. The last row has
    #     n hashes and 0 spaces. Test your formulas on both of those rows.
    #   - Spaces on the wrong side: they go BEFORE the hashes. Nothing
    #     comes after the hashes.
    #   - Passing the two pieces to print() as separate arguments: print
    #     puts a space between its arguments, which would shift your stairs.
    #
    # To test locally, run the file and type a number such as 6.
    #
    # ---------------------------------------------------------------
    # AFTER IT PASSES (stretch thinking, optional)
    # ---------------------------------------------------------------
    #   - Python strings have a built-in method that right-aligns text
    #     to a given width, which replaces the manual spaces entirely.
    #     Search "python string right justify" and try a second version.
    #   - Could you solve it with nested loops and no string
    #     multiplication? It's longer, but it shows what the `*` is
    #     doing for you underneath.

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
