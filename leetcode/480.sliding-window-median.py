#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#

# @lc code=start
from typing import List
from common import BaseTestCase, unittest


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # using two sorted sets (OnlogK)
        # using two priority queues (Onk)
        # is there any better approach ? 
        pass

        
# @lc code=end
class P480TestCase(BaseTestCase):
    def test_1(self):
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3
        expected = [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
        actual = Solution().medianSlidingWindow(nums, k)
        self.assertEqual(actual, expected)

    def test_2(self):
        nums = [1,2,3,4,2,3,1,4,2]
        k = 3
        expected = [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
        actual = Solution().medianSlidingWindow(nums, k)
        self.assertEqual(actual, expected)
    
    
if __name__ == "__main__":
    unittest.main()
