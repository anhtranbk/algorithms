#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
from common import BaseTestCase, unittest
from typing import List

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.solution_1(matrix)

    # O(1) space
    def solution_1(self, matrix: List[List[int]]) -> List[int]:
        m, n, ans = len(matrix), len(matrix[0]), [matrix[0][0]]
       
        top, bottom, left, right = 0, m, -1, n
        l, i, j = m*n, 0, 0
        while len(ans) < l:
            for j in range(j+1, right):
                ans.append(matrix[i][j])

            if len(ans) < l:
                for i in range(i+1, bottom):
                    ans.append(matrix[i][j])
            
            if len(ans) < l:
                for j in range(j-1, left, -1):
                    ans.append(matrix[i][j])
            
            if len(ans) < l:
                for i in range(i-1, top, -1):
                    ans.append(matrix[i][j])

            top, bottom, left, right = top+1, bottom-1, left+1, right-1

        return ans
    
    # O(n^2) space
    def solution_2(self, matrix: List[List[int]]) -> List[int]:
        m, n, ans = len(matrix), len(matrix[0]), [matrix[0][0]]
        masks = [[0,1], [1,0], [0,-1], [-1,0]]
        flags = [[0]*n for _ in range(m)]
        flags[0][0] = 1

        l, i, j = m*n, 0, 0
        while len(ans) < l:
            for mask in masks:
                while True:
                    u, v = i+mask[0], j+mask[1]
                    if u < m and v < n and flags[u][v] == 0:
                        flags[u][v] = 1
                        ans.append(matrix[u][v])
                        i, j = u, v
                    else:
                        break
        return ans

# @lc code=end
class P54TestCase(BaseTestCase):
    def test_1(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        expected = [1,2,3,6,9,8,7,4,5]
        actual = Solution().spiralOrder(matrix)
        self.assertArrayEquals(expected, actual, sorted_before_comparing=False)

    def test_2(self):
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        expected = [1,2,3,4,8,12,11,10,9,5,6,7]
        actual = Solution().spiralOrder(matrix)
        self.assertArrayEquals(expected, actual, sorted_before_comparing=False)

        
if __name__ == "__main__":
    unittest.main()