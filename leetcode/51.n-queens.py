#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
from typing import List

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [None]*n
        for i in range(0, n):
            board[i] = ['.']*n 
        
        return self.solve_recursion(n, board)

    def solve_recursion(self, n: int, board: List[List[str]]) -> List[List[str]]:
        ans = []

        def backtracking(i: int):
            if i == n:
                ans.append([''.join(e) for e in board])
                return

            for j in range(0, n):
                if not self.isValid(board, n, i, j): 
                    continue

                board[i][j] = 'Q'
                backtracking(i+1)
                board[i][j] = '.'

        backtracking(0)
        return ans

    def solve_nonRecursion(self, n: int, board: List[List[str]]) -> List[List[str]]:
        ans, st = [], [0]
        while st:
            i = st.pop()
            if i == n:
                ans.append([''.join(e) for e in board])
                continue

            for j in range(0, n):
                if not self.isValid(board, n, i, j):
                    continue

                board[i][j] = 'Q'
                st.append(i+1)
                # TODO: How to avoid non recursion here ?

    def isValid(self, board: List[List[str]], n: int, row: int, col: int) -> bool:
        for i in range(0, row):
            if board[i][col] == 'Q':
                return False
        
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False

        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i][j] == 'Q':
                return False

        return True


# if __name__ == '__main__':
#     ans = Solution().solveNQueens(n=4)
#     print(ans)
        
# @lc code=end

