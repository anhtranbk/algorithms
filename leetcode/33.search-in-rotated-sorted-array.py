#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
from typing import Dict, List, Optional

from common import BaseTestCase, unittest


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1

        shifted = self.find_min_index(nums)
        lo, hi = shifted, shifted + n - 1
        while lo < hi:
            m = lo + (hi - lo) // 2
            # calculate real index for m
            real_mid = m % n
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                lo = m + 1
            else:
                hi = m

        lo %= n
        return lo if nums[lo] == target else -1

    def find_min_index(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            m = lo + (hi - lo) // 2
            if nums[m] < nums[m - 1] and nums[m] < nums[m + 1]:
                return m
            if nums[m] < nums[hi]:
                hi = m
            else:
                lo = m + 1
        return lo


# @lc code=end
class P33TestCase(BaseTestCase):
    def test_1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        actual = Solution().search(nums, 0)
        self.assertEqual(4, actual)

    def test_2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        actual = Solution().search(nums, 3)
        self.assertEqual(-1, actual)

    def test_3(self):
        nums = [1]
        actual = Solution().search(nums, 0)
        self.assertEqual(-1, actual)

    def test_4(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        actual = Solution().search(nums, 6)
        self.assertEqual(2, actual)

    def test_5(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        actual = Solution().search(nums, 1)
        self.assertEqual(5, actual)

    def test_6(self):
        nums = [1, 3]
        actual = Solution().search(nums, 3)
        self.assertEqual(1, actual)

    def test_7(self):
        nums = [3, 1]
        actual = Solution().search(nums, 3)
        self.assertEqual(0, actual)


if __name__ == "__main__":
    unittest.main()
