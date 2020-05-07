from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == 0:
                self.move_zero(nums, i)
            i -= 1
            
        
    def move_zero(self, nums, i):
        while i+1 < len(nums) and nums[i+1] != 0:
            self.swap(nums, i, i+1)
            i += 1
        
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp