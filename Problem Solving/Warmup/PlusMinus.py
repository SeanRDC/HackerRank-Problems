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

# ===================================================================
# PRACTICE LADDER - 10 small problems that build up to plusMinus
# ===================================================================
# Solve them in order. Each one adds exactly ONE new idea.
# Write each as its own small function and compare against the
# sample output before moving on.
#
# ---------------------------------------------------------------
# PROBLEM 1 - Count everything
# ---------------------------------------------------------------
# Print how many numbers are in the list WITHOUT using len().
# New idea: a counter that starts at 0 and grows inside a `for` loop.
#
#   Input:  [7, -2, 0, 5]
#   Output: 4
#
#   Input:  [10]
#   Output: 1

def count_all(arr):
    elements = 0
    for _ in arr:
        elements += 1
    return elements

print(count_all([7, -2, 0, 5]))

# ---------------------------------------------------------------
# PROBLEM 2 - Count only some
# ---------------------------------------------------------------
# Print how many numbers are positive.
# New idea: an `if` inside the loop, so the counter only grows sometimes.
#
#   Input:  [-4, 3, -9, 0, 4, 1]
#   Output: 3
#
#   Input:  [-1, 0, -5]
#   Output: 0
def count_positive(arr):
    total = 0
    for i in arr:
        if i > 0:
            total += 1
    return total

print(count_positive([-4, 3, -9, 0, 4, 1]))
print(count_positive([-1, 0, -5]))

# ---------------------------------------------------------------
# PROBLEM 3 - Classify one number
# ---------------------------------------------------------------
# Given a single integer, print "positive", "negative", or "zero".
# New idea: if / elif / else, where exactly one branch runs.
#
#   Input:  5
#   Output: positive
#
#   Input:  -3
#   Output: negative
#
#   Input:  0
#   Output: zero

def classifier(num):
    if num == 0:
        return 'zero'
    elif num > 0:
        return 'positive'
    else:
        return 'negative'

print(classifier(5))
print(classifier(-3))
print(classifier(0))

# ---------------------------------------------------------------
# PROBLEM 4 - Two counters
# ---------------------------------------------------------------
# Print how many are positive, then how many are NOT positive.
# New idea: if / else feeding two counters.
# Check: the two outputs should add up to the length of the list.
#
#   Input:  [-4, 3, -9, 0, 4, 1]
#   Output: 3
#           3
#
#   Input:  [2, 8, 0]
#   Output: 2
#           1

def two_counters(arr):
    positive = 0
    negative = 0
    for i in arr:
        if i > 0:
            positive += 1
        else:
            negative += 1
    return f'{positive}\n{negative}'

print(two_counters([-4, 3, -9, 0, 4, 1]))
print(two_counters([2, 8, 0]))
# ---------------------------------------------------------------
# PROBLEM 5 - Three counters
# ---------------------------------------------------------------
# Print the count of positives, negatives, and zeros, one per line.
# New idea: problems 3 and 4 combined. This is half of plusMinus.
#
#   Input:  [-4, 3, -9, 0, 4, 1]
#   Output: 3
#           2
#           1
#
#   Input:  [0, 0, -7]
#   Output: 0
#           1
#           2
def three_counters(arr):
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    return f'{positive}\n{negative}\n{zero}'

print(three_counters([-4, 3, -9, 0, 4, 1]))
print(three_counters([0, 0, -7]))

# ---------------------------------------------------------------
# PROBLEM 6 - Two kinds of division
# ---------------------------------------------------------------
# Given a and b, print a / b and then a // b.
# New idea: which operator keeps the decimal part.
#
#   Input:  3, 6
#   Output: 0.5
#           0
#
#   Input:  7, 2
#   Output: 3.5
#           3
def two_divisions(a, b):
    return f'{a/b}\n{a//b}'

print(two_divisions(3, 6))
print(two_divisions(7, 2))

# ---------------------------------------------------------------
# PROBLEM 7 - Fixed decimal places
# ---------------------------------------------------------------
# Given a and b, print a / b with exactly 6 digits after the point.
# New idea: a format specifier.
# Try round() first and see why it fails on the first sample.
#
#   Input:  1, 2
#   Output: 0.500000
#
#   Input:  1, 6
#   Output: 0.166667
#
#   Input:  2, 3
#   Output: 0.666667
def fix_decimal(a,b):
    return f'{a/b:.6f}'

print(fix_decimal(1, 2))
print(fix_decimal(1, 6))
print(fix_decimal(2, 3))

# ---------------------------------------------------------------
# PROBLEM 8 - One ratio
# ---------------------------------------------------------------
# Print the fraction of the list that is positive, to 6 decimal places.
# New idea: count (problem 2) + divide (6) + format (7) in one function.
#
#   Input:  [-4, 3, -9, 0, 4, 1]
#   Output: 0.500000
#
#   Input:  [1, 2, 3]
#   Output: 1.000000
#
#   Input:  [-1, -2]
#   Output: 0.000000
def one_ratio(arr):
    positive = 0
    for i in arr:
        if i > 0:
            positive += 1
    return f'{positive/len(arr):.6f}'

print(one_ratio([-4, 3, -9, 0, 4, 1]))
print(one_ratio([1, 2, 3]))
print(one_ratio([-1, -2]))

# ---------------------------------------------------------------
# PROBLEM 9 - Same shape, different question
# ---------------------------------------------------------------
# Print the fraction of EVEN numbers, then the fraction of ODD numbers,
# each to 3 decimal places.
# New idea: nothing new, and that is the point. If you can change the
# categories and the precision without looking back, you own the pattern.
#
#   Input:  [1, 2, 3, 4, 6]
#   Output: 0.600
#           0.400
#
#   Input:  [5, 7, 9]
#   Output: 0.000
#           1.000
def odd_even(arr):
    even = 0
    odd = 0
    for i in arr:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return f'{even/len(arr):.3f}\n{odd/len(arr):.3f}'

print(odd_even([1, 2, 3, 4, 6]))
print(odd_even([5, 7, 9]))

# ---------------------------------------------------------------
# PROBLEM 10 - Plus Minus (the real thing, solve it below)
# ---------------------------------------------------------------
# Print the ratio of positives, negatives, and zeros, in that order,
# each on its own line, to 6 decimal places.
#
#   Input:  [-4, 3, -9, 0, 4, 1]
#   Output: 0.500000
#           0.333333
#           0.166667
#
#   Input:  [1, 1, 0, -1, -1]
#   Output: 0.400000
#           0.400000
#           0.200000
#
#   Input:  [0]
#   Output: 0.000000
#           0.000000
#           1.000000
#

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    # Count the positives, negatives, and zeroes
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    # divide them to the total array, and return in 6 decimal places
    print(f'{positive/len(arr):.6f}\n{negative/len(arr):.6f}\n{zero/len(arr):.6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
