#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
from typing import List
from common import unittest, BaseTestCase

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if self.backtracking(board, word, visited, i, j, 0):
                    return True 

        return False
        
    def backtracking(self, 
                     board: List[List[str]], 
                     word: str,
                     visited: List[List[int]],
                     i: int,
                     j: int,
                     k: int) -> bool:
                    
        if i < 0 or i == len(board):
            return False
        
        if j < 0 or j == len(board[0]):
            return False 
        
        if visited[i][j] == 1:
            return False

        if k == len(word)-1:
            return board[i][j] == word[k] 

        if board[i][j] != word[k]:
            return False


        visited[i][j] = 1

        if self.backtracking(board, word, visited, i-1, j, k+1):
            return True
        
        if self.backtracking(board, word, visited, i+1, j, k+1):
            return True
         
        if self.backtracking(board, word, visited, i, j-1, k+1):
            return True
                 
        if self.backtracking(board, word, visited, i, j+1, k+1):
            return True

        visited[i][j] = 0
                        
        
# @lc code=end
class P79TestCase(BaseTestCase):
    def test_1(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        self.assertTrue(Solution().exist(board, word))

    def test_2(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "SEE"
        self.assertTrue(Solution().exist(board, word))

    def test_3(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCB"
        self.assertFalse(Solution().exist(board, word))


if __name__ == "__main__":
    unittest.main()