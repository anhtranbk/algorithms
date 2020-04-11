#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
from typing import List

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass

    def threeSum_firstVersion(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        rs = set()
        for i in range(0, len(nums)):
            if nums[i] in visited: continue
            visited.add(nums[i])

            d = dict()
            x = nums[i]
            for j in range(i+1, len(nums)):
                d[-x-nums[j]] = j

            for j in range(i+1, len(nums)):
                y = nums[j]
                if y in d and d[y] == j:
                    z = -(x + y)
                    rs.add(tuple(sorted([x, y, z])))
        return rs

    def threeSum_secondVersion(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        rs = set()
        for i, x in enumerate(nums):
            if x in visited: continue
            visited.add(x)

            arrs = self.twoSum(nums, i, -x)
            for arr in arrs:
                arr = sorted(arr.append(x))
                rs.add(arr)
        return rs

    def twoSumFor3Sum(self, nums: List[int], x_idx: int, target: int) -> List[List[int]]:
        rs, d= [], dict()
        for j in range(x_idx, len(nums)):
            d[target-y] = j
        
        for j in range(x_idx, len(nums)):
            y = nums[j]
            if y in d and d[y] != j:
                z = d[y]
                rs.append([y, z])

        return rs

    def threeSum_withSorting(self, nums: List[int]) -> List[List[int]]:
        rs = []
        nums = sorted(nums)
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue

            d = dict()
            x = nums[i]
            for j in range(i+1, len(nums)):
                if i != j:
                    d[-x-nums[j]] = j
                    
            for j in range(i+1, len(nums)):
                if x+nums[j] > 0:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                y = nums[j]
                if y in d and d[y] > j:
                    z = -(x + y)
                    rs.append([x, y, z])
        return rs

    def twoSumFor3Sum_withSorting(self, 
        nums: List[int], 
        x_idx: int, 
        target: int
    ) -> List[List[int]]:
        rs = []
        d = dict()
        for y, j in enumerate(nums):
            if x_idx != j:
                d[target-y] = j
        
        for y, j in enumerate(nums):
            if y in d and d[y] != j:
                z = d[y]
                rs.append([y, z])

        return rs

        
# @lc code=end

