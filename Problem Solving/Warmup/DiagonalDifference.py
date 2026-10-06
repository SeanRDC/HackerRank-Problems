#!/bin/python3
# Sums the primary diagonal (arr[i][i]) and the secondary diagonal (arr[i][n - 1 - i])
# in one loop and returns the absolute difference between them.

import math
import os
import random
import re
import sys
import numpy as np

def diagonalDifference(arr):
    n = len(arr)
    primary_sum = 0
    secondary_sum = 0

    for i in range(n):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][n - 1 - i]

    return abs(primary_sum - secondary_sum)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
