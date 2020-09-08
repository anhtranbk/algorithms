#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
from typing import List
import unittest
from common import BaseTestCase

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1]*n for _ in range(m)]
        dp[0][0] = obstacleGrid[0][0] - 1
        dp[-1][-1] = 1 - obstacleGrid[-1][-1]

        def move(i: int, j: int) -> int:
            if dp[i][j] != -1:
                return dp[i][j]
            
            mvd, mvr = 0, 0
            if i+1 != m and obstacleGrid[i+1][j] != 1:
                mvd = move(i+1, j)
            if j+1 != n and obstacleGrid[i][j+1] != 1:
                mvr = move(i, j+1)

            dp[i][j] = mvd + mvr
            return dp[i][j]
        
        move(0, 0)
        return dp[0][0]
        
# @lc code=end

