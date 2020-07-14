#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
from typing import List
from common import BaseTestCase
import unittest


# @lc code=start
class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = nums[0] + nums[1] + nums[2]
        min_diff = abs(target - ans)

        for i in range(len(nums) - 2):
            t = target - nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                diff = abs(t - s)
                if diff < min_diff:
                    ans = nums[i] + s
                    min_diff = diff
                    
                if s > t:
                    r -= 1
                elif s < t:
                    l += 1
                else:
                    return nums[i] + s
        return ans


# @lc code=end
class P16TestCase(BaseTestCase):

    def test1(self):
        nums = [-1, 2, 1, -4]
        expected = 2
        actual = Solution().threeSumClosest(nums, target=1)
        self.assertEqual(expected, actual)

    def test1(self):
        nums = [0, 0, 0]
        expected = 0
        actual = Solution().threeSumClosest(nums, target=1)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
