#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from typing import List

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    self.pathFinding(grid, i, j)
        return ans

    def pathFinding(self, grid: List[List[str]], i: int, j: int):
        if i < 0 or i == len(grid):
            return
        if j < 0 or j == len(grid[0]):
            return

        if grid[i][j] == '1':
            grid[i][j] = '2'
            self.pathFinding(grid, i+1, j)
            self.pathFinding(grid, i-1, j)
            self.pathFinding(grid, i, j+1)
            self.pathFinding(grid, i, j-1)
        elif grid[i][j] == '0':
            grid[i][j] = '2'
        
# @lc code=end
if __name__ == '__main__':
    grid = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            grid[i][j] = str(grid[i][j])
    ans = Solution().numIslands(grid)
    print(ans)
