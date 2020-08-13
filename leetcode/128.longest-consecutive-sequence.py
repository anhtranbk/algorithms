#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
from typing import List, Dict
from common import BaseTestCase, unittest

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pass
                

# @lc code=end
class P128TestCase(BaseTestCase):
    def test_1(self):
        nums = [100,4,200,1,3,2]
        actual = Solution().longestConsecutive(nums)
        self.assertEqual(4, actual)
        
    def test_2(self):
        nums = [0,3,7,2,5,8,4,6,0,1]
        actual = Solution().longestConsecutive(nums)
        self.assertEqual(9, actual)

        
if __name__ == "__main__":
    unittest.main()

