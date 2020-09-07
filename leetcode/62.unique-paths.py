#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
import unittest
from common import BaseTestCase

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        dp[m-1][n-1] = 1

        def move(i: int, j: int):
            if dp[i][j] != -1:
                return dp[i][j]

            mvr = 0 if j == n-1 else move(i, j+1)
            mvd = 0 if i == m-1 else move(i+1, j)
            dp[i][j] = mvr + mvd

            return dp[i][j] 

        move(0, 0)

        return dp[0][0]
        

# @lc code=end
class P62TestCase(BaseTestCase):
    def test_1(self):
        ans = Solution().uniquePaths(3, 7)
        self.assertEqual(28, ans)

    def test_2(self):
        ans = Solution().uniquePaths(3, 2)
        self.assertEqual(3, ans)


if __name__ == '__main__':
    unittest.main()
