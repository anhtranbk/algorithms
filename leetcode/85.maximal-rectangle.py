#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
from typing import List

from common import BaseTestCase, unittest


# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dpx = [[0] * (n + 1) for _ in range(m + 1)]
        dpy = [[0] * (n + 1) for _ in range(m + 1)]

        ma = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    continue
                dpx[i + 1][j + 1] = dpx[i + 1][j] + 1
                dpy[i + 1][j + 1] = dpy[i][j + 1] + 1
                ma = max(ma, dpx[i + 1][j + 1] * dpy[i + 1][j + 1])
                # print(i, j, dpx[i + 1][j + 1], dpy[i + 1][j + 1])

        return ma


# @lc code=end
class P85TestCase(BaseTestCase):
    def test_1(self):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
        self.assertEqual(6, Solution().maximalRectangle(matrix))

    def test_2(self):
        matrix = [["0"]]
        self.assertEqual(0, Solution().maximalRectangle(matrix))

    def test_3(self):
        matrix = [["1"]]
        self.assertEqual(1, Solution().maximalRectangle(matrix))


if __name__ == "__main__":
    unittest.main()
