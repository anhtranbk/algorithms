#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
from typing import List

from common import BaseTestCase, unittest


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        lo, hi = 0, len(matrix) - 1
        while lo < hi:
            m = hi - (hi - lo) // 2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] < target:
                lo = m
            else:
                hi = m - 1
        row = lo
        lo, hi = 0, len(matrix[row]) - 1
        while lo <= hi:
            m = lo + (hi - lo) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                lo = m + 1
            else:
                hi = m - 1
        return False


# @lc code=end
