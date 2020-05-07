from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 1
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            elif j <= i:
                j = i + 1
            elif nums[i] != 0:
                i += 1
            else:
                self.swap(nums, i, j)
                i += 1
                j += 1
    

    def swap(self, nums, i, j):
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t