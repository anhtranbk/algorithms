#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
from typing import List

from common import BaseTestCase, unittest


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # https://leetcode.com/problems/search-a-2d-matrix-ii/solutions/332356/python-o-m-n-linear-search-from-top-right-corner/
        m, n = len(matrix), len(matrix) and len(matrix[0])
        r, c = 0, n - 1
        while r < m and c >= 0:
            if target > matrix[r][c]:
                r += 1
            elif target < matrix[r][c]:
                c -= 1
            else:
                return True
        return False


# @lc code=end
class P240TestCase(BaseTestCase):
    def test_1(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ]
        target = 5
        self.assertTrue(Solution().searchMatrix(matrix, target))

    def test_2(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ]
        target = 20
        self.assertFalse(Solution().searchMatrix(matrix, target))

    def test_3(self):
        matrix = [[1, 4], [2, 5]]
        target = 5
        self.assertTrue(Solution().searchMatrix(matrix, target))

    def test_4(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ]
        target = 9
        self.assertTrue(Solution().searchMatrix(matrix, target))


if __name__ == "__main__":
    unittest.main()
