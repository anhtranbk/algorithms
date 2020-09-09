#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
from typing import List
import unittest
from common import BaseTestCase

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        dp[-1][-1] = grid[-1][-1]

        def move(i: int, j: int) -> int:
            if dp[i][j] != -1:
                return dp[i][j]

            mvd = 20001 if i+1 == m else move(i+1, j)
            mvr = 20001 if j+1 == n else move(i, j+1)

            dp[i][j] = grid[i][j] + min(mvd, mvr)
            return dp[i][j]

        return move(0, 0) 
        
# @lc code=end
class P64TestCase(BaseTestCase):
    def test_1(self):
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        ans = Solution().minPathSum(grid)
        self.assertEqual(7, ans)

    def test_2(self):
        grid = [[1,2,3],[4,5,6]]
        ans = Solution().minPathSum(grid)
        self.assertEqual(12, ans)


if __name__ == "__main__":
    unittest.main()
