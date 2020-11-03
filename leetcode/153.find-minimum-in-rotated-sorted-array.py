#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
from typing import List

from common import BaseTestCase, unittest


# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while hi - lo > 1:
            m = lo + (hi - lo) // 2
            if nums[m] > nums[hi]:
                lo = m
            else:
                hi = m
        ans = hi if nums[lo] > nums[hi] else lo
        return nums[ans]


# @lc code=end
class P153TestCase(BaseTestCase):
    def test_1(self):
        nums = [3, 4, 5, 1, 2]
        actual = Solution().findMin(nums)
        self.assertEqual(1, actual)

    def test_2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        actual = Solution().findMin(nums)
        self.assertEqual(0, actual)

    def test_3(self):
        nums = [11, 13, 15, 17]
        actual = Solution().findMin(nums)
        self.assertEqual(11, actual)

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
