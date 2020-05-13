#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
from typing import List

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [None]*n 
        for i in range(0, n):
            board[i] = [0]*n 
        
        ans = []

        def isValid(row: int, col: int):
            for i in range(0, row):
                if board[i][col] == 1:
                    return False
            
            for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if board[i][j] == 1:
                    return False

            for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
                if board[i][j] == 1:
                    return False

            return True

        def backtracking(i: int):
            if i == n:
                # Must use x as an array because if x is an integer, the reference 
                # to x here will create a new local/internal function-scoped variable 
                # named x instead of the external x variable we declared above
                ans.append(1)
                return

            for j in range(0, n):
                if not isValid(i, j):
                    continue

                board[i][j] = 1
                backtracking(i+1)
                board[i][j] = 0

        backtracking(0)
        return len(ans)


if __name__ == '__main__':
    ans = Solution().totalNQueens(n=4)
    print(ans)
        
# @lc code=end

