#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
import unittest
from common import BaseTestCase
import random

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass

    def twoSum_twoPointers(self, nums: List[int], target: int) -> List[List[int]]:
        lo, hi = 0, len(nums)-1
        nums = sorted(nums)
        ans = []
        while lo < hi:
            t = nums[lo] + nums[hi]
            if t < target:
                lo += 1
            elif t > target:
                hi -= 1
            else:
                ans.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
        return ans

class P1TestCase(BaseTestCase):
    def test1(self):
        nums = [random.randint(1, 100) for _ in range(100)]
        ans = Solution().twoSum_twoPointers(nums, target=100)
        print(ans)
        
# @lc code=end
if __name__ == '__main__':
    unittest.main()
