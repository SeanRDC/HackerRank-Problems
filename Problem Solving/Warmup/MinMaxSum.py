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

# ===================================================================
# PRACTICE LADDER - 7 small problems that build up to miniMaxSum
# ===================================================================
# Solve them in order. Each one adds exactly ONE new idea.
# Write each as its own small function and compare against the
# sample output before moving on.
#
# ---------------------------------------------------------------
# PROBLEM 1 - Add them up
# ---------------------------------------------------------------
# Print the total of all the numbers WITHOUT using sum().
# New idea: an accumulator. Like the counter from PlusMinus, but it
# grows by the number itself instead of by 1.
#
#   Input:  [1, 2, 3, 4, 5]
#   Output: 15
#
#   Input:  [7]
#   Output: 7
def add(arr):
    total = 0
    for i in arr:
        total += i
    return total
print(add([1, 2, 3, 4, 5]))
print(add([7]))

# ---------------------------------------------------------------
# PROBLEM 2 - Smallest so far
# ---------------------------------------------------------------
# Print the smallest number WITHOUT using min() or sorting.
# New idea: a "best so far" variable that gets REPLACED, not added to,
# whenever the loop meets a better candidate.
# Think hard about what it should start at. The second sample will
# catch the most common wrong choice.
#
#   Input:  [3, 1, 4, 1, 5]
#   Output: 1
#
#   Input:  [8, 6, 9]
#   Output: 6
def smallest(arr):
    smallest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    return smallest

print(smallest([3, 1, 4, 1, 5]))
print(smallest([8, 6, 9]))
# ---------------------------------------------------------------
# PROBLEM 3 - Largest so far
# ---------------------------------------------------------------
# Print the largest number WITHOUT using max() or sorting.
# New idea: the same pattern with the comparison flipped.
# The second sample checks your starting value again.
#
#   Input:  [3, 1, 4, 1, 5]
#   Output: 5
#
#   Input:  [-2, -8, -5]
#   Output: -2
def largest(arr):
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    return largest

print(largest([3, 1, 4, 1, 5]))
print(largest([-2, -8, -5]))
# ---------------------------------------------------------------
# PROBLEM 4 - Three trackers, one loop
# ---------------------------------------------------------------
# Print the total, the smallest, and the largest, one per line,
# walking the list only ONCE.
# New idea: problems 1, 2 and 3 living inside the same `for` loop.
#
#   Input:  [3, 1, 4, 1, 5]
#   Output: 14
#           1
#           5
#
#   Input:  [-2, -8, -5]
#   Output: -15
#           -8
#           -2
def three_trackers(arr):
    total = 0
    small = arr[0]
    large = arr[0]
    for i in arr:
        total += i
        if i < small:
            small = i
        if i > large:
            large = i
    return f'{total}\n{small}\n{large}'

print(three_trackers([3, 1, 4, 1, 5]))
print(three_trackers([-2, -8, -5]))

# ---------------------------------------------------------------
# PROBLEM 5 - Leave one out
# ---------------------------------------------------------------
# For each number in the list, print the sum of all the OTHER numbers,
# one per line.
# New idea: you do not need a loop inside a loop. If you already know
# the total, the sum of "everything except this one" is one subtraction.
#
#   Input:  [1, 2, 3, 4, 5]
#   Output: 14
#           13
#           12
#           11
#           10
#
#   Input:  [5, 5, 5]
#   Output: 10
#           10
#           10
def leave_one_out(arr):
    total = 0
    for i in arr:
        total += i
    for j in arr:
        print(total - j)

leave_one_out([1, 2, 3, 4, 5])
leave_one_out([5, 5, 5])
# ---------------------------------------------------------------
# PROBLEM 6 - Two values, one line
# ---------------------------------------------------------------
# Given a and b, print both on the SAME line with one space between.
# New idea: what print() does when you hand it more than one argument.
#
#   Input:  10, 14
#   Output: 10 14
#
#   Input:  20, 20
#   Output: 20 20
a, b = 10, 14
print(f'{a} {b}')

a, b = 20, 20
print(f'{a} {b}')

# ---------------------------------------------------------------
# PROBLEM 7 - Mini-Max Sum (the real thing, solve it below)
# ---------------------------------------------------------------
# Given five positive integers, find the minimum and maximum values
# you can get by summing exactly FOUR of the five. Print the minimum
# then the maximum on one line, separated by a space.
# Look at the output of problem 5 on [1, 2, 3, 4, 5] before you start:
# both answers are already in that list. Which number was left out to
# produce each one?
#
#   Input:  [1, 2, 3, 4, 5]
#   Output: 10 14
#
#   Input:  [5, 5, 5, 5, 5]
#   Output: 20 20
#
#   Input:  [7, 69, 2, 221, 8974]
#   Output: 299 9271
#

def miniMaxSum(arr):
    # Write your code here
    
    # Get the total of the array
    total = 0
    for i in arr:
        total += i
    # Leave one out and append to new list
    new_arr = []
    for j in arr:
        new_arr.append(total - j)
    
    # Get the largest and smallest
    large = new_arr[0]
    small = new_arr[0]
    
    for k in new_arr:
        if k < small:
            small = k
        if k > large:
            large = k
    print(f'{small} {large}')


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
