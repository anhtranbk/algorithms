#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    ans = [0]*len(c)
    res = jump(c, ans, 0)
    print(ans)
    return res
    
def jump(c, ans, i):
    if len(c)-1-i <= 2:
        ans[i] = 1
    elif c[i+1] == 0 and c[i+2] == 0:
        l = jump(c, ans, i+1)
        r = jump(c, ans, i+2)
        ans[i] = 1 + min(l, r)
    elif c[i+1] == 0:
        ans[i] = 1 + jump(c, ans, i+1)
    else:
        ans[i] = 1 + jump(c, ans, i+2)
    return ans[i]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

