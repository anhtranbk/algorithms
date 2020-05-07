#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
from typing import List

# @lc code=start
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
                nums[i] = nums[j]
                nums[j] = 0
                i += 1
                j += 1

# @lc code=end
if __name__ == '__main__':
    # nums = [0, 0, 1, 2, 0, 0, 3, 0, 4, 0, 0, 5]
    nums = [4,2,4,0,0,3,0,5,1,0]
    print(nums)

    Solution().moveZeroes(nums=nums)
    print(nums)
