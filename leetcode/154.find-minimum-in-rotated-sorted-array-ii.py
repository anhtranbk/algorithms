#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
from typing import List

from common import BaseTestCase, unittest


# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.doFindMin(nums, 0, len(nums) - 1)

    def doFindMin(self, nums: List[int], lo: int, hi: int) -> int:
        if lo == hi:
            return nums[lo]

        m = lo + (hi - lo) // 2
        if nums[m] > nums[hi]:
            return self.doFindMin(nums, m + 1, hi)
        elif nums[m] < nums[hi]:
            return self.doFindMin(nums, lo, m)
        else:
            left = self.doFindMin(nums, lo, m)
            right = self.doFindMin(nums, m + 1, hi)
            return min(left, right)


# @lc code=end
class P154TestCase(BaseTestCase):
    def test_1(self):
        nums = [3, 4, 5, 1, 2]
        # [3,3,3,3,3,1,3]
        # [3,1,3,3,3,3,3]
        actual = Solution().findMin(nums)
        self.assertEqual(1, actual)

    def test_2(self):
        nums = [3, 1, 3, 3, 3, 3, 3]
        actual = Solution().findMin(nums)
        self.assertEqual(1, actual)

    def test_3(self):
        nums = [3, 3, 3, 3, 3, 1, 3]
        actual = Solution().findMin(nums)
        self.assertEqual(1, actual)

    def test_4(self):
        nums = [1]
        actual = Solution().findMin(nums)
        self.assertEqual(1, actual)

    def test_5(self):
        nums = [2, 2, 2, 0, 1]
        actual = Solution().findMin(nums)
        self.assertEqual(0, actual)


if __name__ == "__main__":
    unittest.main()
