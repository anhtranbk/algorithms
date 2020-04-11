from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rs = []
        nums = sorted(nums)
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

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
