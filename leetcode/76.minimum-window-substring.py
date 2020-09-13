#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
from common import BaseTestCase, unittest
from typing import List

# 
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
# @lc code=end
class P76TestCase(BaseTestCase):
    def test_1(self):
        s = 'ADOBECODEBANC'
        t = 'ABC'
        expected = 'BANC'
        actual = Solution().minWindow(s, t)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = 'a'
        t = 'a'
        expected = 'a'
        actual = Solution().minWindow(s, t)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = 'a'
        t = 'aa'
        actual = Solution().minWindow(s, t)
        self.assertEqual(0, len(actual))


if __name__ == '__main__':
    unittest.main()