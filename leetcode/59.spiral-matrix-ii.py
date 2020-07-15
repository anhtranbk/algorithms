#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
from typing import List
from common import BaseTestCase
import unittest

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        ans[0][0] = 1

        i, j, is_row, t, cnt = 0, 0, True, 1, 1
        while cnt < n*n:
            if is_row:
                v = j + t
                if v < 0 or v == n or ans[i][v] != 0:
                    is_row = False
                    i += t
                else:
                    j = v
            else:
                v = i + t
                if v < 0 or v == n or ans[v][j] != 0:
                    is_row = True
                    t *= -1
                    j += t
                else:
                    i = v

            cnt += 1
            ans[i][j] = cnt

        return ans
        
# @lc code=end
class P59TestCase(BaseTestCase):
    def test1(self):
        expected = [[1,2,3], [8,9,4], [7,6,5]]
        actual = Solution().generateMatrix(n=3)

        print(actual)
        for i in range(3):
            self.assertArrayEquals(expected[i], actual[i])


if __name__ == '__main__':
    unittest.main()
