#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
from typing import List
import math

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = k = 0
        size = len(nums1) + len(nums2)
        hs = math.ceil(size / 2)
        nums = [0] * size
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums[k] = nums1[i]
                i += 1
            else:
                nums[k] = nums2[j]
                j += 1
            k += 1
        while i < len(nums1):
            nums[k] = nums1[i]
            k += 1
            i += 1
        while j < len(nums2):
            nums[k] = nums2[j]
            k += 1
            j += 1
        if size % 2 != 0:
            return nums[hs-1]
        else:
            return (nums[hs-1] + nums[hs]) / 2
        
# @lc code=end

