#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
import unittest
from common import BaseTestCase
from typing import List

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[i-1] < nums[j]:
                        break
                nums[i-1], nums[j] = nums[j], nums[i-1]
                self.reverseInPlace(nums, i)
                return

        self.reverseInPlace(nums, 0)

    def reverseInPlace(self, nums: List[int], i: int):
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
        
# @lc code=end
class P31TestCase(BaseTestCase):
    def test1(self):
        nums = [4, 5, 3, 2, 1]
        expected = [5, 1, 2, 3, 4]
        Solution().nextPermutation(nums)
        self.assertArrayEquals(expected, actual=nums)

    def test2(self):
        nums = [3, 2, 1]
        expected = [1, 2, 3]
        Solution().nextPermutation(nums)
        self.assertArrayEquals(expected, actual=nums)

    def test3(self):
        nums = [1, 2, 3]
        expected = [1, 3, 2]
        Solution().nextPermutation(nums)
        self.assertArrayEquals(expected, actual=nums)

    def test4(self):
        nums = [2, 3, 1]
        expected = [3, 1, 2]
        Solution().nextPermutation(nums)
        self.assertArrayEquals(expected, actual=nums)

    def test5(self):
        nums = [1, 3, 2]
        expected = [2, 1, 3]
        Solution().nextPermutation(nums)
        self.assertArrayEquals(expected, actual=nums)


if __name__ == '__main__':
    unittest.main()
