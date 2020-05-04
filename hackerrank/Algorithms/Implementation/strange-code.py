#!/bin/python3
# https://www.hackerrank.com/challenges/strange-code/problem

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    c, i = 0, 0
    while c < t:
        c += 3 << i
        i += 1
    return c - t + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()

