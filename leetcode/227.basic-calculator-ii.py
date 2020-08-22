#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
from common import BaseTestCase, unittest

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        
        
# @lc code=end
class P227TestCase(BaseTestCase):
    def test(self):
        exp = "2 + 3 - 7 / 2*9+1-10*3+2/2*4-4+3"
        expected = eval(exp)
        actual = Solution().calculate(exp)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()