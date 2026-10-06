#!/bin/python3
# aVeryBigSum returns the sum of the array with the built-in sum, relying on Python
# integers to hold values larger than 32 bits.

import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)
