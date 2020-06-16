# https://www.hackerrank.com/test/ch1k00qp1cn/questions/6k7inol89sa

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    # Write your code here
    n = len(grid)
    m = len(grid[0])
    check = [[1] * (m + 2) for _ in range(n + 2)]

    grid2 = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            grid2[i][j] = grid[i - 1][j - 1]

    ans = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            curr = grid2[i][j]
            check[i][j + 1] = grid2[i][j + 1] - curr
            check[i + 1][j - 1] = grid2[i + 1][j - 1] - curr
            check[i + 1][j] = grid2[i + 1][j] - curr
            check[i + 1][j + 1] = grid2[i + 1][j + 1] - curr

            check[i][j] = min(
                check[i][j],
                -1 * check[i][j + 1], -1 * check[i + 1][j - 1],
                -1 * check[i + 1][j], -1 * check[i + 1][j + 1]
            )
            if check[i][j] > 0:
                ans += 1
    return ans


def main():
    grid = [[1, 2, 2, 1]]
    print(numCells(grid))


if __name__ == '__main__':
    main()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # grid_rows = int(input().strip())
    # grid_columns = int(input().strip())
    #
    # grid = []
    #
    # for _ in range(grid_rows):
    #     grid.append(list(map(int, input().rstrip().split())))
    #
    # result = numCells(grid)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
