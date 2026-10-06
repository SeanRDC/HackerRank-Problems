#!/bin/python3
# Pairs up the two triplets with zip and awards a point to whichever side has the larger
# value in each position, returning both scores.

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    a_score = 0
    b_score = 0

    for i, j in zip(a, b):
        if i > j:
            a_score += 1
        elif i < j:
            b_score += 1

    return [a_score, b_score]

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)
