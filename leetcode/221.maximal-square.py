#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
from typing import List

from common import BaseTestCase, unittest


# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # only need to keep dp for the current and prev rows
        curr_dp = [0] * (n + 1)

        mv = 0
        for i in range(0, m):
            prev_dp = curr_dp.copy()
            curr_dp = [0] * (n + 1)
            for j in range(0, n):
                if int(matrix[i][j]) == 0:
                    continue
                curr_dp[j + 1] = min(prev_dp[j], prev_dp[j + 1], curr_dp[j]) + 1
                mv = max(mv, curr_dp[j + 1])

        return mv * mv


# @lc code=end
class P221TestCase(BaseTestCase):
    def test_1(self):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
        self.assertEqual(4, Solution().maximalSquare(matrix))

    def test_2(self):
        matrix = [["0", "1"], ["1", "0"]]
        self.assertEqual(1, Solution().maximalSquare(matrix))

    def test_3(self):
        matrix = [["0"]]
        self.assertEqual(0, Solution().maximalSquare(matrix))

    def test_4(self):
        matrix = [
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["0", "0", "0", "0", "0"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
        ]
        self.assertEqual(4, Solution().maximalSquare(matrix))


if __name__ == "__main__":
    unittest.main()
