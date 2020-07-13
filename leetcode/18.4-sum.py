#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
from typing import List, Dict
import unittest
from common import BaseTestCase


# @lc code=start
class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for a in range(len(nums) - 3):
            if a == 0 or nums[a] != nums[a - 1]:
                self.threeSum(nums, a, target - nums[a], ans)
        return ans

    def threeSum(self, nums: List[int], a: int, target: int,
                 ans: List[List[int]]):
        for b in range(a + 1, len(nums) - 2):
            if b == a + 1 or nums[b] != nums[b - 1]:
                # self.twoSum(nums, a, b, target - nums[b], ans)
                self.twoSum_better(nums, a, b, target - nums[b], ans)

    def twoSum(self, nums: List[int], a: int, b: int, target: int,
               ans: List[List[int]]):
        cache: Dict[int, List[List[int]]] = dict()
        for c in range(b + 1, len(nums)):
            if nums[c] in cache:
                for e in cache.get(nums[c], []):
                    e.append(nums[c])
                    ans.append(e)
                del cache[nums[c]]

            if c == b + 1 or nums[c] != nums[c - 1]:
                key = target - nums[c]
                val = [nums[a], nums[b], nums[c]]
                if key in cache:
                    cache[key].append(val)
                else:
                    cache[key] = [val]

    def twoSum_better(self, nums: List[int], a: int, b: int, target: int,
                      ans: List[List[int]]):
        c, d = b + 1, len(nums) - 1
        while c < d:
            t = nums[c] + nums[d]
            if t < target:
                c += 1
            elif t > target:
                d -= 1
            else:
                ans.append([nums[a], nums[b], nums[c], nums[d]]) 
                while c < d and nums[c] == nums[c+1]: 
                    c += 1
                while c < d and nums[d] == nums[d-1]: 
                    d -= 1
                c += 1
                d -= 1


# @lc code=end
class P18TestCase(BaseTestCase):

    def test1(self):
        nums = [1, 0, -1, 0, -2, 2]
        expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        actual = Solution().fourSum(nums, target=0)
        # print(actual)

        self.assertEqual(len(expected), len(actual))
        for i in range(len(expected)):
            self.assertArrayEquals(expected[i],
                                   actual[i],
                                   sorted_before_comparing=True)

    def test2(self):
        nums = [2, 2, 2, 2, 2]
        expected = [[2, 2, 2, 2]]
        actual = Solution().fourSum(nums, target=8)
        # print(actual)

        self.assertEqual(len(expected), len(actual))
        for i in range(len(expected)):
            self.assertArrayEquals(expected[i],
                                   actual[i],
                                   sorted_before_comparing=True)


if __name__ == '__main__':
    unittest.main()
