#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
from typing import List
import unittest
from common import BaseTestCase

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0]*9
        cols = [0]*9
        boxes = [0]*9

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue

                v = 1 << int(board[i][j])
                
                # validate row
                if rows[i] & v > 0:
                    return False

                # validate column
                if cols[j] & v > 0:
                    return False
                
                # validate 3x3 sub-boxes
                k = (i // 3) * 3 + (j // 3)
                if boxes[k] & v > 0:
                    return False

                rows[i] = rows[i] | v    
                cols[j] = cols[j] | v
                boxes[k] = boxes[k] | v
       
        return True 
        
            
# @lc code=end
class P36(BaseTestCase):
    def test_1(self):
        board = [
            ["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]
        ]
        self.assertTrue(Solution().isValidSudoku(board))
    
    def test_2(self):
        board = [
            ["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]
        ]
        self.assertFalse(Solution().isValidSudoku(board))
    
    
if __name__ == "__main__":
    unittest.main()
